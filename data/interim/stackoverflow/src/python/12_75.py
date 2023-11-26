import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def _plot_pareto_by(df_, group_by, column):

    df = df_.groupby(group_by)[column].sum().reset_index()
    df = df.sort_values(by=column,ascending=False)

    df["cumpercentage"] = df[column].cumsum()/df[column].sum()*100


    fig, ax = plt.subplots(figsize=(20,5))
    ax.bar(df[group_by], df[column], color="C0")
    ax2 = ax.twinx()
    ax2.plot(df[group_by], df["cumpercentage"], color="C1", marker="D", ms=7)
    ax2.yaxis.set_major_formatter(PercentFormatter())

    ax.tick_params(axis="y", colors="C0")
    ax2.tick_params(axis="y", colors="C1")

    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    plt.show()
