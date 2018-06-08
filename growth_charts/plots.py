import os
import numpy as np
import matplotlib.pyplot as plt


class Plot(object):

    def __init__(self, df, df_column, who_data_df):
        self.child_df = df
        self.child_df_column = df_column
        self.data_df = who_data_df

        self.fig = plt.figure(figsize=(8, 8))

        self.y_labels_dict = {'weight': 'weight [kg]',
                              'length': 'length [cm]',
                              'head_circumference': 'head_circumference [cm]'}
        self.x_labels_dict = {'age': 'age [months]',
                              'length': 'length [cm]'}

    def create(self, x_limit, x_tick_interval):
        # Plot style
        plt.xkcd()

        # add axis
        ax = self.fig.add_subplot(111)

        # line setups
        columns = ['P3', 'P10', 'P25', 'P50', 'P75', 'P90', 'P97']
        line_style = ['k:', 'k--', 'k:', 'k', 'k:', 'k--', 'k:']
        line_weight = [1, 2, 1, 3, 1, 2, 1]

        # Age vs weight
        max_y, min_y = None, None
        for col, style, lw in zip(columns, line_style, line_weight):
            self.data_df[col].plot(ax=ax, style=style, lw=lw)
            plt.text(x=x_limit,
                     y=self.data_df[col][x_limit] - 0.1,
                     s=col,
                     size=10)
            if max_y is None or max_y < self.data_df[col][x_limit]:
                max_y = self.data_df[col][x_limit]
            if min_y is None or min_y > self.data_df[col][x_limit]:
                min_y = self.data_df[col][self.data_df.index.min()]

        self.child_df[self.child_df_column].plot(ax=ax, style='--bo', lw=2)

        plt.grid(True)
        plt.xlabel(self.x_labels_dict[self.child_df.index.name])
        plt.ylabel(self.y_labels_dict[self.child_df_column])
        plt.ylim([min_y - 1, max_y + 1])
        plt.xlim([self.data_df.index.min(), x_limit])
        plt.xticks(np.arange(self.data_df.index.min(), x_limit, x_tick_interval))

    def save(self, plot_file_name, folder):
        self.fig.savefig(os.path.join(folder, plot_file_name + '.png'))