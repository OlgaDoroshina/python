month = int(input("Ввод номера месяца (in range from 1 to 12): "))

def month_to_season(month):
        if month in [12, 1, 2]:
            print(f"Месяц {month} зима")
        elif month in [3, 4, 5]:
            print(f"Месяц {month} весна")
        elif month in [6, 7, 8]:
             print(f"Месяц {month} лето")
        elif month in [9, 10, 11]:
             print(f"Месяц {month} осень")
        else:
             print("Месяц")
             month = int(input("Месяц (in range from 1 to 12): "))
        
month_to_season(month)