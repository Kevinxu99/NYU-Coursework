n=int(input("Please enter a date of birth: "))
m=int(input("Please enter today's date: "))
ny=n//10000
nm=(n%10000)//100
nd=n%100
my=m//10000
mm=(m%10000)//100
md=m%100
tdn=nd+nm*30+ny*360
tdm=md+mm*30+my*360
days=tdm-tdn
print("you have been alive for ",days//360,"years",(days%360)//30,"months",days%30,"days")
