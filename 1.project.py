class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m  
        self.y = y


monthDays = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]


def countLeapYears(d): 
    years = d.y


    if (d.m <= 2):
        years = 1
    return int(years / 4) - int(years / 100) + int(years / 400)


def getDifference(dt1, dt2):

    n1 = dt1.y * 365 + dt1.d   
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]    
    n1 += countLeapYears(dt1)

    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]

    n2 += countLeapYears(dt2)
    return (n2 - n1)

print("Enter your date of birth:)")
d1=int(input("Date:"))
m1=int(input("Month:"))
y1=int(input("Year:"))

print("EnterToday's Date>")
d2=int(input("Date:"))
m2=int(input("Month:"))
y2=int(input("Year:"))

dt1 = Date(d1, m1, y1)
dt2 = Date(d2, m2, y2)


print(getDifference(dt1, dt2), "Days You Are survieved in this World!")