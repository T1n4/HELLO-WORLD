def main():
    import datetime, calendar
    from datetime import date, time, datetime
    today = date.today()
    print(date.today())
    print(today.day)
    print(today.month)
    print(today.year)
    
    #print which day:
    print(today.weekday())
    
    todays = datetime.now()
    print(datetime.time(datetime.now()))
    print(todays)

    hc = calendar.HTMLCalendar(calendar.SUNDAY)
    st = hc.formatmonth(2024,1)
    c = calendar.TextCalendar(calendar.SUNDAY)
    t = c.formatmonth(2024)
    file1 = open("new.txt", 'w+')
    file1.write(st)
    print(st+t)

    



if __name__ == "__main__":
    main()
