import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")

def hide_current_axis(*args, **kwds):
    plt.gca().set_visible(False)

g = sns.pairplot(iris, hue="species", palette="husl")
g.map_upper(hide_current_axis)
g.map_lower(hide_current_axis)
