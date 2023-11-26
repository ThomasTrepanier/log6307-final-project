import dataclasses
from typing import Optional


@dataclasses.dataclass
class FileObject:
    uploaded_by: Optional[str] = None

class FileObjectExpensive(FileObject):
    @property
    def uploaded_by(self):
        return self._uploaded_by

    @uploaded_by.setter
    def uploaded_by(self, uploaded_by):
        print('Setter Called with Value ', uploaded_by)
        self._uploaded_by = uploaded_by

    def save(self):
        print(self.uploaded_by)

p = FileObjectExpensive()
p.save()
p2 = FileObjectExpensive(uploaded_by='Already Computed')
p2.save()
