
Amount1 = int(input('please enter the amount 1 in cents:'))
Amount2 = int(input('please enter the amount 2 in cents:'))
Result =  (Amount1 + Amount2)/100
formatted_result = "{:.2f}".format(Result)
print (f' The sum of these is €{formatted_result} \n Thanks for buying with us')