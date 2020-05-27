import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Plot(object):

    def __init__(self, child_data_df: pd.DataFrame, growth_chart: list, source: int):
        self.child_df = child_data_df

        self.child_df_column = growth_chart['column']

        if len(self.child_df[self.child_df_column]) == 0:
            self.no_child_data = True
        else:
            self.no_child_data = False

            self.growth_chart_df = growth_chart['df']

            if source == 'cdc':
                self.x_limit = round(max(self.child_df.index) * 2) / 2 + 1
            else:
                self.x_limit = int(max(self.child_df.index)) + 1

            self.fig = plt.figure(figsize=(8, 8))

            self.y_labels_dict = {'weight': 'weight [kg]',
                                  'length': 'length [cm]',
                                  'head_circumference': 'head_circumference [cm]'}
            self.x_labels_dict = {'age': 'age [months]',
                                  'age_days': 'age [days]',
                                  'length': 'length [cm]'}

    def create(self, chart_name):
        title = chart_name.replace('_', ' ').title()
        # Plot style
        # plt.xkcd()

        # add axis
        ax = self.fig.add_subplot(111)

        # line setups
        columns = ['P3', 'P10', 'P25', 'P50', 'P75', 'P90', 'P97']
        line_style = ['k:', 'k--', 'k:', 'k', 'k:', 'k--', 'k:']
        line_weight = [1, 2, 1, 3, 1, 2, 1]

        if self.x_limit > max(self.growth_chart_df.index):
            self.x_limit = max(self.growth_chart_df.index)
        else:
            pass

        # Age vs weight
        max_y, min_y = None, None
        for col, style, lw in zip(columns, line_style, line_weight):
            self.growth_chart_df[col].plot(ax=ax, style=style, lw=lw)
            plt.text(x=self.x_limit,
                     y=self.growth_chart_df[col][self.x_limit] - 0.1,
                     s=col,
                     size=10)
            if max_y is None or max_y < self.growth_chart_df[col][self.x_limit]:
                max_y = self.growth_chart_df[col][self.x_limit]
            if min_y is None or min_y > self.growth_chart_df[col][self.x_limit]:
                min_y = self.growth_chart_df[col][self.growth_chart_df.index.min()]

        self.child_df[self.child_df_column].plot(ax=ax, style='--bo', lw=2)

        plt.grid(True)
        plt.title(title)
        plt.xlabel(self.x_labels_dict[self.child_df.index.name].replace('_', ' '))
        plt.ylabel(self.y_labels_dict[self.child_df_column].replace('_', ' '))
        plt.ylim([min_y - 1, max_y + 1])
        plt.xlim([self.growth_chart_df.index.min(), self.x_limit])
        # plt.xticks(np.arange(self.data_df.index.min(), x_limit, x_tick_interval))

    def save(self, plot_file_name, folder):
        self.fig.savefig(os.path.join(folder, plot_file_name + '.png'))