import datetime as dt

from growth_charts import config
from growth_charts.chiled_data import ChildData
from growth_charts.growth_data import GrowthData
from growth_charts.plots import Plot

children = [dict(name='zachary', date_of_birth=dt.datetime(2018, 5, 31), gender='male'),
            dict(name='abigail', date_of_birth=dt.datetime(2020, 5, 21), gender='female')]

for child in children:

    child_data = ChildData(child_name=child['name'], date_of_birth=child['date_of_birth'], gender=child['gender'])

    growth_data = GrowthData(child_data=child_data, source='who')

    for growth_chart in growth_data.growth_chart_df_list:

        plot_name = child['name'] + '_' + growth_chart['name']

        if growth_chart['name'] == 'weight_by_length':
            child_data_df = child_data.wt_by_lt_df
        elif growth_chart['index'] == 'day':
            child_data_df = child_data.df_days
        else:
            child_data_df = child_data.df

        plot = Plot(child_data_df=child_data_df, growth_chart=growth_chart, source=growth_data.source)
        if plot.no_child_data:
            continue
        else:
            plot.create(chart_name=plot_name)
            plot.save(plot_file_name=plot_name, folder=config.PLOTS_FOLDER)