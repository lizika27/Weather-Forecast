"""BIU DS17 - Python Project 1 - Weather Forecast.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dZGTjDvS3OyltVyd89ekrZQg5uNrzOYS
"""
import Preferences
import Json_Handle

#set globals()
cityName = None
countryName = None
countryCode = None
continentName = None
continentCode = None
humidity = None
weather = None
localTime = None
locationTime = None

def elementChoice():
    element = None
    while(element != None):
        print("Please choose elements to view:")
        print("1. Name of the city \n2.Name of the country \n 3.Code of the country \n3.Name of the continent \n4.Code of the continent \n5.Humidity \n6.Weather \n7.Local Time \nLocation Time")
        choice = input()

        match choice:
            case 1:
                element += cityName
            case 2:
                element += countryName
            case 3:
                element += countryCode
            case 4:
                element += continentCode
            case 5:
                element += humidity
            case 6:
                element += weather
            case 7:
                element += localTime
            case 8:
                element += locationTime
            case _:
                print("You didnt choose a correct number, please choose again.")
    return element

def elementMenu():
    elements = []
    print("Would you like to add or remove settings? A/R")
    choice = input()
    if (choice == "A" or choice == "a"):
        Json_Handle.loadFromJson(elementChoice(), 'settings.json')
        element = elementChoice()
        elements.insert(element)
        Json_Handle.addToJson(elements, 'settings.json')
    if (choice == 'R' or choice == 'r'):
        elements = Json_Handle.loadFromJson('settings.json')
        element = elementChoice()
        elements.remove(element)
        Json_Handle.removeFromJson(elements, 'settings.json')
    else:
        print("Please choose A (add) or R (Remove).")





def settingsMenu():
    print("Would you like to view the settings? N/Y")
    choice = input()
    if(choice == 'Y' or choice == 'y'):
        elementMenu()
    if(choice =='N' or choice == 'n'):
        return False
    else:
        print("You didnt enter Y (yes) or N (no), application exits.")

def mainMenu():
    print("\nPlease select the next operation from the menu:")
    print("1.View preferences \n2.Change preferences \n3. View defualt city \n4.Change default city") #\n5.Settings")"
    choice = int(input("Choose the desired option number: "))
    match choice:
        case 1:
            preferences =Json_Handle.loadFromJson('preferences.json', 'r')
            print(preferences)
        case 2:
            changePreference()

        case 3:
            defaultCity = Json_Handle.loadFromJson('defaultCity.json', 'r')
            print(defaultCity)
        case 4:
            Preferences.changeDefaultCity()

        #case 5: Future development
            #settingsMenu()
        case _:
            print("No such option has been found, please try again.")


def changePreference():
    print("Please choose a preference to change:")
    print("1.Temperature Unit \n2.Favorite locations")
    choice = int(input("The chosen preference number is: "))
    match choice:
        case 1:
            Preferences.changeDefaultUnit()

        case 2:
            changeFavLocations()

        case _:
            print("No such option has been found, please try again.")

def changeFavLocations():
    print("Please choose an option:")
    print("1.Add \n2.Remove \n3.Display")
    choice = int(input("Select option number: "))
    match choice:
        case 1:
            Preferences.addToFav()
        case 2:
            Preferences.removeFromFav()
        case 3:
            Preferences.displayFavorites()
        case _:
            print("No such option has been found, please try again.")