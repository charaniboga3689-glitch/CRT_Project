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

'''

