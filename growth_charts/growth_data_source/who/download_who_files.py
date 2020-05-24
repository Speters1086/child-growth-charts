import pandas as pd
import os

from growth_charts.config import WHO_DATA_FOLDER


genders = ['girls', 'boys']


who_charts = [
    ('who_length_for_age', 'https://www.who.int/childgrowth/standards/lhfa_$gender$_p_exp.txt'),
    ('who_weight_for_age', 'https://www.who.int/childgrowth/standards/wfa_$gender$_p_exp.txt'),
    ('who_weight_for_length', 'https://www.who.int/childgrowth/standards/wfl_$gender$_p_exp.txt'),
    ('who_bmi_for_length', 'https://www.who.int/childgrowth/standards/bfa_$gender$_p_exp.txt'),
    ('who_head_circumference_for_age', 'https://www.who.int/childgrowth/standards/second_set/hcfa_$gender$_p_exp.txt')
    ]

for who_chart in who_charts:
    who_chart_df = pd.DataFrame()
    for gender in genders:
        who_chart_name = who_chart[0] + f'_{gender}'
        who_chart_url = who_chart[1].replace('$gender$', gender)
        who_chart_df = pd.read_csv(who_chart_url, sep='\t')
        who_chart_df['gender'] = gender
        who_chart_df.to_csv(who_chart_name + '.csv')
