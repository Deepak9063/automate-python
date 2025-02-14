
def prime_num(n):


    if i<=1:
       return False

    for i in range(2,n+1):
        if n%i==0:
          break

          if i==n:
              return True

          else:
             return False

        if res == False:
            print("It is not a prime number")

        else:
            print("It is prime number")
res = prime_num(5)
print(res)


