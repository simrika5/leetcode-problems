
#Palindrome Problem: 
"""Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindrome(self, num:int)-> bool:
        if num<0 or (num%10==0 and num!=0):    
            return False 
        rev=0 
        while num>rev:           
            lastdigit=num%10    
       
            rev= rev*10+ lastdigit  
            num=num//10 
        return num==rev or num==rev//10 


    
#1st : 121>0 
# 121 last digit= 121%10= 1 
#rev= 0*10+1= 1 
#121=121//10= 12
#2nd: 12>1 
#last digit: 12%10=2
#reverse = 1*10+2= 12 
#num= 12//10=1 
#3rd: 1>12 exits loop 
# num: 1 and reverse : 12 so, 1==12 (false) OR 1==12//10(1), true,  F V T= T 