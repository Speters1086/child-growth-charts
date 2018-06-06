
# Import libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



   
weight_by_age_plot = Plot(df=child_df, data_df=infant_weight_df, y_label='weight [kg]')
weight_by_age_plot.create(number_of_months=3.5)
weight_by_age_plot.save(plot_file_name='Infant_Weight_vs_Age', folder=plots_folder)
