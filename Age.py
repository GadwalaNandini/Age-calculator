import datetime                        # datetime consists of year,month,days,hours,min's,sec's

Present_Date = datetime.datetime.now()               # gets the currentDate

DOB= input ('Enter your date of birth   dd mm yyyy : \t')       # your input
print("Your date of Birth is :", DOB)
DOB_Date= datetime.datetime.strptime(DOB,'%d %m %Y')        
 #strptime has two arguments  , 1. string (your input ) ,2. convertedcode (yo string converted to code such as %d %m %y)
# dd - %d , mm - %m , yy - %y stores
print("Your Date of Birth in YY-MM-DD-HH-mm-SS is :",DOB_Date)
Present_Age = Present_Date-DOB_Date       # to get current age
print(Present_Age)                         # gets in days and time

years = ((Present_Age.total_seconds())/(365.242*24*3600))              # converts to seconds and gets year as integer 
# .total_seconds() is a method to convert the years into seconds
yearsInt=int(years)                                                    

months=(years-yearsInt)*12
monthsInt=int(months)


days=(months-monthsInt)*(365.242/12)
daysInt=int(days)

hours = (days-daysInt)*24
hoursInt=int(hours)

minutes = (hours-hoursInt)*60
minutesInt=int(minutes)

seconds = (minutes-minutesInt)*60
secondsInt =int(seconds)

print('You are  \n {0:d} years, \n {1:d}  months, \n {2:d}  days, \n {3:d}  hours, \n {4:d} \
 minutes, \n {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt))
