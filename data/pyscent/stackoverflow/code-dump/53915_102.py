def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1
  result = number//base
  # Recursive case: keep dividing number by base.
  return is_power_of(result, base)
