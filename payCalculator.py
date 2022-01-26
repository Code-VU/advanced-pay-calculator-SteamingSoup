def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    
    rate = input('Enter Rate: ')

    try:
        if int(hrs) > 40:
            pay = int(hrs) * int(rate) * 1.5
            print(f'Pay: {pay}')
    except:
        print('Error, please enter numeric input\n')

    try:
        if int(hrs) <= 40:
            pay = int(hrs) * int(rate)
            print(f'Pay: {pay}')

    except:
        print('Error, please enter numeric input\n')
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()