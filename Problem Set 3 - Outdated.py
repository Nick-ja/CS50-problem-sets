month_list = [
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

while True:
    date_input = input("Date: ")
    try:
        if "/" in date_input:
            slash_date = date_input.split("/")
            print(slash_date)
    except:
        print(slash_date)
    # normal_date = date_input.split(" ")
    # print(normal_date)
    #except:
    #    for i in date_input:
    #        if i in month_list:
    #            slash_date = date_input.split(",")
    # else:
    #     m = int(slash_date[0])
    #     d = int(slash_date[1])
    #     y = int(slash_date[2])
    #     print(f"{y}-{m:02}-{d:02}")
