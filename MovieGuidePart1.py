#Dwayne Winn CSI261 week 4 MOVIE GUIDE part 1


  

def main_menu():
   print("The Movie list Program")
   print()
   print("Command Menu")
   print("list - list all movies")
   print("add - add a movie")
   print("del - delete a movie")
   print("exit - exit program")
   c_choice = (input("Command: "))
   if c_choice == "list":
       c_list()
   elif c_choice == "add":
       c_add()
   elif c_choice == "del":
       c_del()
   elif c_choice ==  "exit":
       e_exit()
   else:
     print("Not a valid command. Please try again.")
     
def c_list():
   return main_menu()



def c_add():
   return main_menu()
def c_del():
   return main_menu()

def c_exit():
  print("BYE!")
  END

main_menu()

     
           
   

