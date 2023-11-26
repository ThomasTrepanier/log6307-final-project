import os
import re
import pandas as pd
 
def count_files(top, pattern, list_files):
  top = os.path.abspath(os.path.expanduser(top))
  res = []
  for root, dirs, files in os.walk(top):
    name_space = os.path.relpath(root, top)
    level = os.path.normpath(name_space).count(os.sep) + 1 if name_space != '.' else 0
    matches = [file for file in files if re.search(pattern, file)]
    if matches:
      if list_files:
        res.append((pattern, level, name_space, len(matches), matches))
      else:
        res.append((pattern, level, name_space, len(matches)))

  if list_files:
    df = pd.DataFrame(res, columns=['pattern', 'level', 'name_space', 'count', 'files'])
  else:
    df = pd.DataFrame(res, columns=['pattern', 'level', 'name_space', 'count'])
  return df
