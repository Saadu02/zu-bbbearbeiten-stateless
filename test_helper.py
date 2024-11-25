import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)

def test_get_csv():
    # Given: Es gibt Traktanden
    helper.add("Traktandum 1", "2024-11-25")
    helper.add("Traktandum 2", "2024-11-26")

    # When: Die CSV-Funktion aufgerufen wird
    csv_result = helper.get_csv()

    # Then: Die CSV-Daten enthalten die Traktanden im richtigen Format
    assert "Traktandum 1,2024-11-25" in csv_result
    assert "Traktandum 2,2024-11-26" in csv_result


