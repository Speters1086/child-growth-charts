import datetime as dt

from growth_charts import config
from growth_charts.chiled_data import ChildData
from growth_charts.who_data import WhoData
from growth_charts.plots import Plot

date_of_birth = dt.datetime(2018, 5, 31)
gender = 'male'

child_data = ChildData(date_of_birth=date_of_birth, gender=gender)

who_data = WhoData(child_data=child_data)

for who_dict_key in who_data.who_infant_df_dict.keys():
    for who_df_key in who_data.who_infant_df_dict[who_dict_key].keys():
        if who_df_key == 'infant_weight_by_length':
            child_data_df = child_data.wt_by_lt_df
            x_limit = 80.5
            x_tick_interval = 3
        else:
            child_data_df = child_data.df
            x_limit = 12.5
            x_tick_interval = 1
        plot_name = who_df_key
        plot = Plot(df=child_data_df,
                    df_column=who_dict_key,
                    who_data_df=who_data.who_infant_df_dict[who_dict_key][who_df_key])
        plot.create(title=who_df_key.replace('_', ' ').title(), x_limit=x_limit, x_tick_interval=x_tick_interval)
        plot.save(plot_file_name=plot_name, folder=config.PLOTS_FOLDER)
