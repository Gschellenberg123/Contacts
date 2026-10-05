#Grae Schellenberg


EMAILREQ = ("@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@mymail.com")
CATAGORYREQ = ["friend", "family", "work", "other"]

#Starter Contacts
contacts = [
    {"name": "Alice"  , "phone": "(245)-865-1523", "email": "Alice@gmail.com"       , "catagory" : "Family"},
    {"name": "Bob"    , "phone": "(785)-378-4189", "email": "Bob@gmail.com"         , "catagory" : "Work"},
    {"name": "Charlie", "phone": "(821)-857-1822", "email": "JSTCE4GTHM@gmail.com"  , "catagory" : "Friend"}
]

def GetContactDetails(Contact):
    """gets all the contacts that are saved"""
    number = 1
    for record in Contact:
            print(f" {number} \n Name: {record['name']} \n Phone: {record['phone']} \n Email: {record['email']} \n Catagory: {record['catagory']} \n")
            print("===================================")
            number += 1

def UpdateContactDetails(Contact, personInt, dictKey, newChoice):
    """used in update to update contact details"""
    Contact[personInt-1][dictKey] = newChoice

def VerifyEmail(email):
    """checks if the provided email ends with the valid email address and returns true if so"""
    #checks if email ends with one of the valid email address
    validation = email.endswith(EMAILREQ)
    
    #returns if its true or not
    return validation
    
def VerifyPhone(phoneNum):
    """check if phone number has enough digits in, it then returns true if it was valid"""
    #keeps count of how many digits there are
    digitCount = 0

    #counts the digits in the phone number
    for char in phoneNum:
        if char.isdigit():
            digitCount += 1

    #if the phone number has 10 digits (US standard) returns true
    if digitCount == 10:
        return True



def ViewContacts(Viewcontact):
    """allows you to view all the contacts by printing each record in the contacts"""

    print("====================================================")
    print("  /``\\  /``\\  |\\  |  ``|``  /``\\  /``\\  ``|``  /``")
    print("  |     |  |  | \\ |    |    |--|  |       |    \\-\\")
    print("  \\__/  \\__/  |  \\|    |    |  |  \\__/    |    __/")
    print("====================================================")

    #prints all the contacts
    GetContactDetails(Viewcontact)

    #returns back to menu
    Display_menu()


def ContactCreator(contact):
    """This creates a contact by asking questions and inputing it into its own dict to add onto the contacts list when its all done"""
    #insures that all inputs are fresh
    name = "Null"
    phoneNum = "Null"
    email = "Null"
    catagory = "Null"

    print("====================================================")
    print("  /``\\  /``\\  |\\  |  ``|``  /``\\  /``\\  ``|``")
    print("  |     |  |  | \\ |    |    |--|  |       |  ")
    print("  \\__/  \\__/  |  \\|    |    |  |  \\__/    |  ")
    print("====================================================")

    #inputs name
    name = input("Name : ")

    #loop for phone number
    while True:
        #input phone number
        numberCheck = input("phone Number: ")

        #Makes proper phone number by removing anything that isnt a digit
        phoneNum = "".join(filter(str.isdigit, numberCheck))

        #checks if the phone number is a valid one
        phoneVerification = VerifyPhone(phoneNum)
        
        #if phone number is valid it breaks the loop
        if phoneVerification == True:
            break
        print("Thats not a valid number Try again")

    #email loop 
    while True:
        #email input
        email = input("email : ")

        #removes spaces in email
        emailCheck = email.replace(" ", "")

        #checks if email is valid
        emailValidated = VerifyEmail(emailCheck)

        #if email is valid break the loop
        if emailValidated == True:
            break
        else:
            print("Thats not a valid gmail Try again")

    #catagory loop
    while True:
        #Catagory input
        catagory = input("Tag (Friend, Family, Work, Other) : ")

        #puts input into lowercase
        catagoryCheck = catagory.lower()

        #if its a valid catagory breaks loop
        if catagoryCheck in CATAGORYREQ :
            break
        else:
            print("thats not a valid tag")            

    #creates new contact
    newContact = {"name": name, "phone": phoneNum, "email": email , "catagory" : catagory}
    #adds new contact
    contact.append(newContact)

    #return message and sends back to menu
    print("New Contact Added . . . Returning to menu")
    Display_menu()

def SearchContact(Contact):
    """this lets you search by inputing a keyword then searches all the contacts and entrys in the contacts for anything
     related to the keyword"""
    print("======================================")
    print("  /```  |```  /``\\  |``\\  /``\\  |  |")
    print("  \\--\\  |--   |--|  |__/  |     |--|")
    print("  ___/  |___  |  |  |  \\  \\__/  |  |")
    print("======================================")
    print("     How would you like to search    ")
    
    #lets you input the keyword for the search
    searchTerm = input("        Keyword: ")
        
    #goes through all the contacts and finds all the contacts that have the keyword anywhere in them
    for entry in Contact:           
        for key, value in entry.items(): 
            if isinstance(value, str) and searchTerm.lower() in value.lower():
                #prints contact with keyword
                print(f"\nName: {entry['name']} \nPhone: {entry['phone']} \nEmail: {entry['email']} \nCatagory: {entry['catagory']} \n")  
                break  
    
    #returns to menu
    Display_menu()



def UpdateContact(Contact):
    """This updates a pre-existing contact by using the contacts list to access 
    the specified contact and modifying one of the entrys"""
    totalContactAmount = len(Contact)
    print("""
  _   _          _      _       
 | | | |_ __  __| |__ _| |_ ___ 
 | |_| | '_ \/ _` / _` |  _/ -_)
  \___/| .__/\__,_\__,_|\__\___|
       |_|                      
""")
    #shows all contacts
    while True:
        GetContactDetails(Contact)
        
        #gets input and checks if its valid
        try:
            updatePerson = int(input("who would you like to update"))
        except:
            continue
        if updatePerson > totalContactAmount or updatePerson < 1:
            print("invalid choice, try again")
        else :
            break

    #choosing what you update and checks if its valid
    while True:
        print("what would you like to update?")
        print("")
        print("1) Name")
        print("2) Number")
        print("3) gmail")
        print("4) catagory")
        try:
            updateChoice = int(input(""))
        except:
            continue
        if updateChoice > 4 or updateChoice < 0:
            print("invalid choice please try again")
        else:
            break
    
    #updates their name
    if updateChoice == 1:
        newName = input("Input New name: ")
        UpdateContactDetails(Contact, updatePerson, "name", newName)

    #updates phone number
    elif updateChoice == 2:
        while True:
            #phone number inputs
            numberCheck = input("Input New number: ")

            #Makes proper phone number by removing anything that isnt a digit
            newNumber = "".join(filter(str.isdigit, numberCheck))

            #checks if the phone number is valid
            phoneVerification = VerifyPhone(newNumber)

            #if phone number is valid breaks loop
            if phoneVerification == True:
                break
            print("Thats not a valid number Try again")
        #updates phone number
        UpdateContactDetails(Contact, updatePerson, "phone", newNumber)

    #updates email address
    elif updateChoice == 3:
        while True:
            #email input
            newEmail = input("Input New email: ")

            #removes spaces
            emailcheck = newEmail.replace(" ", "")

            #check if valid
            emailValidated = VerifyEmail(emailcheck)

            #if valid break loop
            if emailValidated == True:
                break  
        #updates email address
        UpdateContactDetails(Contact, updatePerson, "email", newEmail)

    #updates their catagory
    elif updateChoice == 4:
        while True:
            #Catagory input
            newCatagory = input("Input New catagory: ")

            #puts catagory into lowercase
            catagoryCheck = newCatagory.lower()

            #checks if valid and breaks loop if it is valid
            if catagoryCheck in CATAGORYREQ :
                break
            else:
                print("thats not a valid tag")
        #updates catagory
        UpdateContactDetails(Contact, updatePerson, "catagory", newCatagory)

    #ending message and returns to menu
    print("profile updated . . . returning to menu")
    Display_menu()



def DeleteContact(Contact):
    """Deletes contact by putting number with each dict in the contacts list then deleting the chosen number"""
    while True:
        while True:
            number = 1
            totalAmountOfContacts = len(Contact)
            print("\n\n\n\n")
            print("=================================")
            print(" |``\\  |``  |    |``  ``|``  |``")
            print(" |  |  |--  |    |--    |    |--")
            print(" |__/  |__  |__  |__    |    |__")
            print("=================================\n")

            #shows all contacts
            GetContactDetails(Contact)

            #lets you choose who gets deleted by numbered choices
            print("who's contact do you want to delete")

            #checks if choice is a number
            try:
                deleteChoice = int(input())
            except:
                continue
            break
        #checks if it isnt a valid choice restarts the options otherwise deletes the contact
        if deleteChoice > totalAmountOfContacts or deleteChoice < 1:
            continue
        else:
            del Contact[deleteChoice-1]
            print(f"Contact Deleted")
            Display_menu()
            break


def ContactsByCatagory(contact):
    """This lets you see contacts that have the same catagory you choose"""
    print("What catagory do you want to see?")
    while True:
        #lets you search by catagory
        print("1) Friend")
        print("2) Family")
        print("3) Work")
        print("4) Other")

        #Catagory input
        catagoryChoice = input("")

        #checks if its a valid choice
        try:
            catagoryChoiceInt = int(catagoryChoice)
            if catagoryChoiceInt <= 4 and catagoryChoiceInt >= 1:
                break
            else:
                print("Please input a valid option")
        except:
            print("Please only use number options")

    #if its a valid choice chooses what catagory it is 
    if catagoryChoiceInt == 1:
        chosenOption = "Friend"
    elif catagoryChoiceInt == 2:
        chosenOption = "Family"
    elif catagoryChoiceInt == 3:
        chosenOption = "Work"
    elif catagoryChoiceInt == 4:
        chosenOption = "Other"

    #shows all contacts with matching options
    for record in contact:
        if record['catagory'] == chosenOption:
            print(f" Name: {record['name']} \n Phone: {record['phone']} \n Email: {record['email']} \n Catagory: {record['catagory']} \n")    

    #Returns to menu

    Display_menu()
    
#Goodbye Message
def Exit():
    """exit message """
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("""
   _____                 _ ____             
  / ____|               | |  _ \            
 | |  __  ___   ___   __| | |_) |_   _  ___ 
 | | |_ |/ _ \ / _ \ / _` |  _ <| | | |/ _ \\
 | |__| | (_) | (_) | (_| | |_) | |_| |  __/
  \_____|\___/ \___/ \__,_|____/ \__, |\___|
                                  __/ |     
                                 |___/      
        """)
    

#This Transfers you to your chosen option
def MenuTransfer(optionNum):
    """sends you to your chosen option in display menu"""
    if optionNum == 1:
        ViewContacts(contacts)
    elif optionNum == 2:
        ContactCreator(contacts)
    elif optionNum == 3:
        SearchContact(contacts)
    elif optionNum == 4:
        UpdateContact(contacts)
    elif optionNum == 5:
        DeleteContact(contacts)
    elif optionNum == 6:
        ContactsByCatagory(contacts)
    elif optionNum == 7:
        Exit()

#Menu
def Display_menu():
    """starting menu with all the options"""
    print("        Contact Manager")
    print("================================")
    print(" |\\  /|  |```  |\\  |  |   |")
    print(" | \\/ |  |---  | \\ |  |   |")
    print(" |    |  |___  |  \\|  |___|")
    print("================================")
    print("")
    print("1) View all profiles")
    print("2) Add a new contact")
    print("3) Search for a contact")
    print("4) Update a contact")
    print("5) Delete a contact")
    print("6) View contacts by category")
    print("7) Exit")
    print("")
    try:
        menuOption = int(input("Please input your option (1-7) :"))
    except:
        Display_menu()
    if menuOption > 7 or menuOption < 1:
        Display_menu()
    else:
        MenuTransfer(menuOption)


Display_menu()