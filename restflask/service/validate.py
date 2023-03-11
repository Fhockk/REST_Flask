"""Helping functions to validate data"""
from datetime import datetime


def date_format(date_to_convert):
    """
    Converts a date string in ISO format ('YYYY-MM-DDTHH:MM:SS') to 'YYYY-MM-DD' format.

    :param date_to_convert:
        date_to_convert (str): A string representing a date in ISO format.

    :return:
        str: A string representing the same date in 'YYYY-MM-DD' format.
    """
    format_date = datetime.strptime(date_to_convert, '%Y-%m-%dT%H:%M:%S')
    format_date = format_date.strftime("%Y-%m-%d")
    return format_date
