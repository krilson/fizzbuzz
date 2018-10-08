
while True:
    number = int(raw_input("FizzBuzz Game" '\n' "Select a number between 1 and 100: "))

    for count in range(number, 100):

        if count > 100:
            break
        elif count % 3 == 0 & count % 5 == 0:
            print "fizzbuzz"
        elif count % 3 == 0:
            print "fizz"
        elif count % 5 == 0:
            print "buzz"
        else:
            print count
