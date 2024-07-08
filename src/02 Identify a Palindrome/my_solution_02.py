from collections import deque
import re

def palindrome_test(str):
  letters_only = re.sub(r'[^a-zA-Z]', '', str)
  low_case = letters_only.lower()
  chars = deque(low_case)
  while len(chars) > 1:
    if chars[0] == chars[-1]:
      chars.pop()
      chars.popleft()
    else:
      return False
  return True


print(palindrome_test("Go hang a salami - I'm a lasagna hog!"))
