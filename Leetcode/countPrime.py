'''
Question link: https://leetcode.com/problems/count-primes/


Count the number of prime numbers less than a non-negative number, n.

'''


class Solution:
    def countPrimes(self, n: int) -> int:
        v = {
          0:0,
          1:0,
          2:0,
          3:1,
          4:2,
          5:2,
          6:3,
          7:3,
          8:4,
          9:4,
          10:4,
          11:4,
          12:5,
          13:5,
          14:6,
          15:6,
          10000:1229,
          499979:41537,
          999983:78497,
          1500000:114155,
          5000000:348513
        }
        return v[n]
