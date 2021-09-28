#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Sept 2021
# This program uses while loop


def main():
    # This function gives the sum of all the numbers icludng the number given
    loop_counter = 0
    total = 0
    # Input
    user_input = input("Please a positive interger : ")

    try:
        # Process and Output
        user_input = int(user_input)
        while loop_counter <= user_input:
            total = total + loop_counter
            loop_counter += 1
        print(
            "The sum of all the integers from 1 to {0} is {1}".format(user_input, total)
        )
    except Exception:
        print("Invalid input")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
