import os
import pandas as pd
import numpy as np
import datetime as dt
from dateutil import relativedelta

from groth_charts import config


class ChildData(object):

    def __index__(self, birth_date, gender):

        assert type(birth_date) == dt.date
        self.birth_date = birth_date
        self.gender = gender
        if gender == 'male':
            self.gender_id = 1
        else:
            self.gender_id = 2

    def read_child_data(self):

        self.child_df = pd.read_csv(os.path.join(config.DATA_FOLDER, config.CHILD_DATA_FILE),
                                    parse_dates=True,
                                    infer_datetime_format=True,
                                    dayfirst=True)
        self.child_df['age_months'] = np.vectorize(self.number_of_months)(self.child_df['date'], self.birth_date)

        self.child_df.set_index(keys='age_months', drop=True, inplace=True)

    @staticmethod
    def number_of_months(date_1, date_2):

        return relativedelta.relativedelta(date_2, date_1).months








if gender == 'male':
    gender_id = 1
else:
    gender_id = 2