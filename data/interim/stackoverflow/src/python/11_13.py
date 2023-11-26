import os

def up_n(path, n):
    components = os.path.normpath(path).split(os.sep)
    return os.sep.join(components[:-n])

if __name__ == '__main__':
    path = '/data/python_env/lib/python3.6/site-packages/matplotlib/mpl-data'
    result = up_n(path, 2)
    print(result)  # -> \data\python_env\lib\python3.6\site-packages
