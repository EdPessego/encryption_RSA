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

def generate_coprime(n, length):
    """ Calculates a number which is a coprime

        Args:
            n, length -- int -- numbers

        return a integer
    """
    p = n
    while not is_coprime(p, n):
        #Using this function, because it simply generates an odd random number
        p = generate_prime_candidate(length)
    return p

################
#MAIN FUNCTIONS#
################

class message_receiver:
    def __init__(self):
        pass

    def public_key(self):
        """ Generate the public key, composed of n and e

            Args:
                self -- object

            return a tuple (n,e)
        """
        #Generate two random prime numbers
        #p and q should have the same magnitude, but different lengths
        p = generate_prime_number()
        q = generate_prime_number()

        self.n = p*q
        self.lambda_n = lcm(p - 1, q - 1)

        #generate e, a number who is coprime with n, and bigger then 1 and smaller than lambda_n
        self.e = generate_coprime(self.n, len(bin(int(self.lambda_n))[2:]) - 1)

        return(self.n, self.e)

    def private_key(self):
        """ Generate the private key, composed of d

            Args:
                self -- object
        """

        #NOT CORRECT
        #WORK IN PROGRESS
        self.d = pow(1/self.e, 1, int(self.lambda_n))



Alice = message_receiver()
print(Alice.public_key())
print(Alice.private_key())
