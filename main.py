from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    today_date = datetime.now(tz=None)
    print('Hi! Today is ', today_date.date())
    calculate_salary()
    get_employees()


