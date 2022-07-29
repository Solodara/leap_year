# Програма для визначення року. Висикосний чи ні 

def is_year_leap(x):
    if x%4==0:
        return True
    else:
        return False

year = int(input('введіть будь який рік: '))

print(is_year_leap(year))