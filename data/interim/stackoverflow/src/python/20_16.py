import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def mergecells(table, cells):
    '''
    Merge N matplotlib.Table cells

    Parameters
    -----------
    table: matplotlib.Table
        the table
    cells: list[set]
        list of sets od the table coordinates
        - example: [(0,1), (0,0), (0,2)]

    Notes
    ------
    https://stackoverflow.com/a/53819765/12684122
    '''
    cells_array = [np.asarray(c) for c in cells]
    h = np.array([cells_array[i+1][0] - cells_array[i][0] for i in range(len(cells_array) - 1)])
    v = np.array([cells_array[i+1][1] - cells_array[i][1] for i in range(len(cells_array) - 1)])

    # if it's a horizontal merge, all values for `h` are 0
    if not np.any(h):
        # sort by horizontal coord
        cells = np.array(sorted(list(cells), key=lambda v: v[1]))
        edges = ['BTL'] + ['BT' for i in range(len(cells) - 2)] + ['BTR']
    elif not np.any(v):
        cells = np.array(sorted(list(cells), key=lambda h: h[0]))
        edges = ['TRL'] + ['RL' for i in range(len(cells) - 2)] + ['BRL']
    else:
        raise ValueError("Only horizontal and vertical merges allowed")

    for cell, e in zip(cells, edges):
        table[cell[0], cell[1]].visible_edges = e
        
    txts = [table[cell[0], cell[1]].get_text() for cell in cells]
    tpos = [np.array(t.get_position()) for t in txts]

    # transpose the text of the left cell
    trans = (tpos[-1] - tpos[0])/2
    # didn't had to check for ha because I only want ha='center'
    txts[0].set_transform(mpl.transforms.Affine2D().translate(*trans))
    for txt in txts[1:]:
        txt.set_visible(False)


contents = (
    ("Apple", "Banana", "Strawberry", "Melon"),
    ("Apple", "Banana", "Strawberry", "Melon"),
    ("Apple", "Banana", "Strawberry", "Melon")
)
bg_colors = (
    ("r", "y", "r", "g"),
    ("r", "y", "r", "g"),
    ("r", "y", "r", "g")
)



# ///////////////////////////////////////////////////////
# Figure 1: Just merging cells resulting in weired color
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.axis("off")
ax1.set_title("Figure 1")
table = ax1.table(cellText=contents, bbox=[0, 0, 1, 1], cellLoc="center", cellColours=bg_colors)
mergecells(table, [(0, 1), (1, 1), (2, 1)])
# ///////////////////////////////////////////////////////



# ///////////////////////////////////////////////////////
# Figure 2: Overlap empty table only for cells color
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.axis("off")
ax2.set_title("Figure 2")
# 'table_bg' is a background table without any contents
# Set background color of this as you want
table_bg = ax2.table(bbox=[0, 0, 1, 1], cellColours=bg_colors)
for cell in table_bg._cells.values():
    cell.set_edgecolor("none")
# 'table' contatins cell texts
# Sset its color to 'none' then merge
bg_none = (
    ("none", "none", "none", "none"),
    ("none", "none", "none", "none"),
    ("none", "none", "none", "none")
)
table = ax2.table(cellText=contents, bbox=[0, 0, 1, 1], cellLoc="center", cellColours=bg_none)
mergecells(table, [(0, 1), (1, 1), (2, 1)])
# ///////////////////////////////////////////////////////


plt.show()
