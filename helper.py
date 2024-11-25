from dataclasses import dataclass
import datetime
import  csv
import io

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


def get_csv(data):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["title", "category", "description"])
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()