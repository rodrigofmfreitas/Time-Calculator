def add_time(start, duration, *args):
    start = start.split()
    time_day_start = start[1]
    start = start[0].split(":")

    duration = duration.split(":")
    minutes = int(start[1]) + int(duration[1])
    hours = int(start[0]) + int(duration[0])

    if minutes >= 60:
        hours += int(minutes/60)
        minutes %= 60

    days_passed = int(hours/24)
    hours %= 24

    if hours >= 12 and time_day_start == "PM":
        time_day_start = "AM"
        days_passed += 1
    elif hours >= 12 and time_day_start == "AM":
        time_day_start = "PM"
    if minutes < 10:
        minutes = "0" + str(minutes)
    if hours > 13:
        hours %= 12
    new_time = f"{hours}:{minutes} {time_day_start}"

    if args:
        args = args[0].capitalize()
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if args in days_of_week:
            newday = (days_of_week.index(args) + days_passed) % 7
            newday = days_of_week[newday]
            new_time += f", {newday}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time