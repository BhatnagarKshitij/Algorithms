# def ina(x):
#     if x<2**31-1 and x>-2**31:
#         string=str(x)
#         if string[0]=="-":
#             return "-"+str(int(string[:0:-1]))
#         else:
#             return str(int(string[::-1]))
#     else:
#         return 0
# print(ina(1534236469))
# 

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = [1,-1][x < 0]
    rst = sign * int(str(abs(x))[::-1])
    return rst if -(2**31)-1 < rst < 2**31 else 0

print(reverse(12345))
print(x)
