def plot(col):
 
    fig, ax = plt.subplots()
    ax.plot(col)
    plt.show()

df.apply(plot)
