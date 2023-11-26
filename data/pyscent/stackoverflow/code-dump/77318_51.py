def __setitem__(self, name, val):
    """Set the value of a header.

    Note: this does not overwrite an existing header with the same field
    name.  Use __delitem__() first to delete any existing headers.
    """
    max_count = self.policy.header_max_count(name)
    if max_count:
        lname = name.lower()
        found = 0
        for k, v in self._headers:
            if k.lower() == lname:
                found += 1
                if found >= max_count:
                    raise ValueError("There may be at most {} {} headers "
                                     "in a message".format(max_count, name))
    self._headers.append(self.policy.header_store_parse(name, val))
