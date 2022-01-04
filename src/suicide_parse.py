
from datetime import datetime

def parse_bool(string):         #Function to change into boolean
    if string == 'female':
        return True
    if string == 'male':
        return False 

def parse_int(string):          #Function to change into int
    return int(string)

def parse_date(string):         #Function to change into date ("%Y")
    return datetime.strptime(string, "%Y").date()

def parse_float(string):          #Function to change into float
    return float(string.replace(',', '.'))