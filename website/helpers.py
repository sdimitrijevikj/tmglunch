import os
import xlrd
import unicodedata

from datetime import datetime, timedelta

from tmglunch.settings import BASE_DIR
from website.models import FoodItem


def create_week_days(from_date):
    """
    Create the correct datetime objects
    """

    days = []
    start_date = datetime.strptime(from_date, '%Y-%m-%d')

    for x in range(0, 5):
        days.append(start_date + timedelta(days=x))

    return days


def handle_price_value(price):
    """
    Price values are a mess... so we need to check and clean them up a bit
    """

    price_obj = {}

    if type(price) is unicode:
        cell_clean = unicodedata.normalize('NFKD', price).encode('ascii', 'ignore').split()
        try:
            price_obj['small_price'] = float(cell_clean[0].replace(',', '.'))
        except:
            price_obj['small_price'] = 0

        try:
            price_obj['large_price'] = float(cell_clean[1].replace(',', '.'))
        except:
            price_obj['large_price'] = 0

    elif type(price) is str:
        cell_clean = price.split()
        try:
            price_obj['small_price'] = float(cell_clean[0].replace(',', '.'))
        except:
            price_obj['small_price'] = 0

        try:
            price_obj['large_price'] = float(cell_clean[1].replace(',', '.'))
        except:
            price_obj['large_price'] = 0

    else:
        price_obj['small_price'] = price
        price_obj['large_price'] = 0

    return price_obj


def normalize_unicode(data):
    """
    Normalize unicode data
    """

    if type(data) is unicode:
        return unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')
    else:
        return data


def parse_lunch_menu_data(file_path, from_date):
    """
    Parse the excel sheet and save the data to the database
    """

    days = create_week_days(from_date)

    # remove previous items if there were any
    start_date = datetime.strptime(from_date, '%Y-%m-%d')
    FoodItem.objects.filter(date__range=[start_date, start_date + timedelta(days=5)]).delete()

    workbook = xlrd.open_workbook(os.path.join(BASE_DIR, file_path))
    worksheet = workbook.sheet_by_name('week')
    rows = worksheet.nrows
    current_row = 3

    while current_row < rows:
        row = worksheet.row(current_row)
        current_row += 1
        food_obj = {}
        week_counter = 0

        for index, cell in enumerate(row):

            if index == 0:
                food_obj['type'] = normalize_unicode(cell.value)

                # Skip this row since it is probably empty
                if food_obj['type'] == '':
                    break

            elif index % 2 != 0 and index != 0:
                food_obj['name'] = normalize_unicode(cell.value)
            elif index % 2 == 0:

                price_clean = handle_price_value(cell.value)
                if food_obj['name'] != '':
                    food_item = FoodItem(date=days[week_counter], type=food_obj['type'], name=food_obj['name'],
                                         small_price=price_clean['small_price'], large_price=price_clean['large_price'],
                                         votes=0)
                    food_item.save()
                week_counter += 1

