class NotRandom:

    numbers = np.arange(1,10.5,0.5)
    last_index = -1

    @classmethod
    def nrng(cls):
        cls.last_index += 1
        if cls.last_index < len(cls.numbers):
            return cls.numbers[cls.last_index]
        # else:
        return None

# Create an alias to the classmethod
nrng = NotRandom.nrng      # Note this is OUTSIDE the class
