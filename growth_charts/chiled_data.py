import os
import pandas as pd
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta

from growth_charts import config


class ChildData(object):

    def __init__(self, date_of_birth, gender):

        assert type(date_of_birth) == dt.datetime
        self.date_of_birth = date_of_birth
        self.gender = gender
        if gender == 'male':
            self.gender_id = 1
        else:
            self.gender_id = 2

        self.df = None
        self.wt_by_lt_df = None

        self.read_child_data()

    def read_child_data(self):

        self.df = pd.read_csv(os.path.join(config.DATA_FOLDER, config.CHILD_DATA_FILE),
                              parse_dates=['date'],
                              infer_datetime_format=True)

        self.df['date_of_birth'] = self.date_of_birth

        seconds_in_a_month = 365.25 * 24 * 60 * 60 / 12
        self.df['age'] = ((self.df['date'] -
                           self.df['date_of_birth']) / np.timedelta64(1000000000, 'ns')) / seconds_in_a_month

        self.df.set_index(keys='age', inplace=True)

        self.wt_by_lt_df = self.df[['length', 'weight']].dropna()
        self.wt_by_lt_df.set_index('length', inplace=True)

