import sys
import math

def find_primes( last ):
    # Number Array
    valueRange = [ value for value in range(2, last+1) ]
    # Highest Value to Check Against
    highestValue = math.floor( math.sqrt( last ) )

    for number in valueRange:
        # See if all required numbers have been checked
        if number > highestValue:
            return valueRange
        
        # Remove non prime numbers from list
        valueRange = [ value for value in valueRange if value%number != 0 or value == number ]    


# Check if user passed script argument
if len( sys.argv ) >= 2:

    number = int( sys.argv[1] )
    primeList = find_primes( number )

    if number in primeList:

        print("%d is a prime number!" % ( number ) )
        print( primeList )

    else:

        print("%d is not a prime number!" % ( number ))
        print( primeList )
        
else:
    print("Please enter a value to see if it is prime")

