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

Record a speeding offence
- Driver's full name: Must be at least 2 names, exclude numbers, and all characters except 'space' '
- Driver's license number: Two capitalised letters followed by 6 numbers eg (AB123456)
- Posted speed limit: increments of 10 from 30-110
- Driver's recorded speed: Any number above 31 must be greater than the speed limit

Password
- Add a password for information security. Ask for badge number and password.
- Add a number of attempts before exiting programme.


'''


passwords = {
    "pin": "12345",
    "badge_number": "LI123"
    }

def display_login_message():
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
    



if login_confirmation(passwords) == False:
    print("The badge number or password entered is incorrect, access denied.")
else: 
    print("Welcome to the Patrol Infringement Management Programme. \
          This programme...")
    print('''
    1: Record a speeding offence
    2: View all recorded speeding offences
    3: Search offence records
    4: Display patrol summary
    5: Exit programme
''')