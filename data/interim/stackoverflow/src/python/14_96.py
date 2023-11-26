class TransferBasicStatus(AutoEnumChoices):
    NONE = auto()
    WAITING = auto()
    PENDING = auto()
    PROGRESS = auto()
    SUCCESS = auto()
    DECLINED = auto()
    ENDED =  'ended', _('Ended - The transfer has ended with mixed states')
