'''

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

'''

# fizz buzz problem in Python

# adding necessary imports
from typing import List

# naming a class
class Solution:
    def FizzBuzz(self, n: int) ->List[str]:
        # defining an array of numbers ex:1,2,3...
        result =[]
        # a counter that counts from 1,2,3...
        for i in range(1, n + 1):
        # if statement condition if the number is divisibale by both 3 and 5 example 15
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")

        # if the number is divisibale by 3
            elif i % 3 == 0:
                print("Fizz")
        # if the number is divisibale by 5
            elif i % 5 == 0:
                print("Buzz")
        # else it code will print out the number itself. for example 2 isn't divisible by 3 nor 5 
            else:
                result.append(str(i))
        return result

sol = Solution()
print(sol.FizzBuzz(18))
    
