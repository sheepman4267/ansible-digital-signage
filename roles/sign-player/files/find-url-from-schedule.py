import datetime

def simple_strptime(time: str):
    """Returns a datetime.time object. Assumes input string is in the form of '%H:%M'."""
    time = time.split(':')
    return datetime.time(int(time[0]), int(time[1]))

current_time = datetime.datetime.now().strftime('%H:%M')
with open("/var/ansible-digital-signage/signage-schedule") as schedule_file:
    now = datetime.datetime.now()
    for line in schedule_file.readlines():
        if line.startswith("#"):
            continue
        schedule_days, schedule_start_time, schedule_end_time, url = line.split("|")
        if now.strftime("%a") in schedule_days.split(",") \
            and datetime.time(now.hour, now.minute) > simple_strptime(schedule_start_time) \
            and datetime.time(now.hour, now.minute) < simple_strptime(schedule_end_time):
                print(url)
        else:
            print("/opt/ansible-digital-signage/signage-placeholder.html")
