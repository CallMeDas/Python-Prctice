def reverse_string(str):  
    str1 = ""   
    for i in str:  
        str1 = i + str1  
    return str1    
     
str = "mom"        

if str == reverse_string(str): 
    print("The string is a palindrome.")  
else:   
    print("The string is not a palindrome.")  