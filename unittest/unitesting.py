import unittest
from generator.timetable import Timetable
import conf


class TestTimetable(unittest.TestCase):
    def test_check_better_than_origo(self):
        t = Timetable(conf.timetable.copy())
        # Initially, count_of_evaluated_tables should be 0
        self.assertEqual(t.get_evaluated_tables(), 0)

        # Evaluate a timetable with a better score than the original
        better_score = t.score_of_original + 10
        self.assertTrue(t.check_better_than_origo(better_score))
        self.assertEqual(t.get_evaluated_tables(), 1)

        # Evaluate a timetable with a worse score than the original
        worse_score = t.score_of_original - 10
        self.assertFalse(t.check_better_than_origo(worse_score))
        self.assertEqual(t.get_evaluated_tables(), 1)

    def test_generate_table(self):
        t = Timetable(conf.timetable.copy())
        # Initially, count_of_tables should be 0
        self.assertEqual(t.count_of_tables, 0)

        # Generate a table and check count_of_tables
        t.generate_table()
        self.assertEqual(t.count_of_tables, 1)

class TestTimetableEvaluator(unittest.TestCase):
    def test_get_best_score(self):
        t = Timetable(conf.timetable.copy())
        # Initially, the best score should be 0
        self.assertEqual(t.get_best_score(), 0)

        # Update the best score and check again
        t.best_score = 100
        self.assertEqual(t.get_best_score(), 100)