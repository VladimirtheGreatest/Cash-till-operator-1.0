#products variables, name and price
banana = float(1.2)
ice = float(2)
cereal = float(3.2)

Product_dictionary =	{
  "banana": 1.2,
  "ice": 2,
  "cereal": 3.2
}


#variables
subtotal_PLU = ("subtotal")
banana_PLU = ("banana")
ice_PLU = ("ice")
cereal_PLU = ("cereal")
immediate_void_PLU = ("void")
quantity_PLU = ("*")
how_many_PLU = ()
user_input = ("") #
PLU_list = [subtotal_PLU, banana_PLU, ice_PLU, cereal_PLU, immediate_void_PLU, quantity_PLU,]
how_many_PLU_list = [1, 2, 3, 4 ,5, 6, 7, 8, 9]
sales_list = []
sales_list_dict = {}

#POS function

def register():
    user_input = ("")
    while user_input!= subtotal_PLU:
        user_input = input("Choose products or press `subtotal`, for quantity press `*`:")  #add items to the basket loop
        if user_input == banana_PLU:
            sales_list.append(banana)
            print("banana", banana, "£")
        elif user_input == ice_PLU:
            sales_list.append(ice)
            print("ice", ice, "£" )
        elif user_input == cereal_PLU:
            sales_list.append(cereal)
            print("cereal", cereal, "£")
        elif user_input not in PLU_list:
            print("no price defined")
        elif user_input == immediate_void_PLU:        #void function
            try:
                print("which product would you like to void")
                input2 = input()
                if input2 == banana_PLU:
                    sales_list.remove(1.2)
                elif input2 == cereal_PLU:
                    sales_list.remove(3.2)
                elif input2 == ice_PLU:
                    sales_list.remove(2)
            except ValueError:
                pass



#quantity function

        elif user_input == quantity_PLU:
            try:
                how_many_PLU = float(input("Choose how many items you want to buy "))
                user_input = input("Choose product:")
                if user_input == banana_PLU:
                    answer = how_many_PLU * Product_dictionary["banana"]
                    sales_list.append(answer)
                    print("added to the list")
                elif user_input == ice_PLU:
                    answer = how_many_PLU * Product_dictionary["ice"]
                    sales_list.append(answer)
                    print("added to the list")
                elif user_input == cereal_PLU:
                    answer = how_many_PLU * Product_dictionary["cereal"]
                    sales_list.append(answer)
                    print("added to the list")
                elif user_input not in PLU_list:
                    print("no price defined")
            except:
                ValueError
                print("you have to choose number for quantity not capital letters!, Try again!!!")
        else:
                for i in sales_list:
                    print(i, "£")
                total_PLU = sum(sales_list)
                print(total_PLU,"£", "subtotal")
                return total_PLU



#initial text for customer, shopping options and navigation  total stored subtotal from the register function
def till_operator():
    product_list = ["banana", "ice", "cereal"]
    print(product_list)
    total = register()
    money_given = float(input("how much money customer gave you?"))
    change = money_given - total
    print("%.2f" % round(change,2), "change back to customer")
    print("Thanks for your shopping!")



till_operator()
