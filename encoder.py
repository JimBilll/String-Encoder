
# Encode a given word
def encode(word):
    # Define the char array for storing the shifted unicode values
    # and the code variable for holding the code.
    chars = []
    code = 1
    
    # Put the character values for each letter into the char array
    for x in word:
        chars.append(ord(x) - 64)

    # print(chars)

    # Generate an array of prime numbers < 2000
    primeNums = primes2(2000)

    # Multiply each prime to the power of its respective char value
    i = 0
    for x in chars:
        code = code * pow(primeNums[i], chars[i])
        i = i + 1

    return code

# Decode a given code to a word
def decode(code):
    # Find the prime factors, evaluate those factors. Declare empty array for the decoded word
    factors = prime_factors(code)
    chars = evalFactors(factors)
    word = []
    
    # convert back the character values and puts their respective chars into word
    for x in chars:
        word.append(chr(x + 64))
    
    return word

# Evaluate the factors into a correctly formatted array
def evalFactors(factors):
    i = 1
    shift = 1
    newArr = []
    primes = primes2(2000)

    for x in primes:
        occur = factors.count(x)
        if occur > 0:
            newArr.append(occur)
        else:
            break
    return newArr

# Generate the equation for a given word
def genEq(word):
    # Define the char array for storing the shifted unicode values
    # and the eq variable for holding the equation.
    chars = []
    Eq = ''
    
    # Put the character values for each letter into the char array
    for x in word:
        chars.append(ord(x) - 64)

    # Generate an array of prime numbers < 2000
    primeNums = primes2(2000)

    # Concatenate the multiplication of each prime to the power of its respective char value
    i = 0
    for x in chars:
        if i == 0:
            Eq += "2<sup>" + str(x) + "</sup> "
        else:
            Eq += "× " + str(primeNums[i]) + "<sup>" + str(x) + "</sup> "
        i = i + 1
    return Eq

#
# Code shamelessly stolen from Stack Overflow
#

# Generate an array of primes (https://stackoverflow.com/a/3035188)
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

# Create an array of the prime factors of a number (https://stackoverflow.com/a/22808285)
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors