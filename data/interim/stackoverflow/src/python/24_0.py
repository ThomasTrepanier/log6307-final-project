def transform_extent_pts(extent_pts, map_proj, pt_crs):
    
    xul, yul = map_proj.transform_point(
        x = extent_pts[0],
        y = extent_pts[3],
        src_crs = pt_crs)
    
    xlr, ylr = map_proj.transform_point(
        x = extent_pts[1],
        y = extent_pts[2],
        src_crs = pt_crs)

    return [xul, xlr, ylr, yul]
