from utils import euler_lib


def main():

    # make prints easier to read for testing
    week = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
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
    wd = 1  # jan 1 1901 is a tuesday
    for year in range(1901, 2001):

        if euler_lib.is_leap_year(year):
            months["February"] = 29
        else:
            months["February"] = 28

        for _, days in months.items():
            for day in range(1, days + 1):

                if week[wd] == "Sunday" and day == 1:
                    total += 1

                if wd == 6:
                    wd = 0
                else:
                    wd += 1

    return total


if __name__ == "__main__":
    print(main())
