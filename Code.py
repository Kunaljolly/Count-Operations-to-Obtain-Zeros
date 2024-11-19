class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 ==0 or num2 == 0:
            return 0
        c = 0
        while(num1 != 0 or num2 != 0):
            if num1>num2:
                c+=1
                num1 = num1 - num2
                if num1<=0:
                    return c
                
            else:
                num2 = num2 - num1
                c+=1
                if num2<=0:
                    return c
                
        return c
