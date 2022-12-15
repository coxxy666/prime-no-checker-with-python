

def prime_number(number) :

   for i in Range(0, number):

      if number % i == 0 : 
         print("Not a prime number")

      else : 
         print("prime number")


   print(prime_number(3))