#Dwayne Winn CSI261 week 4 MOVIE GUIDE part 1



#set first three movies in list
m_list = ["Mean Girls", "The Craft","HocusPocus"]


#main fuction 
def main():
    # call main menu fubction and get command
    c_choice = main_menu()
    # check command from last function
    if c_choice == "list":
       c_list(m_list)
    elif c_choice == "add":
       c_add()
    elif c_choice == "del":
       c_del()
    elif c_choice ==  "exit":
       c_exit()
    else:
     print("Not a valid command. Please try again.")
     main_menu()


  
# Main Menu fuction
def main_menu():
    # display main menu
    print("The Movie list Program")
    print()
    print("Command Menu")
    print("list - list all movies")
    print("add - add a movie")
    print("del - delete a movie")
    print("exit - exit program")
    #get user Input 
    c_choice = (input("Command: "))
    return c_choice
     
# List movie functions
def c_list(m_list):
    for i, movie in enumerate(m_list, start = 1):
     print(i,": ",movie)
     print()

#add movie functions
def c_add():
   
   return()
 #delete movie functions 
   
def c_del():
   return main()

def c_exit():
  print("BYE!")
  
if __name__ == "__main__":
   main()

     
           
   

