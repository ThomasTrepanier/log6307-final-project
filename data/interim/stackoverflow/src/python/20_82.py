from dbutils import FileInfo
from typing import List

root_path = "/mnt/datalake/.../XYZ"

def discover_size(path: str, verbose: bool = True):
  def loop_path(paths: List[FileInfo], accum_size: float):
    if not paths:
      return accum_size
    else:
      head, tail = paths[0], paths[1:]
      if head.size > 0:
        if verbose:
          print(f"{head.path}: {head.size / 1e6} MB")
        accum_size += head.size / 1e6
        return loop_path(tail, accum_size)
      else:
        extended_tail = dbutils.fs.ls(head.path) + tail
        return loop_path(extended_tail, accum_size)

  return loop_path(dbutils.fs.ls(path), 0.0)

discover_size(root_path, verbose=True)  # Total size in megabytes at the end

