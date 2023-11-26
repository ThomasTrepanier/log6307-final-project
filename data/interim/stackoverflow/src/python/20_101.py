def make_collection_from_data(data, collection_maker):
    return collection_maker(data)

data = [1, 2, 3, 4]

make_collection_from_data(data, set) # Returns a list
make_collection_from_data(data, list) # Returns a set
