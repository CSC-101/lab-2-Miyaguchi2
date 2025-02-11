# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."
   return message


message = welcome_message("nmiyaguc@calpoly.edu")
print(message)

# TASK 3
def smallest(n:float, m:float) -> float:
   if n < m:
      return n              # The first call
   else:
      return m

first = smallest(3,2)       # 3
second = smallest(2,2)      # The value of second is 2. This isn't a reasonable result however, because 2 isn't less than 2.
print(second)

def function2(a:int, b:int, c:int) -> int:
   if a > b and a > c:
      return a - b          # When the first in value is the greatest of the 3
   elif b > c:
      return b + c          # When the second int value is the greatest of the 3
   else:
      return 2 * c          # When the third int value is the greatest of the 3

answer1 = function2(3, 2,1)    # 1
answer2 = function2 (2, 3, 1)  # 4
answer3 = function2(2, 1, 3)   # 6
print(answer3)

# TASK 4
from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional:
   test = idx >= 0 and idx < len(L)           # The value of test in the first call is False. In the second it is True.
   if test:                                   # This check is preventing an index out of bounds error
      return L[idx]
   else:
      return None

first = checked_access([1,0,1], 9)     #  None
second = checked_access([1,0,1], 2)    # 1
print(first)

def length_sum(L:list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2]) # the first call. The values being added are the length of the first three string values in L
   elif len(L) > 0:
      result = len(L[0])                         # The second and third calls. The value of the first index value is what the function will return.
   else:
      result = 0

   return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(third)

def surprising(L:list[str], other:str) -> list[str]:
   L.append(other.upper())
   return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
        # ["this", "is", "such", "confusing", "code", "AVOID", "SUCH."]
        # ["this", "is", "such", "confusing", "code", "AVOID", "SUCH."]
        # The .append() function on line 1 of the surprising function added the two strings from the function calls to the words list.
print(words)