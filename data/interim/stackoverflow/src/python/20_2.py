# from dbutils import FileInfo # Not required in databricks
# from dbruntime.dbutils import FileInfo # may work for some people

def get_size_of_path(path):
    return sum([file.size for file in get_all_files_in_path(path)])

def get_all_files_in_path(path, verbose=False):
    nodes_new = []

    nodes_new = dbutils.fs.ls(path)
    files = []

    while len(nodes_new) > 0:
        current_nodes = nodes_new
        nodes_new = []
        for node in current_nodes:
            if verbose:
                print(f"Processing {node.path}")
            children = dbutils.fs.ls(node.path)
            for child in children:
                if child.size == 0 and child.path != node.path:
                    nodes_new.append(child)
                elif child.path != node.path:
                    files.append(child)
    return files

path = "s3://some/path/"

print(f"Size of {path} in gb: {get_size_of_path(path) / 1024 / 1024 / 1024}")
