import random
import time
import itertools
import multiprocessing
from watchdog.dog import Watchdog
from evaluator.timetableEvaluator import TimetableEvaluator
import conf


"""
Create a list representing a timetable using the IDs of Leason instances
"""
timetable = conf.timetable.copy()

"""
Define the Timetable class to work with timetables
"""
class Timetable:
    """
    The Timetable class handles the generation and evaluation of timetables.

    Attributes:
    - table (list): A list representing a timetable using Leason IDs.
    - duplicate_of_table (list): A copy of the original timetable for reference.
    - perm (list): A list to store permutations of Leason IDs.
    - evaluator (TimetableEvaluator): An instance of the TimetableEvaluator class for scoring.
    - score_of_original (int): The score of the original timetable.
    - better_than_origo (int): The count of tables better than the original.
    - count_of_tables (int): The total count of generated tables.
    - better_table (dict): A dictionary to store better tables for each day of the week.

    Methods:
    - check_better_than_origo(score): Checks if the given score is better than the original and updates the count.
    - get_better_than_origo(): Returns the count of tables better than the original.
    - get_days_of_original(): Gets a list of Leason IDs for each day from the original timetable.
    - get_table_origi(): Gets the score of the original timetable.
    - generate_permutations(): Generates permutations of Leason IDs and adds them to the permutations list.
    - generate_table(): Generates a timetable and evaluates its score.
    - get_count_of_generated_tables(): Gets the count of generated tables.
    - overload_processors(duration=10): Overloads processors by shuffling the timetable for a specified duration.
    - shuffle(): Shuffles the table (list of Leason IDs).

    """
    def __init__(self, table):
        """
        Initializes instance variables.
        :param table: List representing a timetable using Leason IDs.
        """
        self.count_of_permutations = 0
        self.table = table
        self.duplicate_of_table = timetable.copy()
        self.perm = []
        self.evaluator = TimetableEvaluator()
        self.score_of_original = 0
        self.count_of_evaluated_tables = 0
        self.count_of_tables = 0
        self.best_score = 0
        self.better_table = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": []
        }


    def get_best_score(self):
        """
        Returns the best score achieved during the generation process.
        """
        return self.best_score

    def check_score(self, score):
        """
        Checks if the given score is better than the current best score, updating it if true.
        """
        if self.best_score < score:
            self.best_score = score
            return True
        else:
            return False

    def check_better_than_origo(self, score):
        """
        Checks if the given score is better than the original score.
        :param score: The score to compare.
        :return: True if better, False otherwise.
        """
        if self.score_of_original < score:
            self.count_of_evaluated_tables += 1
            return True
        else:
            return False

    def get_evaluated_tables(self):
        """
        Returns the count of tables better than the original.
        :return: The count of better tables.
        """
        return self.count_of_evaluated_tables

    def get_days_of_original(self):
        """
        Gets a list of Leason IDs for each day from the original timetable.
        :return: List of Leason IDs.
        """
        tmp = []
        for i in range(10):
            tmp.append((self.duplicate_of_table.pop()))
        return tmp

    def get_table_origi(self):
        """
        Gets the score of the original timetable.
        :return: The score of the original timetable.
        """
        tmp = []
        score = 0
        for days in range(5):
           tmp.append(self.get_days_of_original())
        score += self.evaluator.evaluate_timetable(tmp)
        self.check_score(score)
        self.score_of_original = score
        return self.score_of_original

    def generate_permutations(self):
        """
        Generates permutations of Leason IDs and adds them to the permutations list.
        :return: List of Leason IDs.
        """
        tmp = []
        for i in range(10):
            tmp.append((self.table.pop()))
        self.perm.extend(list(set(itertools.permutations(tmp))))
        return tmp

    def generate_table(self):
        """
        Generates a timetable and evaluates its score.
        """
        tmp = []
        score_of_table = 0
        self.shuffle()
        for i in range(5):
            tmp.append(self.generate_permutations())
        score_of_table = self.evaluator.evaluate_timetable(tmp)
        self.check_better_than_origo(score_of_table)
        self.count_of_tables += 1


    def get_count_of_generated_tables(self):
        """
        Gets the count of generated tables.
        :return: The count of generated tables.
        """
        self.count_of_permutations = len(self.perm)
        return int(self.count_of_permutations / 5)

    def overload_processors(self, duration=10):
        """
        Overloads processors by shuffling the timetable for a specified duration.
        :param duration: The duration in seconds to overload processors.
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            self.shuffle()

    def shuffle(self):
        """
        Shuffles the table (list of Leason IDs).
        """
        self.table = timetable.copy()
        random.shuffle(self.table)


def main():
    """
    Main function to run the program.
    """
    num_cores = multiprocessing.cpu_count()
    processes = []
    # Create an instance of the Timetable class
    t = Timetable(timetable)

    # Start multiple processes to run the main function concurrently
    for _ in range(num_cores):
        # Timeout maximum must be 2 min
        watchdog_process = multiprocessing.Process(target=Watchdog(60, multiprocessing.current_process().pid).run)
        shuffle = multiprocessing.Process(target=t.overload_processors, args=(10,))
        shuffle.start()
        watchdog_process.start()
        processes.append(watchdog_process)

    for process in processes:
        # Generate tables until the Watchdog process is alive
        while process.is_alive():
            t.generate_table()

    # Wait for the Watchdog process to finish
    for process in processes:
        process.join()
        process.terminate()

    # Print the results
    print("Score puvodniho rozvrhu: " + str(t.get_table_origi()))
    print("Pocet vygerovanych rozvrhu: " + str(t.get_count_of_generated_tables()))
    print("Best score: " + str(t.get_best_score()))
    print("Pocet ohodnocenych rozvrhu: " + str(t.get_evaluated_tables()))

if __name__ == "__main__":
    main()




