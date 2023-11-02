
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
While True:
    try:
    # get input from user
    a = input("Date: ").strip()

    # if the input contains spaces
    if " " in a:
        if "," in a:
            month , day ,year = a.split(" ")
            # find the month title in list
            if month.title() in months:
                # delete the ',' after day number
                day = int(day.strip(","))
                # month index + 1 because list starts from 0
                month = int(months.index(month)) + 1
                if month <= 12 and day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                
