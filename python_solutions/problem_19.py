import euler_lib


def main():

    # make prints easier to read for testing
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = {
                "January":      31,
                "February":     28,
                "March":        31,
                "April":        30,
                "May":          31,
                "June":         30,
                "July":         31,
                "August":       31,
                "September":    30,
                "October":      31,
                "November":     30,
                "December":     31
                }

    total = 0
    wd = 1 # jan 1 1901 is a tuesday
    for year in range(1901, 2001):

        if euler_lib.is_leap_year(year):
            months["February"] = 29
        else:
            months["February"] = 28

        for month in months:
            for day in range(1, months[month] + 1):
                
                if week[wd] == "Sunday" and day == 1:
                    total += 1
                
                if wd == 6:
                    wd = 0
                else:
                    wd += 1

    return total

def description():

    desc = """
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
    print(desc, end="")

pe_name = "COUNTING SUNDAYS"
pe_solution = 171

if __name__ == "__main__":
    print(main())
