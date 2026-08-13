'''
Patrol infringement management programme.

The purpose of this programme is to support patrol officers in their work. 
This is done by giving the user inputting the information from the driver who committed a traffic violation.
The programme will then return a ticket for the violation, and store the data for later use.
This programme has multiple different uses; it can record speeding offences, view offences, search offences, and display the patrol summary.


Elliot Guyan
Started - 03/08/2026
Achievement standard 91896
'''

'''
Things to do, ideas, and trialling.

Navigation:
- Record speeding offence
- View all recorded offences
- Search offence records
- Display patrol summary

Record a speeding offence:
- Driver's full name: Must be at least 2 names, exclude numbers, and all characters except 'space' '
- Driver's license number: Two capitalised letters followed by 6 numbers eg (AB123456)
- Posted speed limit: increments of 10 from 30-110
- Driver's recorded speed: Any number above 31 must be greater than the speed limit

Password:
- Add a password for information security. Ask for badge number and password.
- Add a number of attempts before exiting programme.

Double checking inputs:
- Instead of asking after every input, ask at the end, then specifically what was entered incorrectly and give them a direct input back into it.

'''




'''Storing the password of the police officer, enforcing them to enter the programme
via passwords, increasing user safety and the privacy of citizens.'''
passwords = {
    "pin": "12345",
    "badge_number": "LI123"
    } 

'''Storing the driver's with warrants out for their arrest.
Currently holds name and driver's licence'''
arrest_warrants = {
    "Jonathan Ferreria": "JD123456" "921", 
    "Duncan Russell": "LO987656" "71", 
    "Ceejay Daniel": "CG876543" "182",
    "William Harmse": "IT192783" "72",
    "Hadley Olarte": "HT128342" "108",
}


recorded_offences = {}


def display_login_message():
    '''Displays the first of the of the welcome messages.
    This one asks the user to enter their badge number and password 
    before entering the programme. This allows for citizen privacy, as 
    information can be found out about them through this programme.'''

    print("Welcome to the patrol infringement management programme. \
          To enter, please enter your badge number and pin.")

def login_confirmation(passwords):
    '''Checks if the user's password and badge number are real, 
    allowing the safety of citizen information and privacy.'''

    user = input("Please enter your badge number: ")
    pin = input("Please enter your pin: ")
    if user == passwords["badge_number"] and pin == passwords["pin"]:
        return True
    else:
        return False 

def record_offence(driver_licence, driver_name, posted_speed, recorded_speed):
    '''Validate the drivers licence. 2 Letters followed by 6 numbers. Split and combine?'''
    print(f"Recorded offence: \n\n\
  License number: {driver_licence}\n\
  Driver's name:  {driver_name}\n\
  Posted speed:   {posted_speed}\n\
  Recorded speed: {recorded_speed}\n")
    

'''def calculate_fine(recorded_speed, posted_speed):
    speeding = recorded_speed - posted_speed
    if speeding > 0:
        print(f"Driver is going {speeding} over the speed limit the fine is")
    else:
        print("The driver is going at or under the speed limit.")'''


def speeding_fine(recorded_speed, posted_speed):
    speeding = recorded_speed - posted_speed
    if speeding > 0:
        print(f"Driver is going {speeding} over the speed limit the fine is")
    else:
        print("The driver is going at or under the speed limit.")



#def view_all_offences():


#def search_offence_records():


#def display_patrol_summary():


#---------------------------- Main Programme -------------------------------#
        

if login_confirmation(passwords) == False:
    '''Checks if the login which the user has given is valid or not.
    If the user login is not valid, it will reject them and close the programme. 
    If the user login is valid it will continue on into the programme.'''

    print("The badge number or password entered is incorrect, access denied.")
else: 
    print("Welcome to the Patrol Infringement Management Programme.\n\
This programme...")
    
    print('''
    1: Record a speeding offence
    2: View all recorded speeding offences
    3: Search offence records
    4: Display patrol summary
    5: Exit programme
''')
    
user_choice = input("Please enter the number corresponding to your requirements: ")
'''Allows the user to decide what they want to do. Whether it is to record a
speed offence, search the records, or display the patrol summary.'''

while user_choice != "5":
    if user_choice == "1":
        #driver_licence = input("Please enter the driver's licence number: ")
        #driver_name = input("Please enter the driver's full name: ")
        posted_speed = int(input("Please enter the posted speed limit: "))
        recorded_speed = int(input("Please enter the recorded speed of the driver: "))
        #record_offence(driver_licence, driver_name, posted_speed, recorded_speed)
        speeding_fine(posted_speed, recorded_speed)

    elif user_choice == "2":
        print("")
    elif user_choice == "3":
        print("")
    elif user_choice == "4":
        print()

    else:
        print("Please enter a valid option between 1 and 5.")
    
        user_choice = input("Please enter the number corresponding to your requirements: ")

