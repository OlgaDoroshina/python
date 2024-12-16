year_as_string = input("Enter a year: ")
year = int(year_as_string)

def is_year_leap():
    if year % 4 == 0:
        print("Year", year, ":", True)

    else:
        print("Year", year, ":", False)

is_year_leap()