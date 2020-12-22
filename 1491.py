"""
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        summy, maxxy, minny = 0, 0, 1000000000
        for i in salary:
            if i > maxxy: maxxy = i
            if i < minny: minny = i
            summy += i
        return (summy - minny - maxxy) / (len(salary) - 2)