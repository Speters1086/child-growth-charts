import os
import pandas as pd
import numpy as np
import datetime as dt

from growth_charts import config


class ChildData(object):

    def __init__(self, child_name: str, date_of_birth: dt.datetime, gender: str):

        self.child_name = child_name
        assert type(date_of_birth) == dt.datetime
        self.date_of_birth = date_of_birth
        self.gender = gender
        if gender == 'male':
            self.gender_id = 1
        else:
            self.gender_id = 2

        self.df = None
        self.df_days = None
        self.wt_by_lt_df = None

        self._read_child_data()

    def _read_child_data(self):

        self.df = pd.read_csv(os.path.join(config.CHILD_DATA_FOLDER,self.child_name, 'data.csv'),
                              parse_dates=['date'],
                              infer_datetime_format=True)

        self.df['date_of_birth'] = self.date_of_birth

        self.df['age'] = (self.df['date'] - self.df['date_of_birth']) / np.timedelta64(1, 'M')
        self.df['age_days'] = (self.df['date'] - self.df['date_of_birth']) / np.timedelta64(1, 'D')

        self.df.set_index(keys='age', inplace=True)
        self.df_days = self.df.set_index(keys='age_days')

        self.wt_by_lt_df = self.df[['length', 'weight']].dropna()
        self.wt_by_lt_df.set_index('length', inplace=True)

