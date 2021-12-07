for i in range(int(input())):
    
    num = int(input())
    
    number_of_multiples_of_3_in_num  = (num-1)//3
    number_of_multiples_of_5_in_num  = (num-1)//5
    number_of_multiples_of_15_in_num = (num-1)//15
    
    """
    total number of multiples of n in the given number
    example :-
    
        input = 100
        (100-1)//3 = 33
        so there are 33 multiples of 3 in 100
        
        input = 100
        (100-1)//5 = 19
        so there are 19 multiples of 5 in 100
    
    """
    
    sum_of_multiples_of_3  = ( 3* (number_of_multiples_of_3_in_num * ((number_of_multiples_of_3_in_num) + 1)//2))
    sum_of_multiples_of_5  = ( 5* (number_of_multiples_of_5_in_num * ((number_of_multiples_of_5_in_num) + 1)//2))
    sum_of_multiples_of_15 = ( 15*(number_of_multiples_of_15_in_num * ((number_of_multiples_of_15_in_num) + 1)//2))
    
    
    """
    sum of n terms = half of multiplication of n and n+1
    sum of n terms of any specific number =  that specific number * (half of multiplication of n and n+1)
    example :-
    
        sum of n terms of 3  = 3 * (half of multiplication of n and n+1)
        sum of 33 terms of 3 = 3 *(33 * (33 + 1)//2)
                             = 3 *(33 * 34 //2)
                             = 3 *(1122//2)
                             = 3 *(561)
                             = 1683
        
        sum of n terms of 5 = 5 * (half of multiplication of n and n+1)
    
    """
    
    total = (sum_of_multiples_of_3) + (sum_of_multiples_of_5) - (sum_of_multiples_of_15)
    
    print(total)
    
    """
    
    sn=n(n+1)
    
    """