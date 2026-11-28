import datetime
import calendar
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
time = now.strftime("%I:%M %p").lstrip("0")
optionstxt = """----------------------------
Countdown to a date
         1 """

xmas = """
        *
        ^
       ^^^
      ^^^^^^   
    ^^^^^^^^^^
        ||"""

while True:
    print("\033[H\033[J", end="")
    print(calendar.month(year, month))
    print(f"Current Date:", month, day, year)
    print(f"Current Time:", time)
    if month == 11 and day > 22:
            print(xmas)
    elif month == 12:
            print(xmas)
    
    option = int(input(optionstxt))

    def eventcalc():
        today = datetime.date(year, month, day)
        event = datetime.date(year, eventmonth, eventdate)

        difference = (event - today).days

        print(f"Event is {difference} Days from now")

    if option == 1:
        eventmonth = int(input("Month: "))
        eventdate = int(input("Day: "))
        eventcalc()
        input()
input()