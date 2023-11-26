def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.tick_params(labelbottom=False, labelleft=False, labelright=False)
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])


df = pd.DataFrame()
df['Animal'] = ['Cow', 'Bear']
df['Weight'] = [250, 450]
df['Favorite'] = ['Grass', 'Honey']
df['Least Favorite'] = ['Meat', 'Leaves']

fig = plt.figure(figsize=(9, 2))


gs = GridSpec(3, 4, figure=fig, wspace=0.0, hspace=0.0,height_ratios=[1, 1, 4])
# plot table header
ax1 = fig.add_subplot(gs[:-1, 0])
ax1.text(0.5, 0.5, df.columns[0], va="center", ha="center")
ax2 = fig.add_subplot(gs[:-1, 1])
ax2.text(0.5, 0.5, df.columns[1], va="center", ha="center")
ax3 = fig.add_subplot(gs[0, -2:])
ax3.text(0.5, 0.5, "Food", va="center", ha="center")
ax4 = fig.add_subplot(gs[1, -2])
ax4.text(0.5, 0.5, df.columns[2], va="center", ha="center")
ax5 = fig.add_subplot(gs[1, -1])
ax5.text(0.5, 0.5, df.columns[3], va="center", ha="center")
# plot table data
ax6 = fig.add_subplot(gs[-1, :])
table = ax6.table(cellText=df.values, cellLoc='center', bbox=[0, 0, 1, 1])

format_axes(fig)

plt.show()
