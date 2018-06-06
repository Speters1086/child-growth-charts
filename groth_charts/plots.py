import os
import numpy as np
import matplotlib.pyplot as plt


class Plot(object):

    def __init__(self, df, data_df, y_label):
        self.child_df = df
        self.data_df = data_df
        self.y_label = y_label

        self.fig = plt.figure(figsize=(8, 8))

    def create(self, number_of_months):
        # Plot style
        plt.xkcd()

        # add axis
        ax = self.fig.add_subplot(111)

        # line setups
        columns = ['P3', 'P10', 'P25', 'P50', 'P75', 'P90', 'P97']
        line_style = ['k:', 'k--', 'k:', 'k', 'k:', 'k--', 'k:']
        line_weight = [1, 2, 1, 3, 1, 2, 1]

        # Age vs weight
        max_y = None
        for col, style, lw in zip(columns, line_style, line_weight):
            self.data_df[col].plot(ax=ax, style=style, lw=lw)
            plt.text(x=number_of_months,
                     y=self.data_df[col][number_of_months] - 0.1,
                     s=col,
                     )
            if max_y is None or max_y < self.data_df[col][number_of_months]:
                max_y = self.data_df[col][number_of_months]

        child_df['Weight'].plot(ax=ax, style='--bo', lw=2)

        plt.grid(True)
        plt.xlabel('age [months]')
        plt.ylabel(self.y_label)
        plt.ylim([0, max_y + 1])
        plt.xlim([0, number_of_months])
        plt.xticks(np.arange(0, number_of_months, 0.5))

    def save(self, plot_file_name, folder):
        self.fig.savefig(os.path.join(folder, plot_file_name + '.png'))