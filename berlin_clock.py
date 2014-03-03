class BerlinClock:

    @classmethod
    def from_str(cls, time_str):
        return cls(*time_str.split(':'))

    def __init__(self, hour=None, minute=None, second=None):
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)

    def __str__(self):
        second_row = self._second_row()
        hour_rows = self._hour_rows()
        minute_rows = self._minute_rows()
        return '{}\n{}\n{}'.format(second_row, hour_rows, minute_rows)

    def _second_row(self):
        return 'Y' if self.second % 2 else 'O'

    def _hour_rows(self):
        hour_1 = self._pattern('R', self.hour // 5, 4)
        hour_2 = self._pattern('R', self.hour % 5, 4)
        return '{}\n{}'.format(hour_1, hour_2)

    def _minute_rows(self):
        minute_div_five = self.minute // 5
        min_1 = self._pattern('', minute_div_five, 11)
        for i in reversed(range(minute_div_five)):
            min_1 = ('R' if i % 3 == 2 else 'Y') + min_1
        min_2 = self._pattern('Y', self.minute % 5, 4)
        return '{}\n{}'.format(min_1, min_2)

    def _pattern(self, *args):
        return args[0] * args[1] + 'O' * (args[2] - args[1])

if __name__ == '__main__':
    import time
    current_time = time.strftime('%H:%M:%S')
    berlin_clock = BerlinClock.from_str(time.strftime('%H:%M:%S'))
    print(current_time)
    print(berlin_clock)
