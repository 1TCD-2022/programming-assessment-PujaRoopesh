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

# randomly getting a number between 2 and 20 to skip the line
def roll_the_dice():
    random_no = random.randint(2, 20)
    return random_no


# Asking the user what their name is
name_of_staff = input(str("What is your name? "))


# Pausing the program for 2.5sec
#time.sleep(2.5)

# Using the user's name for the introduction of the program
print(f"""
Hi {name_of_staff},this is a program designed to help you provide safe rides for your customers at Wonderland Park. 
For this program we will need to provide the height/s of your customer/s which will be used to determine 
which rides they will be able to safely ride on. Once you get your rides you can chose if you would like to 
enter more heights or not. You can do this by entering either "y" or "n" at the end of this program. 
Enjoy!""")

# Pausing the program for 2.5sec
time.sleep(2.5)

# Printing out the names of the rides available at the theme park along with their descriptions
print("""
These are the rides that are available at Wonderland Park...
    1. Fear-coaster (thrilling roller coaster)
    2. PowerDrop (drop 20 stories down to the ground and then back up again )
    3. ferris wheel (calming ride for both children and adults )
    4. bumper cars (electric cars you can ride safely while trying to bump into other riders)
    5. Log-land (This ride lets you ride in a log at be at amazing heights )
    6. Lazy river (A ride for all riders to relax while also having fun )
    7. thrilling-tornado (From a six-story high platform riders are sucked in a tube and then pulled out )
    8. Water-Twist (Ride in a see-through winding tube of water for over 600 feet )
    9. 7-Dimension-Thrill (immersive theatre with 7D thrilling effects for the family to enjoy)
    10. Hyper-coaster (Huge roller coaster with terrific amount of speed)
    11. Family-Fun-Go-Karts (A family friendly racing car activity packed with fun)
    12. VR Fun Zone (full of VR, escape rooms, and even E Sports!)
    13. 360-Spin (One of the most thrilling rides in the park with a full 360 degree rotation)
    14. Extreme-Race-Cars (These fast cars will make you feel like a real F1 driver!)
    15. 500m-coaster(This roller coaster will get you screaming with excitement with an amazing speed and looping tracks)

""")

# Asking the user what the height of their customer is
customer_height = int(input("Please enter your customers height in cm... "))

while customer_height >= 250 or customer_height < 120:
    if customer_height < 120:
        print("There are no rides at this theme park for people under 120cm")
        customer_height = int(input("Please enter your customers height in cm... "))

    elif customer_height >= 250:
        print("There are no rides at this theme park for this height")
        customer_height = int(input("Please enter your customers height in cm... "))

# checking if the customer's height is less than or equal to 135cm
if 100 < customer_height <= 135:
    rides = ["Fear Coaster", "PowerDrop", "Ferris wheel"]
    print(f"Your customer can ride : {', '.join(rides)}")
# checking if the customer's height is less than or equal to 140cm
elif 135 < customer_height <= 140:
    rides = ["Family Fun Go Karts", "Lazy River", "VR Fun", "Bumper Cars"]
    print(f" Your customer can ride : {','.join(rides)}")
# checking if customer's height is less than or equal to 150cm
elif 140 < customer_height <= 150:
    rides = ["Thrilling Tornado", "360 Spin", "Log Land"]
    print(f" Your customer can ride : {','.join(rides)}")
# checking if customer's height is more than 150cm
elif 250 >= customer_height > 150:
    rides = ["Water Twist",  "7 dimension thrill",  "Hyper Coaster", "Extreme Car Race",  "500m Coaster"]
    print(f" Your customer can ride : {','.join(rides)}")



    # Giving the user the position of the customer in the line
if 120 < customer_height <= 250:
    queue_pos = roll_the_dice()
    print(f'\n=> Your Position in the queue is {queue_pos}')
    # Asking the customer if they want to try their luck to first in the line
    try_luck = input("Do you want to try your luck to jump the queue? (Y/N): ")
    # if they chose Y, checking if the customer's new number is less than their original

    if try_luck.upper() == 'Y'or try_luck == 'Yes' or try_luck == 'yes':
        # if true, then they are at the front of the queue

        if roll_the_dice() < queue_pos:
            print("\nYou got lucky today! You are now at the front of the queue")
        # if false, they are still in their original position
        else:
            print(f'\nBetter luck next time... Your position is still... {queue_pos}')
    # printing an outro message if they select N
    elif try_luck.upper() == 'N' or try_luck == 'No' or try_luck == 'no':
        print("Ok, thanks for helping our customers at Wonderland Park! See you next time! ")


