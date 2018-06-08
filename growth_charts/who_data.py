import pandas as pd
import os
import numpy as np

from growth_charts import config


class WhoData(object):

    def __init__(self, child_data):

        self.child_data = child_data
        self.who_infant_df_dict = None
        self.get_data()

    def get_data(self):

        # Load WHO data: https://www.cdc.gov/growthcharts/percentile_data_files.htm
        infant_weight_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
                                                    'weight_by_age_infant_0_to_36_months.csv'),
                                       index_col='Agemos')
        infant_weight_df = infant_weight_df.loc[infant_weight_df['Sex'] == self.child_data.gender_id]

        infant_length_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
                                                    'length_by_age_infant_0_to_36_months.csv'),
                                       index_col='Agemos')
        infant_length_df = infant_length_df.loc[infant_length_df['Sex'] == self.child_data.gender_id]

        infant_head_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
                                                  'head_circumference_by_age_infant_0_to_36_months.csv'),
                                     index_col='Agemos')
        infant_head_df = infant_head_df.loc[infant_head_df['Sex'] == self.child_data.gender_id]

        infant_wt_by_lt_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
                                                      'weight_by_length_infant_0_to_36_months.csv'),
                                         index_col='Length')
        infant_wt_by_lt_df = infant_wt_by_lt_df.loc[infant_wt_by_lt_df['Sex'] == self.child_data.gender_id]

        self.who_infant_df_dict = {'weight': {'infant_weight_by_age': infant_weight_df,
                                              'infant_weight_by_length': infant_wt_by_lt_df},
                                   'head_circumference': {'infant_head_circumference_by_age': infant_head_df},
                                   'length': {'infant_length_by_age': infant_length_df}}
