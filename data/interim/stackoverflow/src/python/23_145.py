import re
from itertools import product
from dateutil.parser import parse
from collections import defaultdict, Counter

COMMON_SPECIFIERS = [
    '%a', '%A', '%d', '%b', '%B', '%m',
    '%Y', '%H', '%p', '%M', '%S', '%Z',
]


class FormatFinder:
    def __init__(self,
                 valid_specifiers=COMMON_SPECIFIERS,
                 date_element=r'([\w]+)',
                 delimiter_element=r'([\W]+)',
                 ignore_case=False):
        self.specifiers = valid_specifiers
        joined = (r'' + date_element + r"|" + delimiter_element)
        self.pattern = re.compile(joined)
        self.ignore_case = ignore_case

    def find_candidate_patterns(self, date_string):
        date = parse(date_string)
        tokens = self.pattern.findall(date_string)

        candidate_specifiers = defaultdict(list)

        for specifier in self.specifiers:
            token = date.strftime(specifier)
            candidate_specifiers[token].append(specifier)
            if self.ignore_case:
                candidate_specifiers[token.
                                     upper()] = candidate_specifiers[token]
                candidate_specifiers[token.
                                     lower()] = candidate_specifiers[token]

        options_for_each_element = []
        for (token, delimiter) in tokens:
            if token:
                if token not in candidate_specifiers:
                    options_for_each_element.append(
                        [token])  # just use this verbatim?
                else:
                    options_for_each_element.append(
                        candidate_specifiers[token])
            else:
                options_for_each_element.append([delimiter])

        for parts in product(*options_for_each_element):
            counts = Counter(parts)
            max_count = max(counts[specifier] for specifier in self.specifiers)
            if max_count > 1:
                # this is a candidate with the same item used more than once
                continue
            yield "".join(parts)
