def BracketMatcher(strParam: str) -> bool:
  pairs = {'(':')', '[':']', '{':'}'}
  stack = []
  for c in strParam:
    if c in '([{':
      stack.append(c)
    elif c in ')]}':
      if not stack or c != pairs[stack[-1]]:
        return False
      stack.pop()
  return len(stack) == 0
