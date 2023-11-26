class OctreeNode:
    def __init__(self, points, limit=10):
        self.children = []
        
        if len(points) > limit:
            # calculate the center point of the current node
            center = points.mean(axis=0)

            # for each of the eight octants
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        # select points in the octant
                        in_octant = points[
                            ((points[:, 0] <= center[0]) if i else (points[:, 0] > center[0])) &
                            ((points[:, 1] <= center[1]) if j else (points[:, 1] > center[1])) &
                            ((points[:, 2] <= center[2]) if k else (points[:, 2] > center[2]))
                        ]

                        # if there are any points in the octant, create a new node
                        if in_octant.shape[0] > 0:
                            self.children.append(OctreeNode(in_octant, limit))
        else:
            # if there are not too many points, store them in this node
            self.points = points
