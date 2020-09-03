"""

Project Name: Library Managment System
By:      Ali 
Date:    14.6.2020  
Version:  V.01_14.6.2020 
 
  
   
Last_update: 14.6.2020    
 
  
## Uploaded Parts.

Part-1: No file or code for this part.

Part-2: 
    create DB, connection, Tables, Insert Zero records, create Menus.

    
Part-3:
         
          
"""



import sqlite3, os 

# Create the data-base and name it as LMS.</font> 
db_conn = sqlite3.connect ("LMS.db") 

# set the connection. </font>
c = db_conn.cursor() 



def create_tables_() :
        # to create tables. 
    sql_books =    "CREATE TABLE if not exists books  (b_id INTEGER PRIMARY KEY AUTOINCREMENT, b_name text, b_a_id integer,b_isbn text, b_dop text, b_ed integer)" 
    
    sql_author =   "CREATE TABLE if not exists authors (a_id INTEGER PRIMARY KEY AUTOINCREMENT ,a_ name text, a_email text     )" 
    
    sql_class  = "CREATE TABLE if not exists classifi_list (class_id INTEGER PRIMARY KEY AUTOINCREMENT, class_name text )"  
    
    
    sql_b_class  = "CREATE TABLE if not exists b_class (b_class_id INTEGER PRIMARY KEY AUTOINCREMENT, b_id integer, class_id integer )"  

    sql_sma =      "CREATE TABLE if not exists sma (sma_id INTEGER PRIMARY KEY AUTOINCREMENT, a_id integer,sma_name text, sma_link text)" 
    
    
    c.execute(sql_books) 
    db_conn.commit() 

    c.execute(sql_author) 
    db_conn.commit() 

    c.execute(sql_class)
    db_conn.commit()
        
    c.execute(sql_b_class) 
    db_conn.commit() 

    c.execute(sql_sma) 
    db_conn.commit()  
         
     

    input('\n .. LMS Tables created.. Press any key .. ') 


    
#Function to Insert the Zero Record 
def insert_record_0(): 

    c.execute ("INSERT INTO books (b_id) VALUES(:b_id)",{"b_id":0}) 
    c.execute ("INSERT INTO authors (a_id) VALUES(:a_id)",{"a_id":0}) 
    c.execute ("INSERT INTO classifi_list (class_id) VALUES(:class_id)",{"class_id":0})
    c.execute ("INSERT INTO b_class (class_id) VALUES(:class_id)",{"class_id":0}) 
    c.execute ("INSERT INTO sma (sma_id) VALUES(:sma_id)",{"sma_id":0}) 
    
    db_conn.commit() 
    
    input('\n ...Dummy records been Inserted .... Press any key .. ') 


# we run this one time, so you can remove the # run it then put the # again
#create_tables_() 
#insert_record_0() 
 

def main_menu (): 

    while True :
         
        os.system('clear')
        print('\n   ====== Library Managment System ======')
        print('   1. Books Managment.')
        print('   2. Authors Managment.')
        print('   3. Classification Managment.')      
        print('   4. Search.')
        print('   9. Exit.    ')
        
        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            book_menu() 
            
        elif user_choice == '2' :
            author_menu()
             
        elif user_choice == '3' : 
            class_menu() 
            
        elif user_choice == '4' : 
            search_all() 
            
        elif user_choice == '9' : 
            print('\n\n   You select to exit from the application.\n\n ')
            return 
          
      
     
def book_menu(): 
    
    while True :
        os.system('clear')
        print('\n   ====== LMS - Books Managment ======')
        print('    1. Add New Book.')
        print('    2. Edit a Book information.')
        print('    3. Delete a Book.')
        print('    9. Exit    ')
    
        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            # Function to Add New Book    
            pass
        elif user_choice == '2' : 
            # Function to Edit a Book information.
            pass 
        elif user_choice == '3' : 
            # Function to Delete a Book.
            pass 
         
        elif user_choice == '9' : 
            return 
        
    
    
def author_menu():
    while True :
        os.system('clear')
        print('\n   ====== LMS - Authors Manament ======')
        print('    1. Add New Author.')
        print('    2. Edit an Author information.')
        print('    3. Delete an Author.') 
        print('    9. Exit    ')
        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            # Function to Add New Author    
            pass
        elif user_choice == '2' : 
            # Function to Edit an Author information.
            pass 
        elif user_choice == '3' : 
            # Function to Delete an Author.
            pass 
         
        elif user_choice == '9' : 
            return 
        
    
def class_menu(): 

    while True : 
        os.system('clear')
        print('\n   ====== LMS - Classification Managment ======')
        print('    1. Add New Classification.')
        print('    2. Edit a Classification information.')
        print('    3. Delete a Classification.') 
        print('    9. Exit    ')
        
        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            # Function to Add New Classification   
            pass
        elif user_choice == '2' : 
            # Function to Edit a Classification information.
            pass 
        elif user_choice == '3' : 
            # Function to Delete a Classification.
            pass 
         
        elif user_choice == '9' : 
            return 
         
     
      
      
def search_all(): 
    while True : 
        os.system('clear')
        print('\n   ====== LMS - Searching ======')
        print('    1. Search for Book.')
        print('    2. Search for Author.')
        print('    3. Search for Classification.') 
        print('    9. Exit    ')
        
        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            # Function to Search for Book.   
            pass
        elif user_choice == '2' : 
            # Function to Search for Author.
            pass 
        elif user_choice == '3' : 
            # Function to Search for Classification.
            pass 
         
        elif user_choice == '9' : 
            return 

      
main_menu()       
       
       
       
       
       



