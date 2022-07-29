"""
Filename: Wonderland Park
Author: Puja Roopesh
Date: 30/6/2022
Description: This program will help staff at the new Wellington theme park recommend safe rides for people based on
their heights.
"""
# importing random and time
import random
import time

# Asking the user what their name is
name_of_staff = input(str("What is your name? ")).strip()

# Pausing the program for 2.5sec
time.sleep(2.5)

# Using the user's name for the introduction of the program
print(f"""
Hi {name_of_staff},this is a program designed to help you provide safe rides for your customers at Wonderland Park. 
For this program will will need to provide the height/s of your customer/s which will be used to determine 
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
# Pausing the program for 2.5sec
time.sleep(2.5)

# Asking the user what the height of their customer is
customer_height = int(input("Please enter your customers height in cm... ").strip())

# Checking if the users height is more than or equal to 150cm
if customer_height >= 150:
    rides = ["Water Twist",  "7 dimension thrill",  "Hyper Coaster", "Extreme Car Race",  "500m Coaster"]
    print(f" The rides that your customer can ride are: {' ,'.join(rides)}")
# Checking if the users height is equal to or more than 140cm but less than 150cm
elif customer_height >= 140 < 150:
    rides = ["Thrilling Tornado", "360 Spin", "Log Land"]
    print(f" The rides that your customer can ride are {' ,'.join(rides)}")
# Checking if the users height is equal to or more than 135cm but less than 140cm
elif customer_height >= 135 < 140:
    rides = ["Family Fun Go Karts", "Lazy River", "VR Fun", "Bumper Cars"]
    print(f" The rides that your customer can ride are {' ,'.join(rides)}")
# Checking if the users height is equal to or more than 120cm but less than 135cm
elif customer_height >= 120 < 135:
    rides = ["Fear Coaster", "PowerDrop", "Ferris wheel"]
    print(f" The rides that your customer can ride are {' ,'.join(rides)}")










