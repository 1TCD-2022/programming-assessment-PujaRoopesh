"""
Filename: Wonderland Park
Author: Puja Roopesh
Date: 2/7/2022
Description: This program will help staff at the new Wellington theme park recommend safe rides for people based on
their heights.
"""
# importing random and time
import random
import time


def roll_the_dice():
    # randomly getting a number between 2 and 20 to skip the line
    random_no = random.randint(2, 20)
    return random_no


def wonderland_park():
    # This function is to determine the rides allowed for the customer based on height

    # Asking the user what their name is and validating their name
    count_of_attempts = 0
    name_of_staff = input("=> What is your name? ").strip()

    while not name_of_staff.replace(" ", "").isalpha():
        count_of_attempts += 1
        name_of_staff = input("Please enter your name (no special characters allowed or numerical names allowed!): ")

        if count_of_attempts == 2 and not name_of_staff.replace(" ", "").isalpha():
            print(">>> Too many invalid attempts...quitting!")
            quit()

    # Pausing the program for 1.5sec
    time.sleep(1.5)

    # Using the user's name for the introduction of the program
    print(f"""
    Hi {name_of_staff}, this program is designed to help you provide safe rides for your customers at Wonderland Park!
    Just provide the customer's height to find out what rides they are able to ride safely.
    Enjoy!""")

    # Pausing the program for 5sec
    time.sleep(5.0)
    # designing the menu for the rides available
    print('-' * 130)

    # Printing out the names of the rides available at the theme park along with their descriptions
    print("""
    These are the rides that are available at Wonderland Park...
        1. Fear-Coaster (thrilling roller coaster)
        2. PowerDrop (drop 20 stories down to the ground and then back up again )
        3. Ferris Wheel (calming ride for both children and adults )
        4. Bumper Cars (electric cars you can ride safely while trying to bump into other riders)
        5. Log-land (This ride lets you ride in a log at be at amazing heights )
        6. Lazy river (A ride for all riders to relax while also having fun )
        7. Thrilling-Tornado (From a six-story high platform riders are sucked in a tube and then pulled out )
        8. Water-Twist (Ride in a see-through winding tube of water for over 600 feet )
        9. 7-Dimension-Thrill (immersive theatre with 7D thrilling effects for the family to enjoy)
        10. Hyper-Coaster (Huge roller coaster with terrific amount of speed)
        11. Family-Fun-Go-Karts (A family friendly racing car activity packed with fun)
        12. VR Fun Zone (full of VR, escape rooms, and even E Sports!)
        13. 360-Spin (One of the most thrilling rides in the park with a full 360 degree rotation)
        14. Extreme-Race-Cars (These fast cars will make you feel like a real F1 driver!)
        15. 500m-Coaster(This roller coaster will get you screaming with excitement with an amazing speed and looping tracks)
    """)
    # designing the menu for the rides available
    # print('-' * 130)

    # Asking the user for their customer's height and validating it
    count_of_attempts = 0
    customer_height = 0
    valid_height = False

    while not valid_height and count_of_attempts < 3:
        try:
            if count_of_attempts == 0:
                customer_height = float(input("=> Please enter customer's height in cm [min:120, max:250]: ").strip())
            else:
                customer_height = float(input("=> Please enter a valid customer height in cm [min:120, max:250]: ").strip())

            if 120 <= customer_height <= 250:
                valid_height = True
            else:
                valid_height = False
                count_of_attempts += 1

                if count_of_attempts == 3:
                    print('*' * 40)
                    print(">>> Too many invalid attempts..quitting!")
                    print('*' * 40)
                    quit()

        except ValueError:
            count_of_attempts += 1
            valid_height = False
            if count_of_attempts == 3:
                print('*' * 40)
                print(">>> Too many invalid attempts..quitting!")
                print('*' * 40)
                quit()

    MIN_HEIGHT = 120
    MAX_HEIGHT = 250
    # checking if the customer's height is more than 120 but less than or equal to 135cm
    print('*' * 150)
    if MIN_HEIGHT <= customer_height <= 135:
        rides = ["Fear Coaster", "PowerDrop", "Ferris wheel"]
        print(f" Customer can ride : *****> {', '.join(rides)}")
    # checking if the customer's height is more than 135 but less than or equal to 140cm
    elif 135 < customer_height <= 140:
        rides = ["Family Fun Go Karts", "Lazy River", "VR Fun", "Bumper Cars"]
        print(f" Customer can ride : *****> {','.join(rides)}")
    # checking if customer's height is more than 140 but less than or equal to 150cm
    elif 140 < customer_height <= 150:
        rides = ["Thrilling Tornado", "360 Spin", "Log Land"]
        print(f" Customer can ride : *****> {','.join(rides)}")
    # checking if customer's height is more than 150cm
    elif MAX_HEIGHT >= customer_height > 150:
        rides = ["Water Twist", "7 Dimension Thrill", "Hyper Coaster", "Extreme Car Race", "500m Coaster""\n \t *****> "
                   "Fear Coaster", "PowerDrop", "Ferris Wheel", "Family Fun Go Karts", "Lazy River""\n \t *****> "
                   "VR Fun", "Bumper Cars", "Thrilling Tornado", "360 Spin", "Log Land"]
        print(f" Customer can ride all the rides at Wonderland Park! : \n \n \t *****> {','.join(rides)} " )
    print('*' * 150)

    # Giving the user a position in the queue
    if customer_height >= MIN_HEIGHT or customer_height <= MAX_HEIGHT:
        queue_pos = roll_the_dice()
        print(f"\n>>> Your customer's position in the queue is {queue_pos}")
        # Asking the customer if they want to try their luck to first in the line
        try_luck = input("=> Does your customer want to try their luck to jump the queue? (Y/N): ")

        # validating the user's input
        count_of_tries = 0
        while try_luck.upper() not in ('Y', 'YES', 'N', 'NO') and count_of_tries < 2:
            print("=> Please enter either Y or N! ")
            try_luck = input("=> Do you want to try your luck to jump the queue? (Y/N): ")
            count_of_tries += 1
            # quitting the program if there are too many invalid attempts
            if count_of_tries == 2 and try_luck.upper() not in ('Y', 'YES', 'N', 'NO'):
                print('*' * 40)
                print("=> Too many invalid attempts..quitting!")
                print('*' * 40)
                quit()

        # if they chose Y, checking if the customer's new number is less than their original
        if try_luck.upper() in ('Y', 'YES'):
            if roll_the_dice() < queue_pos:
                # if true, then they are at the front of the queue
                print("\n>>> Your customer got lucky..in front of the queue now :)")
            # if false, they are still in their original position
            else:
                print(f"\n>>> Better luck next time... Your customer's position is still... {queue_pos}")
        # printing an outro message if they select N
        elif try_luck.upper() in ('N', 'NO'):
            print(">>> Thanks for helping our customers at Wonderland Park! See you next time! ")
            print(f">>> Your customer's position in the queue is still {queue_pos}")


def main():
    # Calling the function to determine customer rides allowed based on height
    wonderland_park()

    # Repeat the program when there is another customer
    while True:
        new_customer = str(input("\n=> Would you like to move to the next customer? Y/N : "))
        counter = 1
        while new_customer.upper() not in ('Y', 'YES', 'N', 'NO') and counter < 3:
            print(">>> Please enter either Y or N! ")
            new_customer = str(input("\n=> Would you like to move to the next customer? Y/N : "))
            counter += 1
            if counter == 3 and new_customer.upper() not in ('Y', 'YES', 'N', 'NO'):
                print('*' * 40)
                print(">>> Too many invalid attempts..quitting!")
                print('*' * 40)
                quit()
        # if they enter Y restarting the program
        if new_customer.upper() in ('Y', 'YES'):
            wonderland_park()
        # if the customer enters N, printing an outro message
        elif new_customer.upper() in ('N', 'NO'):
            print(">>> Ok, thanks for helping our customers at Wonderland Park! See you next time! ")
            exit()


# Start the program
main()



