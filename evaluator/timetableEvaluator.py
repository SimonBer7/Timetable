import conf

timetable = conf.timetable.copy()

class TimetableEvaluator:
    """
        The TimetableEvaluator class handles the evaluation of timetables based on various criteria.

        Attributes:
        - attendance_rules (dict): A dictionary containing attendance rules for each subject.
        - subject_repetition_penalty (int): Penalty for repeating a subject on the same day.
        - location_change_penalty (int): Penalty for changing the location between subjects on the same day.
        - lunch_penalty (int): Penalty for scheduling subjects during lunchtime.
        - daily_study_limit (int): Maximum limit for the number of daily study hours.

        Methods:
        - __init__(): Initializes the TimetableEvaluator with default evaluation parameters.
        - get_subject(number): Returns the Leason instance corresponding to the given subject number.
        - evaluate_timetable(table): Evaluates the entire timetable and returns the overall score.
        - evaluate_day(lessons): Evaluates a single day's timetable and returns the score.
        """

    def __init__(self):
        """
            Initializes the TimetableEvaluator with default evaluation parameters.
        """
        # 1
        self.attendance_rules = {
            "WA": 50,
            "C": 30,
            "AJ": 20,
            "M": 40,
            "PV": 30,
            "TP": 20,
            "DS": 10,
            "AM": 40,
            "TV": 10,
            "PIS": 30,
            "CIT": 20,
            "PSS": 10,
        }
        # 2
        self.subject_repetition_penalty = -20
        # 3
        self.location_change_penalty = -10
        # 4
        self.lunch_penalty = -30
        # 5
        self.daily_study_limit = 60

    def get_subject(self, number):
        """
            Returns the Leason instance corresponding to the given subject number.

            Parameters:
            - number (int): The subject number.

            Returns:
            - Leason: The Leason instance corresponding to the subject number.
        """
        if number == 1:
            return conf.WA
        elif number == 2:
            return conf.C
        elif number == 3:
            return conf.AJ
        elif number == 4:
            return conf.M
        elif number == 5:
            return conf.PV
        elif number == 6:
            return conf.TP
        elif number == 7:
            return conf.DS
        elif number == 8:
            return conf.AM
        elif number == 9:
            return conf.TV
        elif number == 10:
            return conf.PIS
        elif number == 11:
            return conf.CIT
        elif number == 12:
            return conf.PSS
        else:
            return conf.VH

    def evaluate_timetable(self, table):
        """
            Evaluates the entire timetable and returns the overall score.

            Parameters:
            - table (list): List representing a timetable using Leason IDs for each day.

            Returns:
            - int: The overall score of the timetable.
        """
        score = 0
        for i in range(5):
            score += self.evaluate_day(table[i])
        return score

    def evaluate_day(self, lessons):
        """
            Evaluates a single day's timetable and returns the score.

            Parameters:
            - lessons (list): List of Leason IDs representing subjects scheduled for the day.

            Returns:
            - int: The score of the day's timetable.
        """
        score = 0
        subjects_in_day = set()
        for lesson in lessons:
            tmp = self.get_subject(lesson)
            # 1
            score += self.attendance_rules.get(lesson, 0)

            # 2
            if lesson in subjects_in_day:
                score += self.subject_repetition_penalty
            else:
                subjects_in_day.add(lesson)

            # 3
            if tmp.floor_number != lessons[0]:
                score += self.location_change_penalty

            # 4
            if tmp.id in {5, 6, 7, 8}:
                score += self.lunch_penalty

            # 5
            self.daily_study_limit -= 1
            if self.daily_study_limit < 0:
                score += self.daily_study_limit * self.lunch_penalty
        return score


