class BerlinClock:

    @classmethod
    def from_str(cls, time_str):
        return cls(*time_str.split(':'))

    def __init__(self, hour=None, minute=None, second=None):
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)

    def __str__(self):
        first = self._1st_row()
        second = self._2nd_row()
        third = self._3rd_row()
        fourth = self._4th_row()
        fifth = self._5th_row()
        return '{}\n{}\n{}\n{}\n{}'.format(first, second, third, fourth, fifth)

    def display(self):
        return self.__str__()

    def _1st_row(self):
        return 'Y' if self.second % 2 else 'O'

    def _2nd_row(self):
        return self._pattern('R', self.hour // 5, 4)

    def _3rd_row(self):
        return self._pattern('R', self.hour % 5, 4)

    def _4th_row(self):
        minute_floordiv_five = self.minute // 5
        row = self._pattern('', minute_floordiv_five, 11)
        for i in reversed(range(minute_floordiv_five)):
            row = ('R' if i % 3 == 2 else 'Y') + row
        return row

    def _5th_row(self):
        return self._pattern('Y', self.minute % 5, 4)

    def _pattern(self, *args):
        if len(args) == 3:
            return args[0] * args[1] + 'O' * (args[2] - args[1])

if __name__ == '__main__':
    import time
    current_time = time.strftime('%H:%M:%S')
    berlin_clock = BerlinClock.from_str(current_time)
    print(current_time)
    print(berlin_clock)

