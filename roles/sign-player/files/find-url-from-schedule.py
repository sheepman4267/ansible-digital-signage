import datetime
import subprocess
import logging

def simple_strptime(time: str):
    """Returns a datetime.time object. Assumes input string is in the form of '%H:%M'."""
    time = time.split(':')
    return datetime.time(int(time[0]), int(time[1]))

current_time = datetime.datetime.now().strftime('%H:%M')
with open('/var/ansible-digital-signage/signage-schedule') as schedule_file:
    now = datetime.datetime.now()
    for line in schedule_file.readlines():
        logging.debug(f'Schedule Line:{line}')
        if line.startswith("#"):
            continue
        schedule_days, schedule_start_time, schedule_end_time, url = line.split("|")
        if now.strftime("%a") in schedule_days.split(",") \
            and datetime.time(now.hour, now.minute) >= simple_strptime(schedule_start_time) \
            and datetime.time(now.hour, now.minute) < simple_strptime(schedule_end_time):
                logging.info(f'Writing {url} to /var/ansible-digital-signage/current and starting Chrome.')
                with open('/var/ansible-digital-signage/current', 'w') as current:
                    current.write(url)
                subprocess.call('systemctl restart signage-chrome.service', shell=True)
                exit(0)
        else:
            logging.info(f'Writing path to placeholder to /var/ansible-digital-signage/current and stopping Chrome.')
            with open('/var/ansible-digital-signage/current', 'w') as current:
                current.write('/opt/ansible-digital-signage/signage-placeholder.html')
            subprocess.call('systemctl stop signage-chrome.service', shell=True)
            subprocess.call('systemctl start signage-display-off.service', shell=True)