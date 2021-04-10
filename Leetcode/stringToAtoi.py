'''
Question link: https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.


'''


class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            s=s.lstrip()
            data=list()

            if s[0] =="-":
                data.append("-")
            elif s[0]=="+":
                pass
            elif s[0].isdigit():
                data.append(s[0])
            else:
                return 0

            for i in range(1,len(s)):
                if s[i].isdigit():
                    if s[i] != 0:
                        data.append(s[i])
                else:
                    break

            if len(s)==1 and s[0]in ["-","+"]:
                return 0
            else:
                output=int(''.join(data))
                if output<=-2**31 or output>=2**31-1:
                    if s[0]=="-":
                        return  -2**31
                    else:
                        return 2**31-1
                else:
                    return output
        except:
            return 0
