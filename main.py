from datetime import datetime

import arrow
from ics import Calendar

now = datetime.now()
current_time = now.strftime("%H:%M")

SCHEDULES = [
    "7 Period Day",
    "3 Period Block",
    "4 Period Block",
    "Mass Schedule",
    "Assembly Schedule",
]

def get_today_schedule():
    today = arrow.now().to("utc").floor("day")

    with open("CalExport.ics", "r") as f:
        file = f.read()

    c = Calendar(file)
    for event in c.events:
        for schedule in SCHEDULES:
            if schedule not in event.name:
                continue

            if event.begin.floor("day") == today:
                return event.name

    return "No School"


def main():
    print(get_today_schedule())


if __name__ == "__main__":
    main()

for schedule in SCHEDULES:
    if schedule == "3 Period Block":
        if current_time == "10:53":
            