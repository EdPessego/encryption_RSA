from prime_generation import  generate_prime_number

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
           a = (a - b)
        else:
           b = (b - a)
    return a

def lcm(a, b):
    """ Calculates the Least Common Multiple

        Args:
            a,b -- int -- numbers

        return a integer
    """

    return a * b / gcd(a, b)

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
    #NOT DONE


