import pandas as pd
from scipy.spatial import distance

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

print("index=",find_nearest(df,1080, 1000),"value=",data[find_nearest(df,1080, 1000)])
