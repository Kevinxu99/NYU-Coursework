m=int(input("Please enter an integer between 1 and 12: "))
import calendar
if(m==2):
    print("The entered month is February and the number of days in February is 28")
if(m<=7 and m!=2):
    if (m%2==1):
        print("The entered month is",calendar.month_name[m],"and the number of days in",calendar.month_name[m],"is 31")
    else:
        print("The entered month is",calendar.month_name[m],"and the number of days in",calendar.month_name[m],"is 30")
if(m>7):
    if(m%2==0):
        print("The entered month is",calendar.month_name[m],"and the number of days in",calendar.month_name[m],"is 31")
    else:
        print("The entered month is",calendar.month_name[m],"and the number of days in",calendar.month_name[m],"is 30")


