from datetime import datetime
from pprint import pprint


def convert12hour(time24:str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')
