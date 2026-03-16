'''
#1) Creating of list:
a=[1, 23, 45, 68]
print(a)
b = list((1,23,4,5,7,98))
print(b)

#2) Accessing of list: Index 0, -1
a=[1,23,45,68]
print(a[1])
print(a[2])
print(a[-1])

#3) Creating List with Repeated Elements:
a=[1,2,3]
print(a*2)

#4) Adding Elements from List:
a=[1,2,3]
a.append(50)
a.insert(1,20)
print(a)

#5) Removing Elements from List:
b=list((1,23,4,5,7,98))
print(b)
b.remove(7)
print(b)
b.pop()
print(b)
b.clear()
print(b)

LeetCode Problems:
169. Majority Element
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.

code:
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            # Add 1 if num matches candidate, else subtract 1
            count += (1 if num == candidate else -1)
            
        return candidate

#2) Creation of set:
a = {1, 2, 3, 4, 5, 6}
print(a)
b = set([1, 2, 3, 45, 5])
print(b)

#3) adding elements to set:
b = set([1,2,3,45,5])
b.add(50)
print(b)

#4) Removing 
b = set([1,2,3,45,5])
b.remove(45)
print(b)

#5) Set Operations:
a = {1,2,3,5,6}
b = {10,2,3,5,60}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Leet code: 268. Missing numbers
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
code:
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)


575. Distribute Candies

Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
Example 1:
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
Example 2:
Input: candyType = [1,1,2,3]
Output: 2
Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.
Example 3:
Input: candyType = [6,6,6,6]
Output: 1
Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.

code:
from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)
'''