from pprint import pprint

cont_det = [
    ['TASU 117000 0', "TGHU 759933 - 0", 'CSQU3054383', 'BMOU 126 780-0', "HALU 2014 13 3"],
    ['40HS'],
    ['Ha2ardous Materials', 'Arm5 Maehinery'],
]


def rotate_matrix(source):
    result = []

    # let's find the longest sub-list length
    length = max((len(row) for row in source))

    # for every column in sub-lists create a new row in the resulting list
    for column_id in range(0, length):
        result.append([])

        # let's fill the new created row using source row columns data.
        for row_id in range(0, len(source)):
            # let's use the first value from the sublist values if source row list has it for the column_id
            if len(source[row_id]) > column_id:
                result[column_id].append(source[row_id][column_id])
            else:
                try:
                    result[column_id].append(source[row_id][0])
                except IndexError:
                    result[column_id].append(None)

    return result


pprint(rotate_matrix(cont_det))
