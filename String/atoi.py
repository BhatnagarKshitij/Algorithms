class Solution:
    def myAtoi(self, s):
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
             
        
                
solution=Solution()
print(solution.myAtoi("     -123123DASD"))