import pandas as pd
import os

from growth_charts import config
from growth_charts.chiled_data import ChildData


class GrowthData(object):

    def __init__(self, child_data: ChildData, source: str):

        self.child_data = child_data
        self.gender_id = child_data.gender_id
        self.growth_chart_df_list = None
        self.source = source
        if source == 'who':
            self.get_who_data()
        else:
            self.get_cdc_data()

    def get_who_data(self):

        if self.gender_id == 1:
            gender = 'boys'
        else:
            gender = 'girls'

        weight_df = pd.read_csv(os.path.join(config.WHO_DATA_FOLDER,
                                             f'who_weight_for_age_{gender}.csv'),
                                index_col='Age')
        length_df = pd.read_csv(os.path.join(config.WHO_DATA_FOLDER,
                                             f'who_length_for_age_{gender}.csv'),
                                index_col='Day')
        head_df = pd.read_csv(os.path.join(config.WHO_DATA_FOLDER,
                                           f'who_head_circumference_for_age_{gender}.csv'),
                              index_col='Age')
        wt_by_lt_df = pd.read_csv(os.path.join(config.WHO_DATA_FOLDER,
                                               f'who_weight_for_length_{gender}.csv'),
                                  index_col='Length')

        self.growth_chart_df_list = [dict(name='weight_by_age', df=weight_df, index='day', column='weight'),
                                     dict(name='weight_by_length', df=wt_by_lt_df, index='length', column='weight'),
                                     dict(name='head_circumference_by_age', df=head_df,
                                          index='day', column='head_circumference'),
                                     dict(name='length_by_age', df=length_df, index='day', column='length')]

    def get_cdc_data(self):

        # Load WHO growth_data_source: https://www.cdc.gov/growthcharts/percentile_data_files.htm
        weight_df = pd.read_csv(os.path.join(config.CDC_DATA_FOLDER,
                                             'weight_by_age_infant_0_to_36_months.csv'),
                                index_col='Agemos')
        weight_df = weight_df.loc[weight_df['Sex'] == self.gender_id]

        length_df = pd.read_csv(os.path.join(config.CDC_DATA_FOLDER,
                                             'length_by_age_infant_0_to_36_months.csv'),
                                index_col='Agemos')
        length_df = length_df.loc[length_df['Sex'] == self.gender_id]

        head_df = pd.read_csv(os.path.join(config.CDC_DATA_FOLDER,
                                           'head_circumference_by_age_infant_0_to_36_months.csv'),
                              index_col='Agemos')
        head_df = head_df.loc[head_df['Sex'] == self.gender_id]

        wt_by_lt_df = pd.read_csv(os.path.join(config.CDC_DATA_FOLDER,
                                               'weight_by_length_infant_0_to_36_months.csv'),
                                  index_col='Length')
        wt_by_lt_df = wt_by_lt_df.loc[wt_by_lt_df['Sex'] == self.gender_id]

        self.growth_chart_df_list = [dict(name='weight_by_age', df=weight_df, index='month', column='weight'),
                                     dict(name='weight_by_length', df=wt_by_lt_df, index='length', column='weight'),
                                     dict(name='head_circumference_by_age', df=head_df,
                                          index='month', column='head_circumference'),
                                     dict(name='length_by_age', df=length_df, index='month', column='length')]
