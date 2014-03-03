import unittest

from berlin_clock import BerlinClock

class testBerlinClock(unittest.TestCase):
    def test_000000(self):
        berlin_clock = BerlinClock.from_str('00:00:00')
        expected = 'O OOOO OOOO OOOOOOOOOOO OOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_000001(self):
        berlin_clock = BerlinClock.from_str('00:00:01')
        expected = 'Y OOOO OOOO OOOOOOOOOOO OOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_050001(self):
        berlin_clock = BerlinClock.from_str('05:00:01')
        expected = 'Y ROOO OOOO OOOOOOOOOOO OOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_100001(self):
        berlin_clock = BerlinClock.from_str('10:00:01')
        expected = 'Y RROO OOOO OOOOOOOOOOO OOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_110001(self):
        berlin_clock = BerlinClock.from_str('11:00:01')
        expected = 'Y RROO ROOO OOOOOOOOOOO OOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_120001(self):
        berlin_clock = BerlinClock.from_str('12:00:01')
        expected = 'Y RROO RROO OOOOOOOOOOO OOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_120101(self):
        berlin_clock = BerlinClock.from_str('12:01:01')
        expected = 'Y RROO RROO OOOOOOOOOOO YOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_120201(self):
        berlin_clock = BerlinClock.from_str('12:02:01')
        expected = 'Y RROO RROO OOOOOOOOOOO YYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_120701(self):
        berlin_clock = BerlinClock.from_str('12:07:01')
        expected = 'Y RROO RROO YOOOOOOOOOO YYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_121201(self):
        berlin_clock = BerlinClock.from_str('12:12:01')
        expected = 'Y RROO RROO YYOOOOOOOOO YYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_121701(self):
        berlin_clock = BerlinClock.from_str('12:17:01')
        expected = 'Y RROO RROO YYROOOOOOOO YYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_123201(self):
        berlin_clock = BerlinClock.from_str('12:32:01')
        expected = 'Y RROO RROO YYRYYROOOOO YYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)
