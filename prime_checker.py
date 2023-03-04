def prime_checker(number):
    is_prime = True
    m =0
    for i in range(2,n): # can be made more efficient by calculating upto n/2 +1
        m=i
        if n % i ==0:
            is_prime = False
        
    if is_prime :
        print("It's a prime number.")  
        #print (m) 
    else:
        print("It's not a prime number.")
       # print(m)

    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)