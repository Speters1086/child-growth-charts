import pandas as pd
import os


from groth_charts import config


class WhoData(object):

    def __init__(self, child_data):

        self.child_data = child_data
        self.infant_weight_df = None
        self.infant_length_df = None
        self.infant_head_df = None
        self.infant_wt_by_lt_df = None

    def get_data(self):
        # Load WHO data: https://www.cdc.gov/growthcharts/percentile_data_files.htm
        self.infant_weight_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
                                                         'weight_by_age_infant_0_to_36_months.csv'),
                                       index_col='Agemos')
        self.infant_weight_df = self.infant_weight_df.loc[self.infant_weight_df['Sex'] == self.child_data.gender_id]

        self.infant_length_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
                                                         'length_by_age_infant_0_to_36_months.csv'),
                                       index_col='Agemos')
        self.infant_length_df = self.infant_length_df.loc[self.infant_length_df['Sex'] == self.child_data.gender_id]

        self.infant_head_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
                                                       'head_circumference_by_age_infant_0_to_36_months.csv'),
                                          index_col='Agemos')
        self.infant_head_df = self.infant_head_df.loc[self.infant_head_df['Sex'] == self.child_data.gender_id]

        self.infant_wt_by_lt_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
                                                           'weight_by_length_infant_0_to_36_months.csv'),
                                              index_col='Agemos')
        self.infant_wt_by_lt_df = self.infant_wt_by_lt_df.loc[self.infant_wt_by_lt_df['Sex']
                                                              == self.child_data.gender_id]

        # self.weight_by_age_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
        #                                                  'weight_by_age_2_to_20_years.csv'),
        #                                     index_col='Agemos')
        # self.weight_by_age_df = self.weight_by_age_df.loc[self.weight_by_age_df['Sex'] == self.child_data.gender_id]
        #
        # self.bmi_by_age_df = pd.read_csv(os.path.join(config.DATA_FOLDER,
        #                                               'bmi_by_age_2_to_20_years.csv'),
        #                                  index_col='Agemos')
        # self.bmi_by_age_df = self.bmi_by_age_df.loc[self.bmi_by_age_df['Sex'] == self.child_data.gender_id]