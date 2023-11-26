def to(device):
    new_self = super(VariationalGenerator, self).to(device)
    new_self._train_noise = new_self._train_noise.to(device)
    new_self._eval_noise = new_self._eval_noise.to(device)

    return new_self
