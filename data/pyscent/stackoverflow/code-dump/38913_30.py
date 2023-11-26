from pathlib import Path
import re

def f_path(path):
    """
    path: str full path, with user's home folder, 
          would be translated to current user's home folder,
          for example, "/Users/jane/some/path" would be translated to
          "/Users/tom/some/path", if current user is Tom.
    """
    # current home folder
    home = str(Path.home())
    # creating regular expression like "^/Users/[^/]+", for later use:
    path_reg = "^" + re.sub("[^/]+$", "", home) + "[^/]+"
    # replacing old home path part to a new one
    return re.sub(path_reg, home, path)
