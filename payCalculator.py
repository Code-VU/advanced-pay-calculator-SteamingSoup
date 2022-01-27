def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    rate = input('Enter Hours:')

    try:
        hrs = int(hrs)
        rate = int(rate)

        if hrs <= 40:
            pay = hrs * rate
        elif hrs > 40:
            pay = ((hrs - 40) * rate * 1.5) + rate * 40
        
        print(f'Pay: {pay}')
    
    except:
        print('Error, please enter numeric input\n')
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()