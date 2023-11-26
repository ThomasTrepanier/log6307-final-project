def to_uniq_digit_int(n):
      seen = set() # A set that collects seen digits
      result = 0
      for i in str(n): # A lazy way to iterate over digits in an integer
          if i not in seen:
              seen.add(i)
              # Since we are iterating from the most significant to the least significant, we can multiply the result by ten each time to move the integer one digit left
              result = result * 10 + int(i)
      return result
