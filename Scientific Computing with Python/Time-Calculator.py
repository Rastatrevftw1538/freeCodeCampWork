def TimeChange(timeOfDay):
    if timeOfDay == "PM":
        timeOfDay = "AM"
        return timeOfDay
    if timeOfDay == "AM":
        timeOfDay = "PM"
        return timeOfDay

def add_time(start, duration, startingDay = None):
    daysGoneBy = 0
    daysOfTheWeek = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    timeValueStart = start.split()[0]
    timeOfDay = start.split()[1]
    hours = timeValueStart.split(":")[0]
    minutes = timeValueStart.split(":")[1]
    hoursToAdd = duration.split(":")[0]
    minutesToAdd = duration.split(":")[1]

    hourValue = int(hours)+int(hoursToAdd)
    minuteValue = int(minutes)+int(minutesToAdd)
    if minuteValue > 59:
        minuteValue = minuteValue - 60
        hourValue += 1
    if len(str(minuteValue))<2:
        minuteValue = "0"+str(minuteValue)
    while hourValue >= 12:
        timeOfDay = TimeChange(timeOfDay)
        if timeOfDay == "AM":
            daysGoneBy += int(1)
        if hourValue != 12:
            twelveHourConversion = hourValue - 12
            hourValue = twelveHourConversion
        else:
            hourValue = 12
        break
    new_time = str(hourValue)+":"+str(minuteValue)+" "+timeOfDay
    if startingDay != None:
        weekIndex = daysOfTheWeek.index(startingDay.lower().capitalize())
        newWeekDayIndex = weekIndex+daysGoneBy
        while newWeekDayIndex > len(daysOfTheWeek)-1:
            newWeekDayIndex -= len(daysOfTheWeek)
            weekName = daysOfTheWeek[newWeekDayIndex]
            new_time += ", "+weekName
    if daysGoneBy != 0:
        if daysGoneBy == 1:
            new_time += " (next day)"
        else:
            new_time += " ("+str(int(daysGoneBy))+" "+"days later)"
    return new_time