# True - keep asking, False - stop the algorithm
def _parse_expert_decision(self, decision) -> bool:
    if decision.lower() == "y":
        # You can't go higher as current threshold is related to medicine
        self._max_threshold = self.threshold_
        if self.threshold_ - self.step < self._min_threshold:
            return False
        # Lower the threshold
        self.threshold_ -= self.step
        return True
    if decision.lower() == "n":
        # You can't got lower than this, as current threshold is not related to medicine already
        self._min_threshold = self.threshold_
        # Multiply threshold to pinpoint exact spot
        self.step *= self.change_multiplier
        if self.threshold_ + self.step < self._max_threshold:
            return False
        # Lower the threshold
        self.threshold_ += self.step
        return True
    return False
