# Cash till operator 1.0 this is the very first version without GUI

Product_dictionary =	{
  "banana": 1.19,
  "ice": 2,
  "cereal": 3.19
}


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


def register():
    user_input = ("")
    while user_input!= subtotal_PLU:
      user_input = input("Choose product from the list:")
      if user_input in Product_dictionary:
        variable = Product_dictionary[user_input]
        sales_list.append(variable)
        print("Your basket")
        for i in sales_list:
          print(i, "£")
      elif user_input not in Product_dictionary and user_input!=subtotal_PLU and user_input!=quantity_PLU and user_input!=immediate_void_PLU:
          print("not found, sorry!")
      elif user_input == immediate_void_PLU:
        user_input = input("Choose product to void:")
        if user_input in Product_dictionary:
          variable = Product_dictionary[user_input]
          sales_list.remove(variable)
          print("Your basket")
          for i in sales_list:
            print(i, "£")
          print("-", variable, "£ voided" )
        else:
          print("I am sorry I cant void this, it is not in the sales list!")


      elif user_input == quantity_PLU:
        try:
          how_many_PLU = float(input("Choose how many items you want to buy "))
          user_input = input("Choose product:")
          if user_input in Product_dictionary:
            variable = Product_dictionary[user_input]
            sales_list.append(round(variable * how_many_PLU))
            print("Your basket")
            for i in sales_list:
              print(i, "£")
          else:
            print("Product not found")
        except:
          ValueError
          print("you have to choose number for quantity not capital letters!, Try again!!!")

      else:
        for i in sales_list:
          print(i, "£")
        total_PLU = round(sum(sales_list))
        print(total_PLU, "£", "subtotal")
        return total_PLU

def till_operator():
  product_list = ["banana", "ice", "cereal"]
  print(product_list)
  total = register()
  money_given = float(input("how much money customer gave you?"))
  change = money_given - total
  print("%.2f" % round(change,2), "change back to customer")
  print("ready to scan")
  till_operator()


till_operator()
