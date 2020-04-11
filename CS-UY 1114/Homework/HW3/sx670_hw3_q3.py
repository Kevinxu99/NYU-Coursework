d=input("Enter the day the call started at:")
t=int(input("Enter the time the call started at (hhmm):"))
dur=int(input("Enter the duration of the call (in minutes):"))
if(d=='Sat' or d=='Sun'):
    print("This call will cost $",0.15*dur)
elif((t//100)>=8 and (t//100)<=18):
    print("This call will cost $",dur*0.4)
else:
    print("This call will cost $",dur*0.25)
