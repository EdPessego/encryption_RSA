from random import randint

def is_prime(n, k):
    '''Test if a number is prime
    
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do

        return True if n is prime
    '''

    ###################
    #VERIFY CONDITIONS#
    ###################

    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0:
        return False

    ##############
    #FIND r AND s#
    ##############

    s = 0
    r = n-1
    while r % 2 == 0 or s <= 0:
        s += 1
        r //= 2

    ############
    #DO k TESTS#
    ############
    
    for i in range(k):
        #Choose a random a
        a = randint(2,n-1)

        # a^r mod n OR a^((2^0)*r) mod n
        test = pow(a, r, n)

        #If test == 1 or n - 1 then it would have passed the test
        if test != 1 or test != n - 1:
            d = 1
            #a^((2^d)*r) mod n
            test = pow(test, 2, n)

            while d <= s - 1 or test != n - 1:
                test = pow(a, 2, n)

                if test == 1:
                    #test needs to be equal to -1 or n - 1
                    return False
                j += 1
            
            if x != n - 1:
                #In case the loop broke, because j = s - 1
                return False
            #It passed the test
    
    #It passed all the tests
    return True