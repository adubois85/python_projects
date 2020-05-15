from datetime import datetime
from pprint import pprint


def convert12hour(time24:str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('schedule.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint(flights)
print()

flights2 = {}

for k, v in flights.items():
    flights2[convert12hour(k)] = v.title()

pprint(flights2)
