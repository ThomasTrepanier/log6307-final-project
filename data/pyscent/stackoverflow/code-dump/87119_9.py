def build_mosaic(list_of_images, num_mosaic_rows, num_mosaic_cols):

    list_of_mosaic_rows = []

    for row_number in range(num_mosaic_rows):

        list_of_mosaic_rows = list_of_images[row_number*num_mosaic_cols,(row_number+1)*num_mosaic_cols]

    mosaic = np.vstack(list_of_mosaic_rows)

    return mosaic
