
def add_time(start, duration, day_of=''):
    spl = start.split(" ")
    hour = int(spl[0].split(":")[0])
    minute = int(spl[0].split(":")[1])

    hourDuration = int(duration.split(":")[0])
    minuteDuration = int(duration.split(":")[1])

    actual = spl[1]

    tuple = calc_hour(hour, minute, actual, hourDuration, minuteDuration)
    days = tuple[3]
    calc_days_off = calc_day_off(day_of, days)

    if days == 1:
        return f'{tuple[0]}:{tuple[1]} {tuple[2]}{calc_days_off} (next day)'
    elif days > 1:
        return f'{tuple[0]}:{tuple[1]} {tuple[2]}{calc_days_off} ({str(days)} days later)'
    else:
        return f'{tuple[0]}:{tuple[1]} {tuple[2]}{calc_days_off}'


def calc_day_off(day_off, num_days):
    if len(day_off) == 0:
        return ''
    elif num_days == 0:
        return f', {day_off.lower().capitalize()}'

    week = {"monday": 1, "tuesday": 2, "wednesday": 3,
            "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}

    daysAfter = num_days
    num = week.get(day_off.lower())
    newDay = ''

    verNum = (num + daysAfter) % 7

    for key, value in week.items():
         if (num + daysAfter) % 7 == value:
             newDay=key
             break

    if newDay != day_off.lower() and verNum == 0:
        return ", Sunday"
        
    return f', {newDay.capitalize()}'


def calc_days(arr):
    cont=0
    for n in arr:
        if 'AM' in n:
            if n['AM'] == 12:
                cont=cont + 1
    return cont


def calc_hour(hour, minute, actual, hourDuration, minuteDuration):
    contHour=hourDuration
    verifyActualChange=[]

    minute=minute + minuteDuration

    if(minute >= 60):
        minute=minute - 60
        hour=hour + 1
        actual='AM' if hour == 12 and actual == 'PM' else 'PM' if hour == 12 and actual == 'AM' else actual
        hour=1 if hour == 13 else hour
        verifyActualChange.append({actual: hour})

    while contHour > 0:
        hour=hour + 1
        contHour=contHour - 1
        actual='AM' if hour == 12 and actual == 'PM' else 'PM' if hour == 12 and actual == 'AM' else actual
        hour=1 if hour == 13 else hour

        verifyActualChange.append({actual: hour})

    formatedMinute='%0*d' % (2, minute)
    day=calc_days(verifyActualChange)

    return (str(hour), formatedMinute, actual, day)
