train_scheduler = CosineAnnealingLR(optimizer, num_epochs)

def warmup(current_step: int):
    return 1 / (10 ** (float(number_warmup_epochs - current_step)))
warmup_scheduler = LambdaLR(optimizer, lr_lambda=warmup)

scheduler = SequentialLR(optimizer, [warmup_scheduler, train_scheduler], [number_warmup_epochs])
