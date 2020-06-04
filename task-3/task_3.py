import sys
from datetime import datetime, timedelta


class GetStartEndDateWeek:

    def __init__(self, input_date):
        self.input_date = input_date
        self.format_date = '%Y-%m-%d'

    def get_start_date_week(self):
        input_date = datetime.strptime(self.input_date, self.format_date)
        start_date = input_date - timedelta(days=input_date.weekday())
        return start_date

    def get_end_date_week(self):
        end_date = self.get_start_date_week() + timedelta(days=6)
        return end_date


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print 'Must provide a date with format YYYY-MM-DD as the argument'
        sys.exit(1)

    GetStartEndDateWeek = GetStartEndDateWeek(sys.argv[1])
    start_date = GetStartEndDateWeek.get_start_date_week()
    end_date = GetStartEndDateWeek.get_end_date_week()

    print 'start date week:', start_date.strftime(GetStartEndDateWeek.format_date)
    print 'end date week:', end_date.strftime(GetStartEndDateWeek.format_date)
