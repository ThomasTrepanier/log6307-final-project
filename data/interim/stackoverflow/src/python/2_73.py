from __future__ import absolute_import
import os
import sys

import pip
from pip._internal.index.package_finder import CandidateEvaluator


class MyCandidateEvaluator(CandidateEvaluator):
    def _sort_key(self, candidate):
        (has_allowed_hash, yank_value, binary_preference, candidate.version,
         build_tag, pri) = super()._sort_key(candidate)

        priority_index = "localhost"  #use your s3pipy here
        if priority_index in candidate.link.comes_from:
            priority = 1
        else:
            priority = 0

        return (has_allowed_hash, yank_value, binary_preference, priority,
                candidate.version, build_tag, pri)


pip._internal.index.package_finder.CandidateEvaluator = MyCandidateEvaluator

# Remove '' and current working directory from the first entry
# of sys.path, if present to avoid using current directory
# in pip commands check, freeze, install, list and show,
# when invoked as python -m pip <command>
if sys.path[0] in ('', os.getcwd()):
    sys.path.pop(0)

# If we are running from a wheel, add the wheel to sys.path
# This allows the usage python pip-*.whl/pip install pip-*.whl
if __package__ == '':
    # __file__ is pip-*.whl/pip/__main__.py
    # first dirname call strips of '/__main__.py', second strips off '/pip'
    # Resulting path is the name of the wheel itself
    # Add that to sys.path so we can import pip
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

from pip._internal.cli.main import main as _main  # isort:skip # noqa


if __name__ == '__main__':
    sys.exit(_main())
