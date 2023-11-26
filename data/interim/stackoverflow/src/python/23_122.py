import dataclasses


@dataclasses.dataclass
class FileObject:
    uploaded_by: str = None

    def save(self):
        print(self.uploaded_by)

    @property
    def _uploaded_by(self):
        return self._uploaded_by_attr

    @_uploaded_by.setter
    def _uploaded_by(self, uploaded_by):
        # print('Setter Called with Value ', uploaded_by)
        self._uploaded_by_attr = uploaded_by


# --- has to be called at module level ---
FileObject.uploaded_by = FileObject._uploaded_by


def main():
    p = FileObject()
    p.save()                            # displays 'None'

    p = FileObject()
    p.uploaded_by = 'foo'
    p.save()                            # displays 'foo'

    p = FileObject(uploaded_by='bar')
    p.save()                            # displays 'bar'


if __name__ == '__main__':
    main()
