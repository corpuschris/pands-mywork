#This program gets what day of the week it is;

#Author: Christiano Ferreira


day_input = input("Enter a day of the week: ")
day_input = day_input.capitalize()

weekday_names = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}


if day_input in weekday_names.values():
    if day_input in ["Saturday", "Sunday"]:
        print("It is the weekend, yay!:D")
    else:
        print("Yes, unfortunately it is a weekday. :(")
else:
    print("It seems like", day_input, "is not a valid day of the week.")