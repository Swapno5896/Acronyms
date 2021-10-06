## let's practise try except else finally
try:
    a = int(input('Enter first number : ')) 
    b = int(input('Enter first number : '))
    c = a + b
except ZeroDivisionError:
    print('Please enter number greater then zoro')
except TypeError:
    print('Please enter number')
except Exception as ex:
    print('The exception is {}'.format(ex) )
else:
    print('The sum of your input is {}'.format(c))
finally:
    print('The execution of our program is done')