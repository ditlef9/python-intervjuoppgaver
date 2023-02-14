#
# File: generate_data.py
# Version 1
# Copyright (c) 2023 S.A. Ditlefsen
# License: https://opensource.org/licenses/GPL-3.0 GNU Public License
#
import datetime
import json
import random

from dateutil.relativedelta import *


def generate_data():
    """
    generates random data to "alarms.json"
    :return:
    """

    # Find current month and year
    now: datetime = datetime.datetime.now()
    data_list: list = []
    for i in range(20):
        # Find date
        now = now + relativedelta(months=-1)
        datetime_year = now.strftime("%Y")
        datetime_month = now.strftime("%m")

        # Generate random alarms
        alarms_count = random.randint(100, 200)
        alarms_high = random.randint(0, alarms_count)
        alarms_medium = random.randint(0, alarms_count - alarms_high)
        alarms_low = random.randint(0, alarms_count - alarms_medium)

        # Add to list
        data_dict = {
            "month": datetime_month,
            "year": datetime_year,
            "alarms_count": alarms_count,
            "categories": {
                "high": alarms_high,
                "medium": alarms_medium,
                "low": alarms_low
            }
        }
        data_list.append(data_dict)

        print(f"generate_data() :: {datetime_year} {datetime_month}", end=" ")
        print(f"alarms_count={alarms_count} (H={alarms_high}, M={alarms_medium}, L={alarms_low})")

    # Write to file
    f = open("data/alarms.json", "w")
    f.write(json.dumps(obj=data_list, indent=4))
    f.close()


if __name__ == '__main__':
    generate_data()
