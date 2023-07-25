from collections import Counter


def sum_mean_of_num(a=None, b=None):
    ''' sum_mean_of_num calculates and returns the sum and average of two numbers
    :param a, b: input float number
    :return: sum and mean of a and b
    '''
    if a is None:
        while True:
            try:
                a = float(input('Enter the first number: '))
                break
            except:
                print('Invalid entry. Enter a number.')
                continue
    if b is None:
        while True:
            try:
                b = float(input('Enter the second number: '))
                break
            except:
                print('Invalid entry. Enter a number.')
                continue
    # calculating the sum and product of a and b
    summation = format(a + b, '.2f')
    mean = format((a + b) / 2, '.2f')
    return float(summation), float(mean)


def test_sum_mean_of_num():
    print('\n----------------- Test Function 1: Sum and Average of Two Numbers\n')
    # Test Case 1
    print('test_sum_avg_of_2_num_1 | sum_mean_of_num(3,-5.23)')
    expected_result = (-2.23, -1.12)
    actual_result = sum_mean_of_num(3, -5.23)
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')
    # Test Case 2
    print('test_sum_avg_of_2_num_2 | sum_mean_of_num(-0.12345,12345)')
    expected_result = (12344.88, 6172.44)
    actual_result = sum_mean_of_num(-0.12345, 12345)
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')
    print('----------------- End Test Function\n')


def max_min_of_set(number_of_numbers=None, number=None):
    """
    max_min_of_set determines the min and max of a set of numbers
    :param number_of_numbers: the number of numbers user would like to enter
    :param number: individual number input as part of the set of numbers
    :return: the min and max of the set of numbers
    """
    # initialize variables
    count = 1
    min_number = number
    max_number = number
    # let user set the number of numbers they'd like to enter
    if number_of_numbers is None:
        while True:
            try:
                number_of_numbers = int(input('Enter the number of numbers you\'d like to enter [1,5]: '))
                if number_of_numbers < 1 or number_of_numbers > 5:
                    print('Number of numbers entered cannot be less than 1 or greater than 5.')
                    continue
                break
            except:
                print('Invalid number of numbers. Enter a whole number.')
                continue
    # let user input numbers within maximum number of numbers they'd like to enter
    if number is None:
        while count < (number_of_numbers + 1):
            try:
                number = int(input(f'Enter number {count}: '))
                if max_number is None and min_number is None:
                    max_number = number
                    min_number = number
                elif number > max_number:
                    max_number = number
                elif number < min_number:
                    min_number = number
                count += 1
            except:
                print('Invalid number. Enter a whole number.')
                continue
    return min_number, max_number


def test_max_min_of_set():
    print('\n----------------- Test Function 2: Max and Min of N Numbers\n')
    # Test Case 1
    print('test_max_min_of_set_1 | max_min_of_set(1,456)')
    expected_result = (-123, 89)
    actual_result = max_min_of_set(1, 1)
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')
    print('----------------- End Test Function\n')


def area_perimeter_of_rect(length=None, width=None):
    """ area_perimeter_of_rect calculates the area and perimeter of a rectangle when given the width and length
    :param length: length of rectangle
    :param width: width of rectangle
    :return: area and perimeter of the rectangle
    """
    if length is None:
        while True:
            try:
                length = float(input('Enter the length of the rectangle: '))
                if length <= 0:
                    print('Length and width must be greater than 0.')
                    continue
                break
            except:
                print('Invalid entry. Enter a number.')
    if width is None:
        while True:
            try:
                width = float(input('Enter the width of the rectangle: '))
                if width <= 0:
                    print('Length and width must be greater than 0.')
                    continue
                break
            except:
                print('Invalid entry. Enter a number.')
    # calculates the area and perimeter of the rectangle with values provided
    area = length * width
    perimeter = (2 * length) + (2 * width)
    return area, perimeter


def test_area_perimeter_of_rect():
    print('\n----------------- Test Function 3: Area and Perimeter of a Rectangle\n')
    # Test Case 1
    print('test_area_perimeter_of_rect_1 | area_perimeter_of_rect(1,1)')
    expected_result = (1, 4)
    actual_result = area_perimeter_of_rect(1, 1)
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')
    print('----------------- End Test Function\n')


def sum_product_1st_n_natural(number_of_numbers=None, number=None):
    """ sum_product_1st_n_natural calculates the sum and product of numbers 1 to N provided by the user
    :param number_of_numbers: the total count of numbers the user would like to input
    :param number: number input in series of numbers 1 to N
    :return: sum and product of numbers 1 to N
    """
    # initialize variables
    count = 0
    sum = 0
    product = 0
    # let user set the number of numbers they'd like to enter
    if number_of_numbers is None:
        while True:
            try:
                number_of_numbers = int(input('Enter the number of natural numbers you\'d like to calculate the sum '
                                              'and product of [2,20]: '))
                if number_of_numbers < 2 or number_of_numbers > 20:
                    print('Number of numbers entered cannot be less than 2 or greater than 20.')
                    continue
                break
            except:
                print('Invalid number of numbers. Enter a whole number.')
                continue
    # let user input numbers within maximum number of numbers they'd like to enter
    if number is None:
        while count < number_of_numbers:
            try:
                number = int(input(f'Enter number {count + 1}: '))
                sum += number
                if count == 0:
                    product = number
                else:
                    product = product * number
                count += 1
            except:
                print('Invalid number. Enter a whole number.')
                continue
    return sum, product


def test_sum_product_1st_n_natural():
    print('\n----------------- Test Function 4: Sum and Product of First N Natural Numbers\n')
    # Test Case 1
    print('test_sum_product_1st_n_natural_1 | sum_product_1st_n_natural(2,1,2)')
    expected_result = (3, 2)
    actual_result = sum_product_1st_n_natural(3, {1, 2})
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')
    print('----------------- End Test Function\n')


def string_info(text=None):
    """ string_info requests a string from the user and performs string calculations and manipulations
    :input text: string input by user
    :return: number of characters in the string, number of words in the string, a copy of the string capitalized, and the string in lower case
    """
    if text is None:
        while True:
            try:
                text = str(input('Enter a string: ')).strip()
                if len(text) < 1:
                    print('Enter a string with more than 0 characters.')
                    continue
                break
            except:
                continue
    # counts number of words in string
    word_count = Counter(text.split())
    return len(text), len(word_count), text.capitalize(), text.lower()


def test_string_info():
    print('\n----------------- Test Function 5: String Info\n')
    # Test Case 1
    print('test_string_info_1 | string_info(\'rOsE\')')
    expected_result = (4, 1, 'Rose', 'rose')
    actual_result = string_info('rOsE')
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')

    # Test Case 2
    print('test_string_info_2 | string_info(\'   rose bud  aford \')')
    expected_result = (19, 3, '   rose bud  aford ', '   rose bud  aford ')
    actual_result = string_info('   rose bud  aford ')
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')

    # Test Case 3
    print('test_string_info_3 | string_info(\'!@# 6 - 3 = 3.22 TWO to0.\')')
    expected_result = (24, 8, '!@# 6 - 3 = 3.22 two to0', '!@# 6 - 3 = 3.22 two to0')
    actual_result = string_info('!@# 6 - 3 = 3.22 TWO to0')
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')
    print('----------------- End Test Function\n')


def calculator(a=None, operand=None, b=None):
    """ calculator performs basic calculator operations such as addition, subtraction, multiplication, and division
    :param a: first number input by user
    :param operand: operation chosen by user to be performed
    :param b: second number input by user
    :return: result of operation on a and b
    """
    if a is None:
        while True:
            try:
                a = float(input('Enter the first number: '))
                break
            except:
                print('Invalid first number. Enter a number.')
                continue
    if operand is None:
        while True:
            try:
                operand = str(input('Enter the operand (+, -, *, /): ')).strip()
                if operand != '+' and operand != '-' and operand != '*' and operand != 'x' and operand != '/':
                    print('Invalid operand. Enter an operand from within these options: +, -, *, /')
                    continue
                break
            except:
                print('Invalid operand. Enter an operand from within these options: +, -, *, / ')
                continue
    if b is None:
        while True:
            try:
                b = float(input('Enter the second number: '))
                break
            except:
                print('Invalid second number. Enter a number.')
                continue
    # perform calculation based on operand provided
    if operand == '+':
        return a + b
    elif operand == '-':
        return a - b
    elif operand == '*' or operand == 'x':
        return a * b
    else:
        return a / b


def test_calculator():
    print('\n----------------- Test Function 6: Calculator\n')
    # Test Case 1
    print('test_calculator_1 | calculator(1, +, 3)')
    expected_result = 4
    actual_result = calculator(1, '+', 3)
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')


    # Test Case 2
    print('test_calculator_2 | calculator(-3, -, 10)')
    expected_result = -13
    actual_result = calculator(-3, '-', 10)
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')


    # Test Case 3
    print('test_calculator_3 | calculator(-12.4, *, 0.22)')
    expected_result = -2.728
    actual_result = calculator(-12.4, '*', 0.22)
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')

    # Test Case 4
    print('test_calculator_4 | calculator(26, /, 9)')
    expected_result = 2.888888888888889
    actual_result = calculator(26, '/', 9)
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')


    # Test Case 5
    print('test_calculator_5 | calculator(3, x, 2)')
    expected_result = 6
    actual_result = calculator(3, 'x', 2)
    print(f'actual result: {actual_result} | expected result: {expected_result} |', end=' ')
    if actual_result == expected_result:
        print('PASS\n')
    else:
        print('FAIL\n')
    print('----------------- End Test Function\n')
