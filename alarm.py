# Andrew Keller
# 11/26/24

current_time = input('What is the current time using 24 hour clock format? (i.e. 1:33 would be 0133 for A.M. or 1333 for P.M.) ')
while isinstance(current_time, str):
    if current_time.isdigit():
        current_hour = int(current_time[:2])
        current_min = int(current_time[-2:])
        current_time = int(current_time)
    else:
        current_time = input('Inncorrect format. What is the current time using 24 hour clock format? (i.e. 1:33 would be 0133 for A.M. or 1333 for P.M.) ') 
        
alarm_hours = input('How many hours in the future do you want the alarm to go off? (Do not input min, we will enter that shit next.' )
alarm_min = input('How many minutes in addition to the hours would you like for the alarm to go off? ')
while isinstance(alarm_hours, str) or isinstance(alarm_min, str):
    if alarm_hours.isdigit() and alarm_min.isdigit:
        alarm_hours = int(alarm_hours)
        alarm_min  = int(alarm_min)
    else:
        alarm_hours = input('Inncorrect format. How many hours in the future do you want the alarm to go off? (Do not input min, we will enter that shit next.' )
        alarm_min = input('Inncorrect format. How many minutes in addition to the hours would you like for the alarm to go off? ')
    

alarm_off_hours = current_hour + alarm_hours
alarm_off_min = current_min + alarm_min
day = 0

if alarm_off_min > 60:
    alarm_off_hours += 1
    alarm_off_min -= 60
    
if alarm_off_hours > 23:
    day = int(alarm_off_hours / 24)
    alarm_off_hours = alarm_off_hours - (day * 24)
else:
    days = 'today'
if day == 1:
    days = 'tomorrow'
elif day > 1:
    days = str(day) + ' days from now.'
    
if alarm_off_min == 0:
    alarm_off_min = str('00')
elif alarm_off_min < 10:
    alarm_off_min = '0' + str(alarm_off_min)
else:
    alarm_off_min = str(alarm_off_min)

if alarm_off_hours == 0:
    alarm_off_hours = str('00')
elif alarm_off_hours < 10:
    alarm_off_hours = '0' + str(alarm_off_hours)
else:
    alarm_of_hours = str(alarm_off_hours)
    
print(f'Your alarm will go off at {alarm_off_hours}{alarm_off_min} {days}')

