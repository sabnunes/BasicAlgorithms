from Algorithms import *

def test_algorithms():
    # Manual test functions
    test_sum_mean_of_num()
    test_max_min_of_set()
    test_area_perimeter_of_rect()
    test_sum_product_1st_n_natural()
    test_string_info()
    test_calculator()

def main():
    # menu ----
    string_menu = '''
Basic Algorithms -------------

[1] Sum and Average of Two Numbers
[2] Maximum and minimum of 5 numbers
[3] Area and Perimeter of a rectangle
[4] Sum and product of first N natural numbers
[5] String Info
[6] Calculator
[7] Test Functions
    '''
    # variable true when user wants to continue
    repeat = True
    # repeat loop -- until the user chooses n
    while repeat:
        # display the menu
        print(string_menu)
        # input validation loop - validates the choice selection [0-7]
        while True:
            try:
                # accept the user choice - should be an integer 0-7 - convert to int()
                choice = int(input("Select 1-7 or 0 to exit: "))
                # exit the validation loop if the input is fine
                if choice in range(8):
                    break
                continue
            except:
                continue

        if choice == 1:
            print("------------------------")
            print("[1] Sum and Average of Two Numbers")
            output_sum_mean_of_num = sum_mean_of_num()
            print(f'Sum: %.2f | Average: %.2f' % (output_sum_mean_of_num[0], output_sum_mean_of_num[1]))
        elif choice == 2:
            print("------------------------")
            print("[2] Maximum and minimum of 5 numbers")
            output_max_min_of_set = max_min_of_set()
            print(f'Min: %d | Max: %d' % (output_max_min_of_set[0], output_max_min_of_set[1]))
        elif choice == 3:
            print("------------------------")
            print("[3] Area and Perimeter of a rectangle")
            output_area_perimeter_of_rect = area_perimeter_of_rect()
            print(f'Area: %.1f | Perimeter: %.1f' % (output_area_perimeter_of_rect[0], output_area_perimeter_of_rect[1]))
        elif choice == 4:
            print("------------------------")
            print("[4] Sum and product of first N natural numbers")
            output_sum_product_1st_n_natural = sum_product_1st_n_natural()
            print(f'Sum: %d | Product: %d' % (output_sum_product_1st_n_natural[0], output_sum_product_1st_n_natural[1]))
        elif choice == 5:
            print("------------------------")
            print("[5] String Info")
            output_string_info = string_info()
            print(f'Number of characters in string: {output_string_info[0]}')
            print(f'Number of words in string: {output_string_info[1]}')
            print(f'String capitalized: {output_string_info[2]}')
            print(f'String lower case: {output_string_info[3]}')
        elif choice == 6:
            print("------------------------")
            print("[6] Calculator")
            output_calculator = calculator()
            print(output_calculator)
        elif choice == 7:
            print("------------------------")
            print("[7] Test Functions")
            test_algorithms()
        elif choice == 0:
            print("Thanks for your time, good bye!")
            repeat = False
            break

        # exit program
        input('\nType any key to continue...')


if __name__ == '__main__':
    main()
