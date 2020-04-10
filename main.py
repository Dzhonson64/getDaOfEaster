if __name__ == '__main__':
    year = 2020
    month = "апрель"
    day = 0
    pp = (19 * (year % 19) + 15) % 30
    a = 12 + pp
    if a <= 31:
        month = "март"
    b = (2*(year % 4) + 4*(year%7) + 6 * pp + 6) % 7
    f = pp + b
    if f <= 9:
        print(str(22+f+13) + " марта")
    else:
        print(str(f - 9+13) + " апреля")
