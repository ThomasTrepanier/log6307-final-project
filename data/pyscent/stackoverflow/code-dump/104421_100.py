if __name__ == "__main__":
  nums = []
  for i in range(10):
    def generate_lambda(i):
      return lambda x: x + i
    j = generate_lambda(i)
    nums.append(j)
  for i in nums:
    print(i(1))
