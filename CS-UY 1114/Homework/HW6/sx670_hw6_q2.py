def print_month_calendar (num_of_days, starting_day):
    print("Mon","Tue","Wed","Thr","Fri","Sat","Sun",sep="\t")
    if(starting_day==0):
        starting_day=7
    for i in range (1,starting_day):
        print(" "*3,"\t",end="")
    current_day=starting_day
    for i in range (1,num_of_days+1):
        print(i,"\t",end="")
        if(current_day==7):
            print("")
            current_day=1
        else:
            current_day+=1
    if(current_day!=1):
        print("\n")
        return current_day-1
    else:
        print("")
        return 7

def leap_year (year):
    if (year%4==0):
        if (year%100!=0 or year%400==0):
            return True
        else:
            return False
    else:
        return False

def print_year_calendar (year, starting_day):
    print("January",year)
    last_day=print_month_calendar (31,starting_day)
    print("February",year)
    if(leap_year(year)):
        last_day=print_month_calendar (29,(last_day+1)%7)
    else:
        last_day=print_month_calendar (28,(last_day+1)%7)
    print("March",year)
    last_day=print_month_calendar (31,(last_day+1)%7)
    print("April",year)
    last_day=print_month_calendar (30,(last_day+1)%7)
    print("May",year)
    last_day=print_month_calendar (31,(last_day+1)%7)
    print("June",year)
    last_day=print_month_calendar (30,(last_day+1)%7)
    print("July",year)
    last_day=print_month_calendar (31,(last_day+1)%7)
    print("August",year)
    last_day=print_month_calendar (31,(last_day+1)%7)
    print("September",year)
    last_day=print_month_calendar (30,(last_day+1)%7)
    print("October",year)
    last_day=print_month_calendar (31,(last_day+1)%7)
    print("November",year)
    last_day=print_month_calendar (30,(last_day+1)%7)
    print("December",year)
    last_day=print_month_calendar (31,(last_day+1)%7)


def main():
    year=int(input("Please enter the year:"))
    starting_day=int(input("Please enter the starting day of the year:"))
    print_year_calendar(year,starting_day)

main()
        
    


