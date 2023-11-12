#Dwayne Winn CSI261 week 4 MOVIE GUIDE part 1



#set first three movies in list
m_list = ["Mean Girls", "The Craft","HocusPocus"]


#main fuction 
def main(m_list):
    # call main menu fubction and get command
    c_choice = main_menu(m_list)
    # check command from last function
    while True:
      if c_choice == "list":
        c_list(m_list)
      elif c_choice == "add":
        c_add(m_list)
      elif c_choice == "del":
        c_del(m_list)
      elif c_choice ==  "exit":
        break
      else:
       print("Not a valid command. Please try again.")
       main(m_list) 

  
# Main Menu fuction
def main_menu(m_list):
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
    return m_list

#add movie functions
def c_add(m_list):
   #user input
   movie = input("Movie name: ")
   # add movie to list
   m_list.append(movie)
   print(movie," was added.")
   return m_list
   
 #delete movie functions  
def c_del(m_list):
  #show list
  c_list(m_list)
  n_movie = int(input("Choose movie to delete: :"))
  if n_movie < 1 or n_movie > len(m_list):
    print("Invalid movie number.")
    print()
  else:
    #del movie 
    movie = m_list.pop(n_movie - 1)
    print(movie," was deleted.")
  return m_list

if __name__ == "__main__":
   main(m_list)
  
  

  

     
           
   

