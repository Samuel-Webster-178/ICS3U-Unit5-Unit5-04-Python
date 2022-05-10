#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


import math


def CalculateVolume(radius, height):
    # I calculate circumference

    # process
    volume = math.pi * height * radius**2

    # output
    return volume


def main():
    # I calculate circumference

    # input & output
    print("This program calculates the volume of a cylinder.")
    print("Please enter radius and height.")
    str_radius = input("\nThe radius is (mm): ")
    str_height = input("The height is (mm): ")
    try:
        int_radius = int(str_radius)
        int_height = int(str_height)
        volume = CalculateVolume(int_radius, int_height)
        print(
            "\nThe volume of a cylinder with radius {0} mm and height {1} mm is {2} mm².".format(
                int_radius, int_height, volume
            )
        )
    except Exception:
        print("Invalid Input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
