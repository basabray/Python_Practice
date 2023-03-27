#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Check if the gievn number is odd or even
def check_odd_even(n):
    if n%2==0:
        return 'EVEN'
    else:
        return 'ODD'
    
# Check if the given number is prime or not
def check_prime(n):
    for i in range(2,n):
        if n%i==0:
            return 'Not Prime'
    else:
        return 'Prime'


if __name__ == '__main__':
    n = 21
    result1 = check_odd_even(n)
    result2 = check_prime(n)
    print(result1,result2)

