bill_amount=int(input('enter amount of payment-'))
mode_of_payment=input('enter mode of payment-')
if mode_of_payment=='credit card':
    print('price after discount is', bill_amount-(bill_amount*0.1))
elif mode_of_payment=='debit card':
    print('price after discount is', bill_amount-(bill_amount*0.05))
elif mode_of_payment=='net banking':
    print('price after discount is', bill_amount-(bill_amount*0.02))
else:
    print('final price is', bill_amount)

    
    
