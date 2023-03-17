
# Define the word and character value arrays, and the code variable
word = ["A","A","A"]
chars = []
code = 1

# Put the character values for each letter into the char array
for x in word:
    chars.append(ord(x) - 64)

print(chars)

# Generate an array of primes (shamelessley stolen from Stack Overflow)
def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

# Generate an array of prime numbers < 2000
primeNums = primes2(2000)

# Multiply each prime to the power of its respective char value
i = 0
for x in chars:
   code = code * pow(primeNums[i], chars[i])
   i = i + 1

# Print the code
print(code)