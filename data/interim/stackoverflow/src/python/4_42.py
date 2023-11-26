from copy import deepcopy

@dataclass(frozen=True)
class A:
    a: str = ''
    b: int = 0

    def mutate(self, **options):
        new_config = deepcopy(self.__dict__)
        # some validation here
        new_config.update(options)
        return self.__class__(**new_config)
