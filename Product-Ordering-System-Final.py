from tkinter import *
from tkinter import messagebox
import pygame, os

#Finds out if number is an integer By Jerry Han
def findTextValue(textMessage):
    inputValue = textMessage.get("1.0", END)
    
    try:
        x = int(inputValue)
        return x
    except ValueError:
        messagebox.showinfo("Error", "Please enter an integer")

def checkCompletion(choice):
    string = ""
    completion = []
    
    if choice == pickup:
        if len(pickupName.get("1.0", END)) < 1:
            completion.append("name")
        
        if len(pickupPhoneNumber.get("1.0", END)) != 10:
            completion.append("number")
        else:
            try:
                g = int(pickupPhoneNumber.get("1.0", END))
        
            except ValueError:
                completion.append("number")
        
        if (locationChoices.get() != "Vancouver") and (locationChoices.get() !=  "Langley") and (locationChoices.get() != "Burnaby") and (locationChoices.get() != "White Rock") and (locationChoices.get() != "Surrey"):
            completion.append("location")
    
    if choice == delivery:
        if len(deliveryName.get("1.0", END)) < 1:
            completion.append("name")
                
        if len(deliveryPhoneNumber.get("1.0", END)) != 10:
            completion.append("number")
        
        else:
            try:
                g = int(deliveryPhoneNumber.get("1.0", END))
        
            except ValueError:
                completion.append("number")

        if len(deliveryAddress.get("1.0", END)) < 1:
            completion.append("address")    
    
    for i in range(0, (len(completion) - 1)):
        if completion[i] == "name":
            string = string + "Please enter your name\n"
        elif completion[i] == "number":
            string = string + "Please enter a valid phone number in the form 1234567890\n"
        elif completion[i] == "location":
            string = string + "Please select a location\n"
        elif completion[i] == "address":
            string = string + "Please enter your address\n"
        
    if string != "":
        messagebox.showinfo("Error", "Please complete the following:\n" + string)
    else:
        return 0
    
#Displays order By Jerry Han
def addToOrder(message):
    global smallChocolate1, mediumChocolate1, largeChocolate1, smallChocolate2, mediumChocolate2, largeChocolate2, smallChocolate3, mediumChocolate3, largeChocolate3, cost
    
    #Gets the selected choice from dropdown menu
    option1Choice = size1Choices.get()
    option2Choice = size2Choices.get()
    option3Choice = size3Choices.get()
    
    #Tests if user entered a valid number, then adds number to order
    if findTextValue(message):
        #If the choice is chocolate 1
        if message == chocolate1:
            if option1Choice == "Small(200g, $6.99)":
                smallChocolate1 += findTextValue(message)
                cost += 6.99 * findTextValue(message)
            if option1Choice == "Medium(400g, $10.99)":
                mediumChocolate1 += int(findTextValue(message))
                cost += 10.99 * findTextValue(message)
            if option1Choice == "Large(800g, $18.99)":
                largeChocolate1 += int(findTextValue(message))
                cost += 18.99 * findTextValue(message)
        
        if message == chocolate2:
            if option2Choice == "Small(200g, $6.99)":
                smallChocolate2 += int(findTextValue(message))
                cost += 6.99 * findTextValue(message)
            if option2Choice == "Medium(400g, $10.99)":
                mediumChocolate2 += int(findTextValue(message))
                cost += 10.99 * findTextValue(message)
            if option2Choice == "Large(800g, $18.99)":
                largeChocolate2 += int(findTextValue(message))
                cost += 18.99 * findTextValue(message)
                
        if message == chocolate3:
            if option3Choice == "Small(200g, $6.99)":
                smallChocolate3 += int(findTextValue(message))
                cost += 6.99 * findTextValue(message)
            if option3Choice == "Medium(400g, $10.99)":
                mediumChocolate3 += int(findTextValue(message))
                cost += 10.99 * findTextValue(message)
            if option3Choice == "Large(800g, $18.99)":
                largeChocolate3 += int(findTextValue(message))
                cost += 18.99 * findTextValue(message)
         
         #Doesn't let amount of chocolate ordered go into negative
        if smallChocolate1 < 0:
            smallChocolate1 = 0
        if mediumChocolate1 < 0:
            mediumChocolate1 = 0
        if largeChocolate1 < 0:
            largeChocolate1 = 0      
        if smallChocolate2 < 0:
            smallChocolate2 = 0
        if mediumChocolate2 < 0:
            mediumChocolate2 = 0
        if largeChocolate2 < 0:
            largeChocolate2 = 0
        if smallChocolate3 < 0:
            smallChocolate3 = 0
        if mediumChocolate3 < 0:
            mediumChocolate3 = 0
        if largeChocolate3 < 0:
            largeChocolate3 = 0
        
        global chocolateAmount
        chocolateAmount = [smallChocolate1, mediumChocolate1, largeChocolate1, smallChocolate2, mediumChocolate2, largeChocolate2, smallChocolate3, mediumChocolate3, largeChocolate3, cost]

#Writes the user's order to a text file By Jerry Han
def submit(choice):
    if choice == pickup:
            fileD = open("orders.txt", "w")
            fileD.write("Name:\n")
            fileD.write("%s\n" % pickupName.get("1.0", END))
            fileD.write("Phone Number:\n")
            fileD.write("%s\n" % pickupPhoneNumber.get("1.0", END))
            fileD.write("Location of Pickup:\n")
            fileD.write("%s\n\n" % locationChoices.get())
            
            for i in range(0, (len(chocolateAmount) - 1)):
                if chocolateAmount[i] > 0:
                    string = chocolateAndCost[i] + ":   " + str(chocolateAmount[i]) + "\n"
                    fileD.write(string)
                
            fileD.close()
            confirmWindow.destroy()
            
            messagebox.showinfo("Success", "Your order has been processed.")
    
    if choice == delivery:
            fileD = open("orders.txt", "w")
            fileD.write("Name:\n")
            fileD.write("%s\n" % deliveryName.get("1.0", END))
            fileD.write("Phone Number:\n")
            fileD.write("%s\n" % deliveryPhoneNumber.get("1.0", END))
            fileD.write("Address:\n")
            fileD.write("%s\n" % deliveryAddress.get("1.0", END))
            fileD.write("Apartment Number(if applicable):\n")
            fileD.write("%s\n" % aptNumber.get("1.0", END))
            
            for i in range(0, (len(chocolateAmount))):
                if chocolateAmount[i] > 0:
                    string = chocolateAndCost[i] + ":   " + str(chocolateAmount[i]) + "\n"
                    fileD.write(string)
                    
            fileD.close()
            confirmWindow.destroy()

            messagebox.showinfo("Success", "Your order has been processed.")

#Lets user choose if they want to pickup their order or have it delivered By Jerry Han
def pickupOrDelivery():
    var.get()
    option = var.get()
    
    if (option != "pickup") and (option != "delivery"):
        messagebox.showinfo("Error", "Please select a delivery option")
        return 0

    global confirmWindow
    confirmWindow = Toplevel(app)
    confirmWindow.geometry("900x700+100+200")
    confirmWindow.title("Confirm Order")
    confirmWindow.resizable(0, 0)
    
    #Depending on the choice picked, it asks for either which location they would like to pick it up
    #or where would they like it to be sent By Jerry Han    
    if option == "pickup":
        global pickupName, pickupPhoneNumber, location
        
        Label(confirmWindow, text = "Name for Pickup").place(relx = 0.1, rely = 0.05)
        pickupName = Text(confirmWindow, height = 1, width = 20)
        pickupName.place(relx = 0.1, rely = 0.1)
        
        Label(confirmWindow, text = "Phone number").place(relx = 0.1, rely = 0.15)
        pickupPhoneNumber = Text(confirmWindow, height = 1, width = 15)
        pickupPhoneNumber.place(relx = 0.1, rely = 0.2)
        
        Label(confirmWindow, text = "Choose your location").place(relx = 0.1, rely = 0.25)
        location = OptionMenu(confirmWindow, locationChoices, *locations)
        location.place(relx = 0.1, rely = 0.3)
        
        Label(confirmWindow, text = "\n\n\n\nPlease review your order.").place(relx = 0.1, rely = 0.35)

        confirmButton = Button(confirmWindow, text = "Confirm Order", command = lambda: submit(pickup))
        confirmButton.place(relx = 0.7, rely = 0.4)
        app.withdraw()
        
    elif option == "delivery":
        global deliveryName, deliveryPhoneNumber, deliveryAddress, aptNumber
        
        Label(confirmWindow, text = "Full Name").place(relx = 0.1, rely = 0.05)
        deliveryName = Text(confirmWindow, height = 1, width = 20)
        deliveryName.place(relx = 0.1, rely = 0.1)
        
        Label(confirmWindow, text = "Phone number").place(relx = 0.1, rely = 0.15)
        deliveryPhoneNumber = Text(confirmWindow, height = 1, width = 15)
        deliveryPhoneNumber.place(relx = 0.1, rely = 0.2)
        
        Label(confirmWindow, text = "Mailing Address").place(relx = 0.1, rely = 0.25)
        deliveryAddress = Text(confirmWindow, height = 1, width = 30)
        deliveryAddress.place(relx = 0.1, rely = 0.3)
        
        Label(confirmWindow, text = "Apartment Number(if applicable)").place(relx = 0.1, rely = 0.35)
        aptNumber = Text(confirmWindow, height = 1, width = 8)
        aptNumber.place(relx = 0.1, rely = 0.4)
        
        Label(confirmWindow, text = "Please review your order.").place(relx = 0.1, rely = 0.5)
        
        confirmButton = Button(confirmWindow, text = "Confirm Order", command = lambda: submit(delivery))
        confirmButton.place(relx = 0.7, rely = 0.6)
        app.withdraw()
    
    #displays order so user can review, but must use main window to make changes By Jerry Li
    y = 0.55
    for i in range(0, len(chocolateAmount)):
        if chocolateAmount[i] > 0:
            displayText = chocolateAndCost[i] + ":  " + str(chocolateAmount[i])
            Label(confirmWindow, text = displayText).place(relx = 0.1, rely = y)
            y += 0.05

WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)

smallChocolate1 = 0
mediumChocolate1 = 0
largeChocolate1 = 0
smallChocolate2 = 0
mediumChocolate2 = 0
largeChocolate2 = 0
smallChocolate3 = 0
mediumChocolate3 = 0
largeChocolate3 = 0
cost = 0

sizeList = ["Small(200g, $6.99)", "Medium(400g, $10.99)", "Large(800g, $18.99)"]
locations = ["Vancouver", "Langley", "Burnaby", "White Rock", "Surrey"]
chocolateAndCost = ["Small box of Hedgehogs", "Medium box of Hedgehogs", "Large box of Hedgehogs", "Small box of Ferreros", "Medium box of Ferreros", "Large box of Ferreros", "Small box of white chocolate bars", "Medium box of white chocolate bars", "Large box of white chocolate bars", "Cost"]

app = Tk()
app.title("Tirion's Sweets")
app.geometry('1500x800+200+100')
app.resizable(0,0)
app.config(background = "gold")

#Code to use pygame window in tkinter By Jerry Han
embed = Frame(app, width = 500, height = 400)
embed.place(relx = 0.7, rely = 0.4)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

#tkinter page formatting all By Jerry Li
pygame.init()
mainClock = pygame.time.Clock()
size = (500, 400)
screen = pygame.display.set_mode(size)

var = StringVar()

optionsVar = StringVar(app)

TITLE = Label(app, text = "Tirion's", bg = "orange")
TITLE.place(relx = 0.3, rely = 0.04)
TITLE.config(font = ("Comic Sans", 33))

TITLE2 = Label(app, text = " Sweets", bg = "orange")
TITLE2.place(relx = 0.48, rely = 0.04)
TITLE2.config(font = ("fixedsys", 30))

size1Choices = StringVar()
size1Choices.set("Please choose the size of the box")
size2Choices = StringVar()
size2Choices.set("Please choose the size of the box")
size3Choices = StringVar()
size3Choices.set("Please choose the size of the box")

locationChoices = StringVar()
locationChoices.set("Please choose which store you would like to pickup your order from")

button = Button(app, text = "Submit", command = pickupOrDelivery).place(relx = 0.82, rely = 0.82)

#Size of box of chocoaltes By Jerry Li
option1 = OptionMenu(app, size1Choices, *sizeList) 
option1.place(rely = 0.17, relx = 0.35)

option2 = OptionMenu(app, size2Choices, *sizeList) 
option2.place(rely = 0.42, relx = 0.35)

option3 = OptionMenu(app, size3Choices, *sizeList) 
option3.place(rely = 0.67, relx = 0.35)

#add button for textboxes 1, 2, and 3 By Jerry Li
addButton1 = Button(app, text = "Add", command = lambda: addToOrder(chocolate1))
addButton1.place(relx = 0.35, rely = 0.3)

addButton2 = Button(app, text = "Add", command = lambda: addToOrder(chocolate2))
addButton2.place(relx = 0.35, rely = 0.55)

addButton3 = Button(app, text = "Add", command = lambda: addToOrder(chocolate3))
addButton3.place(relx = 0.35, rely = 0.8)

#Text to put in amount of boxes user wishes to buy By Jerry Li
sizel1 = Label(app, text = "Amount of boxes:", bg = "gold")
sizel1.place(relx = 0.35, rely = 0.25)
chocolate1 = Text(app, height = 1, width = 10)
chocolate1.place(relx = 0.5, rely = 0.25)

sizel2 = Label(app, text = "Amount of boxes:", bg = "gold")
sizel2.place(relx = 0.35, rely = 0.5)
chocolate2 = Text(app, height = 1, width = 10)
chocolate2.place(relx = 0.5, rely = 0.5)

sizel3 = Label(app, text = "Amount of boxes:", bg = "gold")
sizel3.place(relx = 0.35, rely = 0.75)
chocolate3 = Text(app, height = 1, width = 10)
chocolate3.place(relx = 0.5, rely = 0.75)

#radiobuttons delivery/pickup By Jerry Li
var = StringVar()
var.set(None)
pickup = Radiobutton(app, text = "Pickup", value = "pickup", variable = var, bg = "gold")
pickup.place(relx = 0.75, rely = 0.75)
delivery = Radiobutton(app, text = "Delivery", value = "delivery", variable = var, bg = "gold")
delivery.place(relx = 0.85, rely = 0.75)

x = 10

side_title = Label(app, text = "Shopping Cart", bg = "orange")
side_title.place(relx = 0.72, rely = 0.3)
side_title.config(font = ("Comic Sans", 20))

#photo example
photo1 = PhotoImage(file = "hedgehog.png")
photo1Label = Label(app, image = photo1, bd = 3, relief = "solid")
photo1Label.image = photo1
photo1Label.place(rely = 0.15, relx = 0.1)

photo2 = PhotoImage(file = "ferrero.png")
photo2Label = Label(app, image = photo2, bd = 3, relief = "solid")
photo2Label.image = photo2
photo2Label.place(rely = 0.41, relx = 0.1)

photo3 = PhotoImage(file = "whiteChocolate.png")
photo3Label = Label(app, image = photo3, bd = 3, relief = "solid")
photo3Label.image = photo3
photo3Label.place(rely = 0.67, relx = 0.1)

logo = PhotoImage(file = "logo.png")
logoLabel = Label(app, image = logo, bd = 3, relief = "solid")
logoLabel.image = logo
logoLabel.place(rely = 0.04, relx = 0.75)

#pygame loop that displays and manages what the user ordered and how much it costs By Jerry Han
while True:
    screen.fill(GOLD)
       
    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Small box of Hedgehogs: " + str(smallChocolate1), 1, BLACK)
    screen.blit(orderText, (0, 0))

    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Medium box of Hedgehogs: " + str(mediumChocolate1), 1, BLACK)
    screen.blit(orderText, (0, 25))

    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Large box of Hedgehogs: " + str(largeChocolate1), 1, BLACK)
    screen.blit(orderText, (0, 50))

    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Small box of Ferreros: " + str(smallChocolate2), 1, BLACK)
    screen.blit(orderText, (0, 75))
            
    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Medium box of Ferreros: " + str(mediumChocolate2), 1, BLACK)
    screen.blit(orderText, (0, 100))
            
    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Large box of Ferreros: " + str(largeChocolate2), 1, BLACK)
    screen.blit(orderText, (0, 125))
            
    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Small box of white chocolate bars: " + str(smallChocolate3), 1, BLACK)
    screen.blit(orderText, (0, 150))
            
    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Medium box of white chocolate bars: " + str(mediumChocolate3), 1, BLACK)
    screen.blit(orderText, (0, 175))

    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Large box of white chocolate bars: " + str(largeChocolate3), 1, BLACK)
    screen.blit(orderText, (0, 200))
    
    font = pygame.font.SysFont("Arial", 25)
    orderText = font.render("Cost: " + str(cost), 1, BLACK)
    screen.blit(orderText, (0, 225))
            
    #pygame.display.update()
    mainClock.tick(3)
    app.update()
    
app.mainloop()