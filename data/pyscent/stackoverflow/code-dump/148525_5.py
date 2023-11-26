import numpy as np
import pandas as pd
from scipy.spatial import distance
import timeit

data = [(989, 998), (1074, 999), (1159, 1000), (1244, 1001), (1329, 1002),
        (970, 1042), (1057, 1043), (1143, 1044), (1230, 1045), (1316, 1046),
        (951, 1088), (1039, 1089), (1127, 1090), (1214, 1091), (1302, 1092),
        (930, 1137), (1020, 1138), (1109, 1139), (1198, 1140), (1287, 1141),
        (909, 1188), (1000, 1189), (1091, 1190), (1181, 1191), (1271, 1192)]
df = pd.DataFrame(data)
df.columns = ['x', 'y']
def find_nearest( df, x, y):
    min_distance = float('inf')
    index_of_closest = -1
    for index, pos in enumerate(df.values):
        x_coord, y_coord = pos
        current_distance = distance.euclidean((x, y), (x_coord, y_coord))
        if current_distance < min_distance and current_distance != 0 :
            min_distance = current_distance
            index_of_nearest= index
    return index_of_nearest
starttime = timeit.default_timer()
print(data[find_nearest(df,1080, 1000)])
print("The time difference 1 is :", timeit.default_timer() - starttime)
#or
starttime = timeit.default_timer()
df.iloc[-1]=[1080, 1000]
z = np.array([[complex(c[0], c[1]) for c in df.values]])
Distance = abs(z.T - z)
masked_a = np.ma.masked_equal(Distance, 0.0, copy=False)
print(df.iloc[np.argmin(masked_a[:, len(masked_a)-1])])
print("The time difference 2 is :", timeit.default_timer() - starttime)

data = [[(989, 998), (1074, 999), (1159, 1000), (1244, 1001), (1329, 1002)],
        [(970, 1042), (1057, 1043), (1143, 1044), (1230, 1045), (1316, 1046)],
        [(951, 1088), (1039, 1089), (1127, 1090), (1214, 1091), (1302, 1092)],
        [(930, 1137), (1020, 1138), (1109, 1139), (1198, 1140), (1287, 1141)],
        [(909, 1188), (1000, 1189), (1091, 1190), (1181, 1191), (1271, 1192)]]
df = pd.DataFrame(data)
starttime = timeit.default_timer()
l = (1080, 1000)
out = min(df.to_numpy().flatten(), key=lambda c: (c[0]- l[0])**2 + (c[1]-l[1])**2)
print(out)
print("The time difference for method 3 is :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
dist = df.stack().apply(lambda c: (c[0]- l[0])**2 + (c[1]-l[1])**2)
idx = dist.index[dist.argmin()]
val = df.loc[idx]

print(idx)
print(val)
print("The time difference for method 4 is :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
arr = df.to_numpy().astype([('x', int), ('y', int)])
dist = (arr['x'] - l[0])**2 + (arr['y'] - l[1])**2
idx = tuple(np.argwhere(dist == np.min(dist))[0])
val = arr[idx]  # or df.loc[idx]
print(val)
print("The time difference for method 5 is :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
I = (1080, 1000)

s1 = df.stack()
s = pd.DataFrame(s1.to_list(), index=s1.index).sub(I).pow(2).sum(axis=1)
out = s[s.idxmin()]
print (out)
(1074, 999)

print(s.idxmin())
(0, '1')
print("The time difference for method 6 is :", timeit.default_timer() - starttime)
