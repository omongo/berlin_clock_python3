class BerlinClock:

    def __init__(self, hour=None, minute=None, second=None):
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)

    @classmethod
    def from_str(cls, time_str):
        return cls(*time_str.split(':'))

    def display(self):
        return '{} {} {}'.format(self._sec_pos(), self._hour_pos(), self._min_pos())

    def _sec_pos(self):
        return 'Y' if self.second % 2 else 'O'

    def _hour_pos(self):
        hour1 = self._pattern('R', self.hour // 5, 4)
        hour2 = self._pattern('R', self.hour % 5, 4)
        return '{} {}'.format(hour1, hour2)

    def _min_pos(self):
        minute_div_five = self.minute // 5
        minute_mod_five = self.minute % 5
        min1 = 'O' * (11 - minute_div_five)
        for i in reversed(range(minute_div_five)):
            min1 = ('R' if i % 3 == 2 else 'Y') + min1
        min2 = self._pattern('Y', self.minute % 5, 4)
        return '{} {}'.format(min1, min2)

    def _pattern(self, *args):
        return args[0] * args[1] + 'O' * (args[2] - args[1])
