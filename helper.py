from dataclasses import dataclass
import datetime
import csv
from io import StringIO

items = []


@dataclass
class Item:
    text: str
    date: datetime.date 
    isCompleted: bool = False


def add(text, date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text, date))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted


def get_csv():
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Text", "Date", "Completed"])  # Header

    for item in items:
        writer.writerow([item.text, item.date, item.isCompleted])

    return output.getvalue()