def to(self, **kwargs):
    module = super(VariationalGenerator, self).to(**kwargs)
    module._train_noise = self._train_noise.to(**kwargs)
    module._eval_noise = self._eval_noise.to(**kwargs)

    return module
