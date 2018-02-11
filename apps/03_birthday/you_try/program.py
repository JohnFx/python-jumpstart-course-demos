#Birthday Application
import datetime


def print_header():
    print("---------------------------------")
    print("-------     Birthday   ----------")
    print("---------------------------------")
    print()


def get_birthday_from_user():
    birth_year = int(input("What year were you born (yyyy): "))
    birth_month = int(input ("What month were you borm  (mm): "))
    birth_day = int(input ("What day were you borm  (dd): "))
    
    return datetime.date(birth_year,birth_month,birth_day)

def compute_days_between_dates(date1,date2):
    date1_thisyear = datetime.date(date2.year,date1.month,date1.day)
    return (date1_thisyear-date2).days
    
def print_birthday_information(days_until_birthday):
    if days_until_birthday<0:
        print("Your birthday was {0} days ago".format(abs(days_until_birthday)))   
    elif days_until_birthday>0:
        print("Your birthday is in {0} days".format(days_until_birthday))
    else:
        print("Happy Birthday")

def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    days_until_birthday = compute_days_between_dates(bday,today)
    print_birthday_information(days_until_birthday)


main()