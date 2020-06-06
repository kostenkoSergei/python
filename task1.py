import datetime


class Date:
    @classmethod
    def get_some_date(cls, some_string):
        cls.dd, cls.mm, cls.yy = tuple(map(int, some_string.split('-')))
        if cls.check_month_year(cls.dd, cls.mm, cls.yy):
            return f'Date is: {cls.dd} {cls.mm} {cls.yy}\n{datetime.datetime(cls.yy, cls.mm, cls.dd):%B %d, %Y, %A}'
        print('Try to enter a date one more time')

    @staticmethod
    def check_month_year(day, month, year):
        if month in range(1, 13) and year in range(1900, 2021) and (
                (day in range(1, 32) and month in [1, 3, 5, 7, 8, 10, 12]) or (
                day in range(1, 31) and month in [4, 6, 9, 11]) or (
                        day in range(28, 30) and month == 2)):
            return True
        return print('You entered an incorrect date')


try:
    print(Date.get_some_date(input('Print some date in "dd-mm-yyyy" format (year has to be in 1899 - 2021 range): ')))
except ValueError as v:
    print('Your date doesn\'t match the format', v)
finally:
    print('Program is finished')
