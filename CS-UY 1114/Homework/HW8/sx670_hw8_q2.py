'''

Kevin Xu
CS 1114
sx670

Purpose of program
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.
    cf=open(cleaned_weather_filename,"w+")
    f=open(complete_weather_filename,"r")
    #cf.write("City,Date,High,Low,Precipitation\n")
    for line in f:
        lst=line.split(",")
        s=""
        s=s+lst[0]+","+lst[1]+","+lst[2]+","+lst[3]+","
        if(lst[8]=='T'):
            s=s+'0'+'\n'
        else:
            s=s+lst[8]+'\n'
        cf.write(s)
    cf.close()
    f.close()

# Part B
def f_to_c(f_temperature):
    return ((f_temperature-32)*5)/9 # modify this

def in_to_cm(inches):
    return inches*2.54 # modify this

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    # Similar to clean_data() - read in the file and make a new file with metric values.
    wm=open(metric_weather_filename,"w+")
    wi=open(imperial_weather_filename,"r")
    for line in wi:
        lst=line.split(",")
        s=""
        if(lst[2]=='High'):
            s=line
        else:
            s=lst[0]+","+lst[1]+","+str(f_to_c(int(lst[2])))+","+str(f_to_c(int(lst[3])))+","+str(in_to_cm(float(lst[4])))+'\n'
        wm.write(s)
    wm.close()
    wi.close()

# Part C
def print_average_temps_per_month(city, weather_filename, unit_type):
    # prints average highs and lows in each month for the given city
    lst_month=['January','February','March','April','May','June','July','August','September','October','November','December']
    f=open(weather_filename,"r")
    print("Average temperatures for ",city,":\n",sep="")
    if(unit_type=='imperial'):
        unit='F'
    if(unit_type=='metric'):
        unit='C'
    high_sums=[0,0,0,0,0,0,0,0,0,0,0,0]
    low_sums=[0,0,0,0,0,0,0,0,0,0,0,0]
    day_nums=[0,0,0,0,0,0,0,0,0,0,0,0]
    for line in f:
        lst=line.split(",")
        if(lst[1]!='Date'):
            date=lst[1].split("/")
            high_sums[int(date[0])-1]+=float(lst[2])
            low_sums[int(date[0])-1]+=float(lst[3])
            day_nums[int(date[0])-1]+=1
    for i in range(12):
        print(lst_month[i],": ",high_sums[i]/day_nums[i],unit," High, ",low_sums[i]/day_nums[i],unit," Low\n",sep="")
    f.close()
    
# Part D
# Write your question (as a comment), and implement a function to answer it
# Q: Given two cities, which has higher average rainfall?
def higher_rainfall(city1,city2,weather_filename):
    f=open(weather_filename,"r")
    rain1=0
    rain2=0
    for line in f:
        lst=line.split(",")
        if(lst[0]==city1):
            rain1+=float(lst[4])
        if(lst[0]==city2):
            rain2+=float(lst[4])
    if(rain1>rain2):
        print(city1)
    if(rain1<rain2):
        print(city2)
    if(rain1==rain2):
        print("The same")
    f.close()
    
def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    higher_rainfall("San Francisco","New York","weather in imperial.csv")
    

    
main()
