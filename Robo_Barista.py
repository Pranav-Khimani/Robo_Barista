#----------------------------------------------------# P R P O J E C T - 1 #----------------------------------------------------------------#
#-------------------------------------------------------# ROBO BARISTA #--------------------------------------------------------------#

# Hey this is my First project ....
# IN this project the robo barista i made can do the following things : 

# 1 : Greet custromers , ask their name and hand them a menu.
# 2 : The Barista can Blacklisted some unwanted customers and also ask if they did any good deeds.
# 3 : take the input of the thing ordered by our customer .
# 4 : can take order and calculate the price 
# 5 : can know if we have a particular thing on our menu or not .
# 6 : can ask for some custimisation 
# 7 : can ask how man do we need
# 8 : can tell what you ordered
# 9 : can calculate the final order total , etc....

#----------------------------------------___________START_____________--------------------------------------------#
print("Welcome to MV's coffee Shop !!!!")

name = input("what is your name ? \n ")


if name == "kavish" or name == "sagar" or name == "arman":
        pagal_status = input(" are you pagal ? \n")
        good_deeds = input(" How many good deeds you've done today ? \n ")
        if pagal_status == "yes" and good_deeds < "5":
                print(" Get out of here " + name +  " , you will not get served here !")
        elif pagal_status == "no" and good_deeds >= "5":
                print(" Wow you've done some great deeds! Come on in .")

else:
       print(" 0h you are one of the good people !")

    # the word PAGAL means MAD OR EVIL .

print (" hello... " + name + " welcome in !")
      
menu = "espresso \n" + "cappuccino \n" + "latte \n" + "black coffee \n" 

print("What would you like to order ? \n " )

print("Here is our menu : \n " + menu)

order = input()

if order == "latte":
    whipped_status = input(" Would you like it with whipped cream? \n ")
    if whipped_status == "yes": 
        price = 20 
    else: 
        price = 12

elif order == "cappuccino":
    price = 15
elif order == "espresso":
    price = 10      
elif order == "black coffee":
    price = 8
else : 
  print(" Sorry we don't have that here .")
  exit()



print ( " how many " + order + " do you want ? " )
print ("each cup will be " + str(price) + " only !")
quantity =  input ()

total = int(price) * int(quantity)


print ( "okay "+ name + " you ordered " + quantity + " " + order +" and your total will be " + str(total) +  " rupees " + " only !")
print("your order will be ready soon !!!!")
 
 









