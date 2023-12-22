
import multiprocessing
from generator.timetable import Timetable
import conf
from watchdog.dog import Watchdog

def main():
    """
    Main function to run the program.
    """
    num_cores = multiprocessing.cpu_count()
    processes = []
    # Create an instance of the Timetable class
    t = Timetable(conf.timetable.copy())

    # Start multiple processes to run the main function concurrently
    for _ in range(num_cores):
        # Timeout maximum must be 2 min
        watchdog_process = multiprocessing.Process(target=Watchdog(120, multiprocessing.current_process().pid).run)
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
