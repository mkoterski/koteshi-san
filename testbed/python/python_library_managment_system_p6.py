


"""

Project Name: Library Managment System
By:      Ali 
Date:    14.6.2020  
Version:  V.01_14.6.2020 
 
  
   
Last_update: 14.6.2020    
 
  
## Uploaded Parts.

Part-1: No codes in this part

Part-2: 
    Create DB, DB Connection, Create Tables, Insert Zero records, Create Menus.

    
    
Part-3:
    Writing Codes for :
        classification Managment: [Add New, Edit, delete and Show Classifications]     
    

Part-4:
    Writing Codes for :
        Authors Managment: [Add New, Edit, delete and Show Authors] 
        with Author we Add, Edit and Delete the SMA Social Media Accounts for the 
        Author.
        
            
part-5:
    Writing Codes for :
        Book Managment: [Add New, Edit, delete and Show Books] 
        
        Update on show_Author, Edit_author, Delete_author and new_authors 
        Update on Show_classification, Edit Classification, Delete Classification
        
        
    
Part-6:     
    lib_info function: Function to printout some information or statistics about the library 
        such as : (Statistics about Books, Authors and Clasifications)
            Sample ..
            # Number of book in the lib 
            # books  without classifications 
            # Books without Author
            # Books without ISBN 
            # Books under each classification 
            # Authors 
            # Classifivations     
    
        
        

Enhancement: Version 02.         
        + Using regex Validation 
        + validation on:
            Email [xxx@xx.xx], ISBN, Date [dd-mm-yyyy]    
                
        + Delete Function: If we delete a classification, we need to delete any links with that classifications
          in table b_class. Check same action for all Delete functions in the system     
        
        + Add personal Book numbering.
        	
        + Add Books from more than one libraries. (multiple Library )            
"""



import sqlite3, os 

# Create the data-base and name it as LMS.</font> 
db_conn = sqlite3.connect ("LMS.db") 

# set the connection. </font>
c = db_conn.cursor() 



def create_tables_() :
        # to create tables. 
    sql_books =    "CREATE TABLE if not exists books  (b_id INTEGER PRIMARY KEY AUTOINCREMENT, b_name text, b_a_id integer,b_isbn text, b_dop text, b_ed integer)" 
    
    sql_author =   "CREATE TABLE if not exists authors (a_id INTEGER PRIMARY KEY AUTOINCREMENT ,a_name text, a_email text, has_sma  )" 
    
    sql_class  = "CREATE TABLE if not exists classifi_list (class_l_id INTEGER PRIMARY KEY AUTOINCREMENT, class_name text )"  
    
    
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
    c.execute ("INSERT INTO classifi_list (class_l_id) VALUES(:class_l_id)",{"class_l_id":0}) 
    
    c.execute ("INSERT INTO b_class (b_class_id) VALUES(:b_class_id)",{"b_class_id":0}) 
    c.execute ("INSERT INTO sma (sma_id) VALUES(:sma_id)",{"sma_id":0}) 
        
    db_conn.commit() 
    
    input('\n ...Dummy records been Inserted .... Press any key .. ') 


 

def main_menu (): 

    while True : 
        os.system('clear')
        print('\n   ====== Library Managment System ======')
        print('   1. Books Managment.')
        print('   2. Authors Managment.')
        print('   3. Classification Managment.')      
        print('   4. Search.') 
        print('   5. Library Information.')
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
            
        elif user_choice == '5' : 
            lib_info() 
            
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
        print('    4. Show Books.')
        print('    9. Exit.    ')
    
        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            # Function to Add New Book    
            new_book ()
        elif user_choice == '2' : 
            # Function to Edit a Book information.
            edit_book()
        elif user_choice == '3' : 
            # Function to Delete a Book.
            delete_book()
        elif user_choice == '4' : 
            # Function to show the Books.
            show_books() 
         
        elif user_choice == '9' : 
            return 
        
    
    
def author_menu():
    while True :
        os.system('clear')
        print('\n   ====== LMS - Authors Manament ======')
        print('    1. Add New Author.')
        print('    2. Edit Authors information.')
        print('    3. Delete Authors.')
        print('    4. Show Authors.') 
        print('    9. Exit    ')
        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            # Function to Add New Author
            new_authors()    
            
        elif user_choice == '2' : 
            # Function to Edit an Author information.
            edit_authors()
            
        elif user_choice == '3' : 
            # Function to Delete an Author.
            delete_authors() 
            
        elif user_choice == '4' : 
            # Function to Show All Author.
            show_authors() 
         
        elif user_choice == '9' : 
            return 
                
        
def class_menu(): 

    while True : 
        os.system('clear')
        print('\n   ====== LMS - Classification Managment ======')
        print('    1. Add New Classification.')
        print('    2. Edit a Classification information.')
        print('    3. Delete a Classification.') 
        print('    4. Show Classifications')
        print('    9. Exit.')
            
        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            # Function to Add New Classification   
            new_classification()
        elif user_choice == '2' : 
            # Function to Edit a Classification information.
            edit_classification()  
        elif user_choice == '3' : 
            # Function to Delete a Classification.
            delete_classification()  

        elif user_choice == '4' : 
            # Function to Show a Classification.
            show_classification()  
    
         
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


def lib_info():
    os.system('clear')
    print('\n   ====== Information About the Library ======')  
     
    print('\n   Books information')  
    # Number of book in the Library     
    c.execute ("select count() from books where b_id > 0") 
    books_count = c.fetchone()
    print('     Total Books in the Library are: ',books_count[0])       
    
    # books  without classifications  
    c.execute ("select b_id from b_class where b_class_id > 0") 
    books_no_class = [item[0] for item in c.fetchall()]  
    print('     Total Books without Class',books_count[0] -  len(set(books_no_class)) )    
            
    # Books without Author
    c.execute ("select count() from books where b_a_id='' and b_id > 0") 
    books_no_author = c.fetchall()
    print('     Total books without Authors: ',books_no_author[0][0])       
     
    # books without ISBN 
    c.execute ("select count() from books where b_isbn='' and b_id > 0") 
    books_no_isbn = c.fetchall()
    print('     Total books without ISBN: ',books_no_isbn[0][0])       

    # books without Edition number 
    c.execute ("select count() from books where b_ed='' and b_id > 0") 
    books_no_ed = c.fetchall()
    print('     Total Books without Edition Number: ',books_no_ed[0][0])       

    # books without Publish Date 
    c.execute ("select count() from books where b_dop='' and b_id > 0") 
    books_no_pd = c.fetchall()
    print('     Total Books without Publish Date: ',books_no_pd[0][0])       


    # books under each classification 
      
    print('\n   Authors information:')  
    
    # Total Authors
    c.execute ("select count() from authors where a_id > 0") 
    auth_count = c.fetchone()       
    print('     Total Registered Authors are: ',auth_count[0])       
    
      
    # Authors without Books
    
    # Authors without emails
    c.execute ("select count() from authors where a_email='' and a_id > 0") 
    auth_no_email = c.fetchall()
    print('     Total Authors without Email: ',auth_no_email[0][0])       
    
    # Authors without Social Media Account 
    c.execute ("select a_id from sma where sma_id > 0") 
    sma_aid = c.fetchall()       
    a_in_sma = lambda sma_aid: [sma_id for each in sma_aid for sma_id in each]
    a_with_sma = list(dict.fromkeys(a_in_sma(sma_aid)))
    print('     Total Authors without Social Media Accounts: ',(auth_count[0] - len(a_with_sma)))  
    
    
    print('\n   Classifications information')  
    # Total of Classifications
    c.execute ("select count() from classifi_list where class_l_id > 0") 
    class_count = c.fetchone()       
    print('     Total Classification we have: ',class_count[0])
    
    # Classifications not linked with any books   
    c.execute ("select class_id from b_class where b_class_id > 0") 
    class_no_book = [item[0] for item in c.fetchall()]  
    print('    Classifications not linked with any books: ', (class_count[0]) - (len(set(class_no_book))))
    
    # Top 5 Classification used.
    print('    Top 5 Classification Used :')
    c.execute ("select class_id, count(*) from b_class where b_class_id > 0  group by class_id order by count() desc limit 5") 
    class_top_5 = c.fetchall()       
    for each in class_top_5:
            c.execute ("select class_name from classifi_list where class_l_id ={} ".format(each[0])) 
            class_name = c.fetchone() 
            print('         "{}"  Used  {}  Time/s.'.format(class_name[0],each[1]))
    
     

    input('\n   To Exit ... Press any key ..') 
            

# ============================= Classification Managment ==========================       
      
def new_classification(alone='Yes') :
    if alone =="Yes" :
        os.system('clear')
        print('\n   ====== Add New Classification ======') 
        
    while True  :
        class_name = input('\n   Enter the Classification and Press Enter. [ To Exit Enter Q ].. >  ').capitalize()
        
        c.execute ("select * from classifi_list where class_name='{}'".format(class_name)) 
        result = c.fetchone()     
                 
        if class_name not in ['q','Q']:  
            if (result != None) : 
                print('\n   We already have [{}] in the Classification Database. '.format(class_name)) 
            else:    
                c.execute ("INSERT INTO classifi_list (class_name) VALUES(:class_name)",{"class_name":class_name})
                db_conn.commit() 
                if alone == "No":
                    c.execute("select max(class_l_id) from classifi_list")
                    new_class_id = c.fetchone()
                    print('new_class_id[0]',new_class_id[0])
                    input('   check ...')
                    return new_class_id[0]
                print('\n      One Classification Added ... ')

        else:
            input('\n   To Exit ... Press any key ..') 
            return


def edit_classification() :
    os.system('clear')
    print('\n   ====== Edit Classification ======\n')
    #print('\n   To Edit a Classification, Enter it''s ID.') 
        
    # First we list down all classifications.
    show_classification('No')
    
    
    try:
        user_select = int(input('\n\n   Enter the ID of the Classification.  > '))
        c.execute ("select * from classifi_list where class_id = {}".format(user_select))     
        result = c.fetchone() 
    except:
        input('\n   Not Valid Value, Try again .. ')
        return

    if (result != None) : 
                user_yes = input('\n   Do You want to Edit "{}". [Y,N] '.format(result[1]))  
                if user_yes in ['y','Y'] :
                   new_class = input('\n   Enter the New Classification. >  ').capitalize() 
                   c.execute("update classifi_list set class_name = '{}' where class_id = {}".format(new_class.capitalize(),int(user_select))) 
                   db_conn.commit()  
                   input('\n      One Classification been updated ..... Press any key .. ')      
                else: 
                   input('\n      You Select to Exit ..... Press any key .. ') 
                   
    else: 
        input ('\n   Your Input is not Exist ... Press any key ..  ')   
            

      
def delete_classification() :
    os.system('clear') 
    while True:
        print('\n   ====== Delete Classification ======\n') 
        show_classification('No')
            
        # we need a validation on user inputs     
        del_class = input('\n\n   To Delete a Classification Enter it''s ID number [Q To Exit]  > ')
        
        if del_class not in ['Q','q'] :
            c.execute ("select * from classifi_list where class_l_id = '{}' ".format(int(del_class))) 
            c_to_del =  c.fetchone()[1]     
            print('\n   Are you sure you want to Delete "{}" Classification? '.format(c_to_del))     
            print('   This action may affect books has this Classification.') 
         
            user_approve = input('\n   If you are sure to Delete "{}" Press Y or N: > '.format(c_to_del))  
            if user_approve in ['y','Y'] : 
                c.execute ("delete from classifi_list where class_l_id = '{}' ".format(del_class))
                db_conn.commit() 
                input('\n   One Classification has been Deleted... Press any Key > ')    
            else: 
                input('\n\n   You Select NOT to Delete the "{}" Classification, Press any key to go back.. '.format(c_to_del))
    
            if input('\n   Do you Want to Delete Another Classification? [Y,N] > ') in ['n','N'] :
                return
        else:
             input('\n   You Select to Exit .. Press any Key > ')
             return   
        
    
    
def show_classification(alone ='Yes'):      
    if alone =='Yes':
        os.system('clear')
        print('\n   ====== Show Classification ======')
        print('   The List of Classifications We Have, Sorted in Alphbatic\n') 
    
    c.execute ("select * from classifi_list where class_l_id > 0  order by class_name")     
    class_list = c.fetchall()           
    for cla in range (0,(len(class_list)),4):
       try: 
           print('   {:<3}{:<20}'.format(class_list[cla][0],class_list[cla][1]),end="")
           print('{:<3}{:<20}'.format(class_list[cla+1][0],class_list[cla+1][1]),end="")
           print('{:<3}{:<20}'.format(class_list[cla+2][0],class_list[cla+2][1]),end="")
           print('{:<3}{:<20}'.format(class_list[cla+3][0],class_list[cla+3][1]))
           
       except:
           pass     
        
    if alone =='Yes' :
        input('\n\n         ... Press any Key ..') 
    
          
          
# ===================================    Authors  Managment   ======================= 
def new_authors(alone='Yes') :
   
    
    while True  :
        if alone =='Yes' :
            os.system('clear')
        print('\n   ====== Add New Authors ======') 
    
        author_name = input('\n   Enter the Author Name .. >  ').capitalize()
        author_email = input('   Enter the Author Email [Enter to be Empty].. >  ')

        c.execute ("select * from authors where a_name='{}'".format(author_name)) 
        result = c.fetchone()     
                 
        if (result != None) : 
            print('\n   We already have [{}] in the Auther Database. '.format(class_name)) 
        else:    
            c.execute ("INSERT INTO authors (a_name, a_email) VALUES(:a_name,:a_email)",{"a_name":author_name,"a_email":author_email})
            db_conn.commit() 
            print('\n      One Author Added ... ') 
            c.execute ("select max(a_id) from authors") 
            auth_id = c.fetchone()    
            while True :
                    if input('\n   Do you want to Add any Social Media Account to this Author? [Y,N] .. >  ') in ['Y','y']:  
                        sma_name = input('\n   Enter the Social Media Name.. > ').capitalize()
                        sma_link = input('   Enter the Social Media Link.. > ')
                        c.execute ("INSERT INTO sma (sma_name,sma_link,a_id) VALUES(:sma_name,:sma_link,:a_id)",{"sma_name":sma_name,"sma_link":sma_link,"a_id":auth_id[0]}) 
                        db_conn.commit() 
                    else:
                        if alone =='Yes':
                            break
                        else:
                            return auth_id[0] 

        if alone !="Yes": 
            return auth_id[0]
        else:    
            if input('\n\n   Do you want to Add Another Author? [Y,N].. >  ') in ['N','n'] :
                input('\n   To Exit ... Press any key ..') 
                return
        
            

def edit_authors(alone='Yes',aid = 0) :
   
    if alone =='Yes' :
        os.system('clear')
        print('\n   ====== Edit Authors ======') 
        print('   The List of Authors We Have, Sorted in Alphbatic\n') 

        # First we show all Authors so the user can select the One to be Edited.
        show_authors('No')
    
    if alone == 'No' : edit_auth = aid 
    else : edit_auth = input('\n\n   Enter the ID of the Author to Edit. [Q to Exit]  >  ')
    if edit_auth not in ['q','Q'] :
        try:
            c.execute ("select * from authors where a_id = {} ".format(int(edit_auth)))     
            auth_edi = c.fetchall()  
            # get the Author SMA 
            c.execute ("select * from sma where a_id = {}".format(int(edit_auth)))  
            sma_list = c.fetchall()
            print('         ID:',auth_edi[0][0])
            print('       Name:',auth_edi[0][1])
            print('      Email:',auth_edi[0][2])
            print('     Social Media:')
            for each in sma_list :  
                print('{:<11}{:<13} [ {} ]'.format('',each[2],each[3]))

            print('\n   Edit each Author Attributes. [To Keep the existed one Press Enter]')
            a_name = input('\n   Enter the Author Name.  >  ').capitalize()
            a_email = input('   Enter the Author Email.  >  ') 
            if a_name > "" :
                c.execute("update authors set a_name = '{}' where a_id = {}".format(a_name,int(edit_auth))) 
                db_conn.commit() 
            if a_email > "" :      
                c.execute("update authors set a_email = '{}' where a_id = {}".format(a_email,int(edit_auth))) 
                db_conn.commit()      
            
            if (sma_list) != "" :
                for each in sma_list :  
                    sma_l = input('   Enter the {} Account. [D to Delete the Account]  >  '.format(each[2])) 
                    if sma_l > "" and (sma_l not in ['d','D'] ):
                        c.execute("update sma set sma_link = '{}' where a_id = {} and sma_name = '{}'".format(sma_l,int(edit_auth),each[2])) 
                        db_conn.commit()
                    elif sma_l > "" and (sma_l in ['d','D']) :
                        c.execute ("delete from sma where sma_id = '{}' ".format(each[0]))
                        db_conn.commit()
                        print('   {} Account Deleted... '.format(each[2]))
            
            
            while True :
                    if input('\n   Do you want to Add any Social Media Account to this Author? [Y,N] .. >  ') in ['Y','y']: 
                        sma_name = input('\n   Enter the Social Media Name.. >  ').capitalize()
                        sma_link = input('   Enter the Social Media Link.. >  ')
                        c.execute ("INSERT INTO sma (sma_name,sma_link,a_id) VALUES(:sma_name,:sma_link,:a_id)",{"sma_name":sma_name,"sma_link":sma_link,"a_id":int(edit_auth)}) 
                        db_conn.commit() 
                    else:
                        break
                  
        except:
            
           print('\n   Not valid .. ')
    input('\n   To Exit ... Press any key ..')
    return
    


def delete_authors():
    os.system('clear')
    print('\n   ====== Delete Authors ======') 
    print('   The List of Authors We Have, Sorted in Alphbatic\n') 
    c.execute ("select * from authors where a_id > 0  order by a_name")     
    auth_list = c.fetchall() 
    
    # First we show all Authors so the user can select the One to be Deleted.
    show_authors('No')
   
    print('\n\n\n   NOTES: Deleting an Author may effect on other Entities in the Library Data.')
    del_auth = input('\n   Enter the ID of the Author to delete it. [Q to Exit]  >  ')
    if del_auth not in ['q','Q'] :
        try:
            c.execute ("select * from authors where a_id = {} ".format(int(del_auth)))     
            auth_det = c.fetchall() 

            print('         ID:',auth_det[0][0])
            print('       Name:',auth_det[0][1])
            print('      Email:',auth_det[0][2])

            if input('\n   Are you Sure you want to Delete this Author? [Y,N].  >   ') in ['Y','y'] :
        
                c.execute ("delete from authors where a_id = '{}' ".format(int(del_auth)))
                db_conn.commit()  
                # To delete any SMA linked to this Author.
                c.execute ("delete from sma where a_id = '{}' ".format(int(del_auth)))
                db_conn.commit()
                input('\n   One Author has been Deleted... Press any Key > ')    
             
            else:
                print('\n   You Select NOT To Delete Author "{}" . '.format(auth_det[0][1]))
                input('\n   To Exit ... Press any key ..') 
        except:
            input('\n   Not valid .. ')
    return

    
def show_authors(details ='Yes') :
    
    if details =="Yes":
        os.system('clear')
        print('\n   ====== Show Authors ======')
        print('   The List of Authors We Have, Sorted in Alphbatic\n') 
    c.execute ("select * from authors where a_id > 0  order by a_name")     
    auth_list = c.fetchall()           
    
    # Show Only Authors Name and ID ============
    if details =='No' :
        for auth in range (0,(len(auth_list)),4):
            try: 
                print('   {:<3}{:<20}'.format(auth_list[auth][0],auth_list[auth][1]),end="")
                print('{:<3}{:<20}'.format(auth_list[auth+1][0],auth_list[auth+1][1]),end="")
                print('{:<3}{:<20}'.format(auth_list[auth+2][0],auth_list[auth+2][1]),end="")
                print('{:<3}{:<20}'.format(auth_list[auth+3][0],auth_list[auth+3][1]))
           
            except:
                pass     
    else : # Show Authors Details
        for auth in range (0,(len(auth_list))):
            try: 
                # For each Author we fetch the Social Media Accounts. 
                c.execute ("select * from sma where a_id = {}".format(auth_list[auth][0]))  
                sma_list = c.fetchall()
                print('\n     ID: {}'.format(auth_list[auth][0])) 
                print('   Name: {}'.format(auth_list[auth][1]))
                print('  Email: {}'.format(auth_list[auth][2]))
                print('  Social Media:')
                # Here we list  the SMA for the Author
                for each in sma_list :  
                    print('{:<11}{:<13} [ {} ]'.format('',each[2],each[3]))
                print('-'*50)           
            except:
                pass     
    
        input('\n\n         ... Press any Key ..') 
          
          
# ================================== Books Managment ======================== 
	    
	
def 	new_book (): 
    os.system('clear')
    print('\n   ====== Add New Book ======') 
    print('\n   ')
    b_name = input('   Enter the Book Name/Title ..: >  ').capitalize() 

    b_isbn = input ('   Enter the ISBN of the Book. :  >  ')
    b_dop  = input ('   Enter the Date of Publish. :  >  ') 
    b_ed  = input ('   Enter the Edition Number :  >  ')
    
    print('\n\n   Now, Select the Book Author ID, If the Author Name is not in the list, you will\n   Enter it in next step.\n')
    
    # First we show all Authors so the user can select one
    show_authors('No')
    b_auth = input ('\n\n   Enter the ID of the Book Author, if it''s Not in the List just Press Enter .  >  ')
    
    if b_auth =="" :
        # we need to Enter New Author to the System, so we will call the new_authors() Function from here. 
        b_auth = new_authors('No')
        
    c.execute ("INSERT INTO books (b_name, b_a_id, b_isbn, b_dop, b_ed) VALUES(:b_name, :b_a_id, :b_isbn, :b_dop, :b_ed)", { "b_name":b_name, "b_a_id":int(b_auth), "b_isbn":b_isbn, "b_dop":b_dop, "b_ed":b_ed  }) 
    db_conn.commit() 
     
    
    # To Add Classifications to the book
    print('\n\n   Now, Select a Classification ID, a Book may have more than One Classifications.\n   If the Classification is not in the list, you will Enter it in next step.\n')
    
    # First we show all Classifications so the user can select one
    show_classification('No')
    
    # Get the Book ID
    c.execute ("select max(b_id) from books")
    the_b_id = c.fetchone()     
    #print('\n   the max book id  = ',the_b_id[0])
    while True :
        b_class_id = input ('\n\n   Enter the ID of Classification, if it''s Not in the List just Press Enter. [Q to Exit]  >  ')
   
        try:
            if b_class_id in ['q','Q'] : 
                input('\n\n     One Book Added to the System ... Press any Key ..') 
                return
            elif b_class_id =="":
                # call add new classification 
                c_class_id = new_classification('No')
                            
                
            if isinstance(int(b_class_id[0]), int) :
                c.execute ("INSERT INTO b_class (b_id, class_id ) VALUES (:b_id, :class_id )", {"b_id":the_b_id[0], "class_id": int(b_class_id)})  
                db_conn.commit()
         
        except:
             
            input('\n\n   Invalid Input.. Press any Key ..')                           
    
 
def delete_book () :

    os.system('clear')
    print('\n   ====== Delete a Book ======')
    print('\n   The List of Books We Have, Sorted by Book Title\n') 
  
    # First we show all Bookd so the user can select the One to be Deleted.
    # we Call show_books function and pass 'T' 
    show_books('No','T')  
          
    del_book = input('\n\n   Entert the Book ID that you want to Delete: [Q to Exit]  >  ') 
    if del_book not in ['q','Q'] :
        try: 
            c.execute ("select b_name from books where b_id = {}".format(int(del_book)))     
            d_b_name = c.fetchone() 
            
            if input('\n   Are you Sure you want to Delete Book "{}"? [Y,N].  >   '.format(d_b_name[0])) in ['Y','y'] :             
                c.execute ("delete from books where b_id = {} ".format(int(del_book)))
                db_conn.commit()
                input('\n   One Book has been Deleted... Press any Key > ')    
    
            else:
                print('\n   You Select NOT To Delete The Book "{}" . '.format(d_b_name[0]))
                input('\n   To Exit ... Press any key ..') 
        except:    
            input('\n   Not valid .. ')
    
 
def edit_book(): 
    os.system('clear')
    print('\n   ====== Edit Books ======') 
            
    b_list_type = input('\n    To Edit a Book we Need to select it''s ID, Do you want to\n    List all Books in Detail [D], or Just Titles [T]? [Q Exit] [D , T , Q] > ') 
        
    if b_list_type in ['q','Q'] :
        return
    elif b_list_type in ['t','T'] :
        # Calling show_books function with list_type = T 
        show_books('No','T')
            
    elif b_list_type in ['d','D'] : 
        # Calling Show_books function with list_type = D
        show_books('No','D') 
        
    # if the user Enter any thing else than T or D 
    else :
        print('\n   Invalid Selection, try D for Details, T for Titles or Q to Exit')
        input('\n\n         ... Press any Key to Exit..') 
        return
        
    book_edit = int(input('\n\n   Select the Book ID to Edit it.  >  '))  
    
    # Show the Book Details.
    c.execute ("select * from books where b_id = {} ".format(book_edit))     
    book_detail = c.fetchall()
    print('\n             ID: {}'.format(book_detail[0][0])) 
    print('     Name/Title: {}'.format(book_detail[0][1]))
    print('      Book ISBN: {}'.format(book_detail[0][3]))
    print('   Publish Date: {}'.format(book_detail[0][4])) 
    print('   Book Edition: {}'.format(book_detail[0][5])) 
    print('   Book Classifications:') 
    # To get the Book Classification 
    c.execute ("select class_name from classifi_list INNER JOIN b_class ON (classifi_list.class_l_id = b_class.class_id) AND (b_class.b_id ={})".format(book_detail[0][0]))     
    b_class_list = c.fetchall()
    #print('b_class_list',b_class_list[0])
    try :
        for item in range(0,len(b_class_list),5) : 
            print(' '*17,b_class_list[item][0], end="")
            print(' | ',b_class_list[item+1][0], end="")
            print(' | ',b_class_list[item+2][0], end="")
            print(' | ',b_class_list[item+3][0], end="")
            print(' | ',b_class_list[item+4][0])
            
    except:
        pass
        
    auth_id = book_detail[0][2]
    
    # To get the Author Data 
    c.execute ("select * from authors where a_id = {}".format(int(auth_id)))     
    auth_list = c.fetchone()
           
    # To get the Author's Social Media Accounts. 
    c.execute ("select * from sma where a_id = {}".format(auth_id))  
    sma_list = c.fetchall()  
           
    # To print-out Author Data
    print('\n   The Book Author:')
    print('           Name: {}'.format(auth_list[1]))
    print('          Email: {}'.format(auth_list[2]))
    print('          Social Media:')
        
    # Here we list the SMA for the Author
    for each in sma_list :  
        print('{:<14}{:<13} [ {} ]'.format('',each[2],each[3]))
    print('-'*50)
    
    
    print('\n   Edit Each Book Attribute. [To Keep the existed one Press Enter]')
    b_name = input('\n   Enter the Book Name/Title.  >  ').capitalize()
    b_isbn = input('   Enter the Book ISBN.  >  ') 
    b_dop  = input('   Enter the Book Date of Publish.  >  ') 
    b_ed   = input('   Enter the Book Edition.  >  ') 
    if b_name > "" :
        c.execute("update books set b_name = '{}' where b_id = {}".format(b_name,int(book_edit))) 
        db_conn.commit() 
            
    if b_isbn > "" :
        c.execute("update books set b_isbn = '{}' where b_id = {}".format(b_isbn,int(book_edit))) 
        db_conn.commit()
            
    if b_dop > "" :
        c.execute("update books set b_dop = '{}' where b_id = {}".format(b_dop,int(book_edit))) 
        db_conn.commit()
               
    if b_ed > "" :
        c.execute("update books set b_ed = '{}' where b_id = {}".format(b_ed,int(book_edit))) 
        db_conn.commit()     
        
    print('\n   One Book has been Edited .. ')    
    
    
    # Editing Author information .. 
    if input('\n   Do you want to Edit the Author Information? [ Y, N] >  ') in ['Y','y'] : 
        print('\n   The Author Information:')
        # Calling edit_author function and pass the author ID
        edit_authors('No', auth_id) 
        input('\n\n    The Author Information updated.     ... Press any Key ..')
        
        
    # Edit Book Classification 
    if input('\n   Do you want to Edit the Book Classification? [Y, N] >  ') in ['Y','y'] : 
        print('\n   The Book Classifications:')
        
        c.execute ("select classifi_list.*, b_class.* from classifi_list INNER JOIN b_class ON (classifi_list.class_l_id = b_class.class_id) AND (b_class.b_id ={})".format(int(book_edit)))                 
        b_class_list = c.fetchall() 
        
        if len(b_class_list) == 0 :    
            print('       There is No Classification for this Book.')
        try:
            for item in range(0,len(b_class_list),5) :
                print('   ',b_class_list[item][2],b_class_list[item][1], end="")
                print('  |  ',b_class_list[item+1][2],b_class_list[item+1][1], end="")
                print('  |  ',b_class_list[item+2][2],b_class_list[item+2][1], end="")
                print('  |  ',b_class_list[item+3][2],b_class_list[item+3][1], end="")
                print('  |  ',b_class_list[item+4][2],b_class_list[item+4][1])
        except:
            pass
        
        # To remove classification from the book
        print('\n\n\n   First, IF you Want to Remove any Classifications from the Book..')
     
        while True :
            
            user_class_remove = input('   IF YES, Enter the Classification ID to be Removed, IF NO, Just Press Enter.  >  ')
            
            if user_class_remove !="" and isinstance(int(user_class_remove), int) :
                c.execute ("DELETE from b_class where b_class_id = {} and b_id={} ".format(int(user_class_remove),int(book_edit)))
                db_conn.commit()
                    
            else :
                break 
            print('\n   Do you Want to Remove another One?')
            
        # To Add more Classification to a Book
        if user_class_remove =="" :
      
                # First we show all Classifications so the user can select one
                show_classification('No')
 
                print('\n\n   Now, IF You want to Add more Classification Enter it''s ID, a Book may have more than One Classifications.\n   IF the Classification is not in the list, you will Enter it in next step.\n\n')
         
                while True :
                    b_class_id = input ('\n\n   Enter the ID of Classification, if it''s Not in the List just Press Enter. [OR Q to Exit]  >  ')
   
                    try:
                        if b_class_id in ['q','Q'] : 
                            input('\n\n    The Book has been Edited .. Press any Key to Exit ..') 
                            return
                        elif b_class_id =="":
                            # We will Enter New Classification..
                            while True :
                                # call add new classification 
                                n_class_id = new_classification('No')
                                
                                c.execute ("INSERT INTO b_class (b_id, class_id ) VALUES (:b_id, :class_id )", {"b_id":int(book_edit), "class_id":int(n_class_id) })  
                                db_conn.commit()
                                n_class = input('\n   Do you want to Add Another Classification? [Y,N] > ')
                                if  n_class in ['N','n','y','Y'] : 
                                    if n_class in ['N','n'] :
                                        break
                                else :
                                    input('\n\n     ... Press any Key to Exit ..')
                                    return 

                        elif b_class_id !="" and isinstance(int(b_class_id), int) :
                             c.execute ("INSERT INTO b_class (b_id, class_id ) VALUES (:b_id, :class_id )", {"b_id":int(book_edit), "class_id":int(b_class_id) })  
                             db_conn.commit()
                             
                    except: 
                        input('\n\n   Invalid Input.. Press any Key ..')                        
                        return   

    else:
        input('\n\n         ... Press any Key ..')
        return 
 
     
     
def show_books(alone='Yes', list_type = "D") : 
        
    c.execute ("select * from books where b_id > 0  order by b_name")     
    books_list = c.fetchall()           
    if list_type =="D":
        os.system('clear')
        print('\n   ====== Show Books ======')
        print('\n   The List of Books We Have, Sorted by Book Title\n') 
    
        for book in range (0,(len(books_list))):
           try: 
               print('\n             ID: {}'.format(books_list[book][0])) 
               print('     Name/Title: {}'.format(books_list[book][1]))
               print('      Book ISBN: {}'.format(books_list[book][3]))
               print('   Publish Date: {}'.format(books_list[book][4])) 
               print('   Book Edition: {}'.format(books_list[book][5]))
               
               # To get the Book Classification 
               c.execute ("select class_name from classifi_list INNER JOIN b_class ON (classifi_list.class_l_id = b_class.class_id) AND (b_class.b_id ={})".format(books_list[book][0]))     
               b_class_list = c.fetchall()
               print('\n   Book Classification:')
               try:
                   for i in range(0,len(b_class_list),5) :
                       print(' '*15,b_class_list[i][0], end ="")
                       print(' | ',b_class_list[i+1][0], end ="")
                       print(' | ',b_class_list[i+2][0], end ="")
                       print(' | ',b_class_list[i+3][0])    
                       
                       
               except:
                   pass 
                                  
               auth_id = books_list[book][2]
               # To get the Author Data 
               c.execute ("select * from authors where a_id = {}".format(int(auth_id)))     
               auth_list = c.fetchone()
           
               # To get the Author's Social Media Accounts. 
               c.execute ("select * from sma where a_id = {}".format(auth_id))  
               sma_list = c.fetchall()  
           
               # To print-out Author Data
               print('\n\n   The Book Author:')
               print('           Name: {}'.format(auth_list[1]))
               print('          Email: {}'.format(auth_list[2]))
               print('          Social Media:')
               
               # Here we list  the SMA for the Author
               for each in sma_list :  
                  print('{:<14}{:<13} [ {} ]'.format('',each[2],each[3]))
               print('-'*50)           
           except:
               pass     
   
        input('\n\n         ... Press any Key ..') 
        return

    if list_type == "T" :
        print('\n')
        for book in range (0,(len(books_list)),4):
            try: 
                print('    {:<3}{:<27}'.format(books_list[book][0],books_list[book][1]),end="")
                print('{:<3}{:<27}'.format(books_list[book+1][0],books_list[book+1][1]),end="")
                print('{:<3}{:<27}'.format(books_list[book+2][0],books_list[book+2][1]),end="")
                print('{:<3}{:<27}'.format(books_list[book+3][0],books_list[book+3][1]))           
            
            #Exception for index out of range error
            except:
                pass
        if alone =='Yes' :         
            input('\n\n         ... Press any Key ..')
            return 
        else : return    
        
    
# FIRST: We RUN Next TWO lines one time, So you can remove the # run it, EXIT for the system, put the # back again.
#create_tables_() 
#insert_record_0() 
    
    
main_menu()  
c.close()
