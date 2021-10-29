from tkinter import Tk, Canvas
from datetime import date, datetime


def get_events():
    list_events = []
    with open("events.txt") as file:
        for line in file:
            line = line.rstrip("\n")
            current_event = line.split(".")
            # Turn the second item in the list from a string into a date
            event_date = datetime.strptime(current_event[1], "%d/%m/%y").date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events


# Count the days:
def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(" ")
    return number_of_days[0]


root = Tk()  # Create a Tkinter window
c = Canvas(root, width=800, height=800, bg="black")  # create a canvas called c
c.pack()
# add text onto the c canvas. the text starts at x= 100 y= 50.
# The starting coordinate is at the left(west) of the text.
c.create_text(
    100,
    50,
    anchor="w",
    fill="orange",
    font="Arial 28 bold underline",
    text="My Countdown Calendar",
)

events = get_events()
today = date.today()

vertical_space = 100
events.sort(key=lambda x: x[1])
for event in events:
    event_name = event[0]
    day_until = days_between_dates(event[1], today)
    display = "It is %s days until %s" % (day_until, event_name)
    c.create_text(
        100,
        vertical_space,
        anchor="w",
        fill="lightblue",
        font="Arial 28 bold",
        text=display,
    )
    vertical_space = vertical_space + 30
