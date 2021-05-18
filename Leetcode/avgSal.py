'''
Question link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.
'''


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return (sum(salary)-salary[0]-salary[-1])/(len(salary)-2)
        
