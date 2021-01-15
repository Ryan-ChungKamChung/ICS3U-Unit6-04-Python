#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program adds a 2d array together


import random


def average(numbers_2d, rows, columns):
    # Rounds user input to chosen amount of decimal values

    total = 0

    for row_value in numbers_2d:
        for single_element in row_value:
            total += single_element

    number_of_values = rows * columns

    average = total / number_of_values

    return average


def main():
    # Takes user input, passes it to functions and calls them

    numbers_2d = []

    while True:
        rows_string = input("How many rows?: ")
        try:
            rows = int(rows_string)
            assert rows > 0
            break
        except AssertionError:
            print("This isn't a valid input")
        except Exception:
            print("This isn't a valid input")

    while True:
        columns_string = input("How many columns?: ")
        try:
            columns = int(columns_string)
            assert columns > 0
            break
        except AssertionError:
            print("This isn't a valid input")
        except Exception:
            print("This isn't a valid input")

    for rows_loop_counter in range(0, rows):
        temp_column = []
        for columns_loop_counter in range(0, columns):
            temp_column.append(random.randint(0, 50))

        numbers_2d.append(temp_column)

    for print_counter in range(0, columns):
        print(numbers_2d[print_counter])

    average_number = average(numbers_2d, rows, columns)

    print("The average is: {}".format(average_number))


if __name__ == "__main__":
    main()
