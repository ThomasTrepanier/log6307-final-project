def _apply(self, fn):
    super(VariationalGenerator, self)._apply(fn)
    self._train_noise = fn(self._train_noise)
    self._eval_noise = fn(self._eval_noise)
    return self
