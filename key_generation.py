from prime_generation import  generate_prime_number, generate_prime_candidate

#####################
#AUXILIARY FUNCTIONS#
#####################

def gcd(a, b):
    """ Calculates the Greatest Common Divisor

        Args:
            a,b -- int -- numbers

        return a integer
    """
    while a != b:
        if a > b:
            n = 2
            while a > b * n:
                n += 1
            a = (a - b * (n - 1))
        else:
            n = 2
            while b > a * n:
                n += 1
            b = (b - a * (n - 1))

    return a

def lcm(a, b):
    """ Calculates the Least Common Multiple

        Args:
            a,b -- int -- numbers

        return a integer
    """
    div = find_divisor(gcd(a, b))

    return (a / (gcd(a, b) / div)) * (b / div)

def find_divisor(a):
    s = 2
    while a % s != 0:
        s += 1
    return s

def is_coprime(a, b):
    """ Verifies if two numbers are coprimes of each other

        Args:
            a,b -- int -- numbers

        return a bool
    """
    
    #For two numbers to be coprimes their greatest common multiple has to be 1
    if gcd(a, b) == 1:
        return True
    else:
        return False

def generate_co_prime(n):
    """ Calculates a number which is a coprime

        Args:
            n -- int -- numbers

        return a integer
    """
    p = n
    while not is_coprime(p, n):
        #Using this function, because it simply generates an odd random number
        p = generate_prime_candidate(1024)
    return p

################
#MAIN FUNCTIONS#
################

def public_key():
    """ Generate the public key, composed of n and e

        return a tuple (n,e)
    """
    #Generate two random prime numbers
    #p and q should have the same magnitude, but different lengths
    p = generate_prime_number()
    q = generate_prime_number()

    n = p*q
    lambda_n = lcm(p - 1, q - 1)

    print(lambda_n)

    e = lambda_n*10
    while e > lambda_n:
        print("E")
        e = 2**16 + 1
        print(is_coprime(e, lambda_n))

    print(e)

    #NOT DONE

##########
#NOT DONE#
##########
    #Still need to find e