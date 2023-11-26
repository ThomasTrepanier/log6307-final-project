def file_dir():
    directories = []
    res = {}
    cwd = os.getcwd()
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(".tsv"):
                directories.append(os.path.join(root, file))
    res['dir'] = directories
    return res
