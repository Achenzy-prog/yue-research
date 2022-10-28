import time
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

 
def SieveOfEratosthenes(n):
    primes = []
        
    # Create a boolean array "prime[0..n]" and set all entries as true
    prime = [True for i in range(n + 1)]

    #If i is not prime, change prime[i] to false 
    p = 2
    while (p * p <= n):
           
        # If prime[p] is not changed, then it's prime
        if (prime[p] == True):
               
            #all multiples of p set to false
            for i in range(p * p, n + 1, p):
                prime[i] = False
                 
        p += 1
       
    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes
#less_than_n = []
#for x in range(100000):
#  less_than_n.append(x)

less_than_n=np.geomspace(2, 1000000, 100, dtype=np.int)

if __name__=='__main__':
    count = []
    timetaken = []

    i=0 
    while i < len(less_than_n):
      start_time = time.time()    
      b = SieveOfEratosthenes(less_than_n[i])
      #print(b)
      #print(len(b))
      count.append(len(b))
      
      #print(nthprime[i]+1, "prime number is", primes[nthprime[i-1]])
      #Time calculation
      timetaken.append(time.time() - start_time)
      i = i + 1
   
    print("time:", timetaken)
    print(count)
   

  
#Plot time against number of primes
fig1, ax1 = plt.subplots()
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.scatter(less_than_n, timetaken)


#calculate r^2
res = stats.linregress(less_than_n, timetaken)
print(f"R-squared: {res.rvalue**2:.6f}")
