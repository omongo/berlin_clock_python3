import unittest

from berlin_clock import BerlinClock

class testBerlinClock(unittest.TestCase):
    def test_000000(self):
        berlin_clock = BerlinClock.from_str('00:00:00')
        expected = 'O\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_000001(self):
        berlin_clock = BerlinClock.from_str('00:00:01')
        expected = 'Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_050001(self):
        berlin_clock = BerlinClock.from_str('05:00:01')
        expected = 'Y\nROOO\nOOOO\nOOOOOOOOOOO\nOOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_100001(self):
        berlin_clock = BerlinClock.from_str('10:00:01')
        expected = 'Y\nRROO\nOOOO\nOOOOOOOOOOO\nOOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_110001(self):
        berlin_clock = BerlinClock.from_str('11:00:01')
        expected = 'Y\nRROO\nROOO\nOOOOOOOOOOO\nOOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_120001(self):
        berlin_clock = BerlinClock.from_str('12:00:01')
        expected = 'Y\nRROO\nRROO\nOOOOOOOOOOO\nOOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_120101(self):
        berlin_clock = BerlinClock.from_str('12:01:01')
        expected = 'Y\nRROO\nRROO\nOOOOOOOOOOO\nYOOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_120201(self):
        berlin_clock = BerlinClock.from_str('12:02:01')
        expected = 'Y\nRROO\nRROO\nOOOOOOOOOOO\nYYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_120701(self):
        berlin_clock = BerlinClock.from_str('12:07:01')
        expected = 'Y\nRROO\nRROO\nYOOOOOOOOOO\nYYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_121201(self):
        berlin_clock = BerlinClock.from_str('12:12:01')
        expected = 'Y\nRROO\nRROO\nYYOOOOOOOOO\nYYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_121701(self):
        berlin_clock = BerlinClock.from_str('12:17:01')
        expected = 'Y\nRROO\nRROO\nYYROOOOOOOO\nYYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_123201(self):
        berlin_clock = BerlinClock.from_str('12:32:01')
        expected = 'Y\nRROO\nRROO\nYYRYYROOOOO\nYYOO'
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)
