class Group(enum.Enum):
    user = 0
    manager = 1
    admin = 2

    def __repr__(self) -> str:
        return self.name
