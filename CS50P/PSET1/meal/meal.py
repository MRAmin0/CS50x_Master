def main():
    sch =
    [
         {"meal" : "breakfast time" , "start hour" : 7, "end hour" :8}
         {"meal" : "lunch time" , "start hour" : 12, "end hour" :13}
         {"meal" : "dinner time" , "start hour" : 18, "end hour" :19}
    ]
    time = input("what time is it? ")
    time = float(convert(time))
    for d in sch
        if time >= float(d["start hour"]) and time <= float(d["end hour"]):
            print(d["meal"])
        else
            continue

def convert(time):
    h, m = time.strip().split(":")


if __name__ == "__main__":
    main()
