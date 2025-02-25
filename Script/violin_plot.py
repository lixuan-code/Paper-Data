import pandas as pd
import matplotlib.pyplot as plt

from superviolin import test_plot,plot
from superviolin.plot import Superviolin

plt.rcParams["axes.spines.right"] = True
plt.rcParams["axes.spines.top"] = True


violin_data_dry = pd.read_excel("Data/violin_data.xlsx",sheet_name="dry")
violin_data_paddy = pd.read_excel("Data/violin_data.xlsx",sheet_name="paddy")

for var,violin_data_dry_df in violin_data_dry.groupby("vars"):
    violin = Superviolin(dataframe=violin_data_dry_df,
                         condition="class",value="values",replicate="model",
                         middle_vals="median",centre_val="median",
                         cmap="Paired",linewidth=0.7,dpi=600)
    violin.generate_plot()


for var,violin_data_paddy_df in violin_data_paddy.groupby("vars"):
    violin = Superviolin(dataframe=violin_data_paddy_df,
                         condition="class",value="values",replicate="model",
                         middle_vals="median",centre_val="median",
                         cmap="Paired",linewidth=0.7,dpi=600)
    violin.generate_plot()