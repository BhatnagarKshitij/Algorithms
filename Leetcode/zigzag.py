'''
Question link: https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
            if numRows==1 or numRows==0:
                return s
            data=[""]*numRows
            mode=number=0
            for letters in s:
                if mode==0:
                    data[number]+=letters
                    number+=1
                else:
                    data[number]+=letters
                    number-=1

                if number==numRows:
                    mode=1
                    number=numRows-2
                elif number==-1:
                    mode=0
                    number=1
            return ''.join(data)
