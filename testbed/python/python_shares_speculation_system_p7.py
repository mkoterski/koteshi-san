




"""

Shares Speculation System
Date: 5.7.2020
By: Ali
Version: V01-05072020    


Part-1:
    
    Project Definition, Concept, Scope of work, List of Tables and Fields  
    
    
    No Code
      
       
Part-2:
    
    Set database connection.
    Create Tables.
    Insert record Zero.
    Create Main Menu.
    Functions:
        1. 
        2.
        3. Main Menu
        
        
        
Part-3 : 

    Budget Managment Functions
    Date Validation

       
       
Part-4:
           
    Share Managment Functions   
    
    
    
part-5:    
        1. Add New Table s_basket. 
        2. Changing in Main Menu.
        3. Writing the code to save Buying record in  Buying Transaction Function.  
        4. Writing the code to Display Buying records in Show All Transaction
        5. [Important Note]: This app for saving transactions and not for desetion making and dose't have 
           any AI of ML Model to predict the prices and/or giving sugestions on buying or selling shares. 

        

Part-6:
        1. Writing the code to save Selling record in  Selling Transaction Function.  
        2. Writing the code to Display Selling records in Show All Transaction
        3. Update the budget_t: Subtract the cost when we Buy Shares. 
        4. Update the budget_t: Adding Incomes When we Sell shares.  
        5. Update the Show Budget Function.      
        6. Adding the one-line Exit code : if VARIABLE-NAME in ['q','Q'] : return to Budgets Managment Functions.



Part-7:
        1. Writing the code to Delete Transaction.
        2. Writing the code to Display Both Buying and Selling records in ONE Table in Show All Transaction
        



""" 


import sqlite3, os 

# Create the data-base and name it as Share_S_System. 
db_conn = sqlite3.connect ("Share_S_System.db") 

# set the connection. </font>
c = db_conn.cursor() 

def create_tables_() :
    # to create tables.         
    
    sql_share_t =    "CREATE TABLE if not exists shares_name  (s_id INTEGER PRIMARY KEY AUTOINCREMENT, full_name text, abb_name text)" 
            
    sql_buy_t_t =   "CREATE TABLE if not exists buy_t_table (bt_id INTEGER PRIMARY KEY AUTOINCREMENT ,buy_date text, sn_id integer, buy_amount integer, buy_price float, cost float)" 
    
    sql_sell_t_t  = "CREATE TABLE if not exists sell_t_table (st_id INTEGER PRIMARY KEY AUTOINCREMENT, sell_date text, sn_id integer, sell_amount integer, sell_price float, profit float)" 

    sql_s_basket = "CREATE TABLE if not exists s_basket (sb_id INTEGER PRIMARY KEY AUTOINCREMENT, sn_id integer, ts_amount float, min_p float, max_p float)"   
 
    sql_budget_t  = "CREATE TABLE if not exists budget_t (bud_id INTEGER PRIMARY KEY AUTOINCREMENT, bud_date text, bud_amount float, bud_note text )"  

    sql_year_roi =  "CREATE TABLE if not exists year_roi (y_id INTEGER PRIMARY KEY AUTOINCREMENT, bud_amount float, profits float, costs float, roi float, t_buy float, t_sell float )"


    c.execute(sql_share_t) 
    db_conn.commit() 

    c.execute(sql_buy_t_t) 
    db_conn.commit() 

    c.execute(sql_sell_t_t)
    db_conn.commit()
        
    c.execute(sql_s_basket)    
    db_conn.commit()
        
    c.execute(sql_budget_t) 
    db_conn.commit() 

    c.execute(sql_year_roi) 
    db_conn.commit()  
        
     

    input('\n .. Shares Speculation System Tables created.. Press any key .. ') 


#Function to Insert the Zero Record 
def insert_record_0(): 


    c.execute ("INSERT INTO shares_name (s_id)   VALUES(:s_id)" ,{"s_id":0}) 
    c.execute ("INSERT INTO buy_t_table (bt_id)  VALUES(:bt_id)",{"bt_id":0})
    c.execute ("INSERT INTO sell_t_table (st_id) VALUES(:st_id)",{"st_id":0}) 
    
    c.execute ("INSERT INTO s_basket     (sb_id) VALUES(:sb_id)",{"sb_id":0}) 
    
    c.execute ("INSERT INTO budget_t (bud_id) VALUES(:bud_id)",{"bud_id":0})
    
    c.execute ("INSERT INTO year_roi (y_id) VALUES(:y_id)",{"y_id":0}) 
        
    db_conn.commit()     

    input('\n ...Dummy records been Inserted .... Press any key .. ') 


def date_validation (the_d) :

    if (len(the_d) !=10) or (the_d[2] !='-' and the_d[5] !='-') :
        return '  Date Not Valid. [Date format: dd-mm-yyyy]'
    else:
        
        if not(len((the_d.split("-")[2])) == 4 ):
            return '   Date Not Valid "Bad Year". [Date format: dd-mm-yyyy].'
        if not (len((the_d.split("-")[1])) == 2 and (int(the_d.split("-")[1]) > 0 and  int(the_d.split("-")[1]) <=12) ):
            return '   Date Not Valid "Bad Month". [Date format: dd-mm-yyyy].'
        if not (len((the_d.split("-")[0])) == 2 and (int(the_d.split("-")[0]) > 0 and  int(the_d.split("-")[0]) <=31)) :
            return '   Date Not Valid "Bad Day". [Date format: dd-mm-yyyy].'
      
    return 'valid'    

    
    
def main_menu (): 

    while True : 
        os.system('clear')
        print('\n   ====== Shares Speculation System ======')
        print('   1. Budget Managment.')
        print('   2. Transactions Managment.')      
        print('   3. Shares List.') 
        print('   4. ROI Information')
        print('   9. Exit.    ')
        
        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            budget_menu() 
            
        elif user_choice == '2' :
            share_transaction_menu()
                 
        elif user_choice == '3' : 
            share_menu() 
            
        elif user_choice == '4' : 
            roi_info() 
            
        elif user_choice == '9' : 
            print('\n\n   You select to exit from the application.\n\n ')
            return 
            

# =======================   BUDGET MANAGMENT ================================== 
def budget_menu(): 

    while True : 
        os.system('clear')
        print('\n   ====== Budget Managment ======')
        print('   1. Add New Budget.') 
        print('   2. Withdraw Budget.') 
        print('   3. Edit a Budget.')
        print('   4. Delete a Budget.')
        print('   5. Show all Budget.')
        print('   9. Exit.')

        user_choice = input('\n   Select the Action you want from the Menu: ')
    
        if  user_choice == '1' :
            add_budget() 
        elif  user_choice == '2' :
            sub_budget() 
                
        elif user_choice == '3' :
            edit_budget()

        elif user_choice == '4' :
            del_budget()

        elif user_choice == '5' :
            show_budget('No')

        elif user_choice == '9' : 
            print('\n\n   .... Press any key to  Exit.  ')
            return
    


def add_budget (): 
    os.system('clear')
    print('\n   ====== Add New Budget ======\n\n') 
    print('   Enter the Details of the Budget..\n')
      
    while True :
        bud_date = input ('   Enter the Date as [dd-mm-yyyy]. [Q to Exit]  >  ') 
        if  bud_date in ['q','Q'] : return
        msg = (date_validation (bud_date))
        if msg !='valid' :
            print(msg) 
        else:
            break
    bud_amount = input ('   Enter the Budget Amount. [Q to Exit] >  ')
    if  bud_amount in ['q','Q'] : return
    bud_note = input ('   Enter any Notes if you want. [Hint: Cheque No.]  [Q to Exit]>  ') 
    if  bud_note in ['q','Q'] : return
    bud_note = " ".join([word.capitalize() for word in bud_note.split(" ")])    
    c.execute ("INSERT INTO budget_t (bud_date ,bud_amount, bud_note)  VALUES(:bud_date ,:bud_amount, :bud_note)",{"bud_date":bud_date ,"bud_amount":float(bud_amount), "bud_note":bud_note}) 
    db_conn.commit()
          
    input('\n\n        ... Press any Key to Exit.   ')           
            
   
def sub_budget (): 
    os.system('clear')
    print('\n   ====== Withdraw from Budget ======\n\n')
    print('   Enter the Details of Withdraw Amount..\n')
    while True :
        bud_date = input ('   Enter the Date as [dd-mm-yyyy]. [Q to Exit] >  ') 
        if bud_date in ['q','Q'] : return
        msg = (date_validation (bud_date))
        if msg !='valid' :
            print(msg) 
        else:
            break
   
    bud_amount = input ('   Enter the Withdraw Amount. [Q to Exit] >  ')
    if  bud_amount in ['q','Q'] : return
    if int(bud_amount) > 0 : 
        bud_amount = int(bud_amount) * (-1)
    bud_note = input ('   Enter any Notes if you want. [Hint: Cheque No.]  [Q to Exit] >  ')
    if  bud_note in ['q','Q'] : return
    bud_note = "[ WITHDRAW ], " + bud_note 
    bud_note = " ".join([word.capitalize() for word in bud_note.split(" ")])
    c.execute ("INSERT INTO budget_t (bud_date ,bud_amount, bud_note)  VALUES(:bud_date ,:bud_amount, :bud_note)",{"bud_date":bud_date ,"bud_amount":bud_amount, "bud_note": bud_note}) 
    db_conn.commit()
           
    input('\n\n        ... Press any Ket to Exit.  ')   
       
   
           
    
def edit_budget (): 
    os.system('clear')
    print('\n   ====== Edit Budget ======\n\n') 
    show_budget (inside='Yes')
    try: 
        edit_budget = input ('\n\n    Select the Budget ID to Edit.  > ')
        c.execute ("select * from budget_t where bud_id ={}".format(int(edit_budget))) 
        e_budget = c.fetchone()
        if e_budget != None: 
            print('\n    You Select to Edit this Budget ..') 
        else:
            print('\n    ID Not Valid ... ')
             
        print('\n       ID: ',e_budget[0])
        print('     Date: ',e_budget[1])
        print('   Amount:  {:,}'.format(e_budget[2]))
        print('     Note: ',e_budget[3])
    
        print('\n\n   Edit Each Attribute OR Press Enter to Skip.. \n')
    
        while True :
            new_b_date = input('   Enter the New Date as [dd-mm-yyyy]. [Q to Exit]  > ')
            if new_b_date in ['q','Q'] : return
            if new_b_date >"" : 
                msg = (date_validation (new_b_date))
                if msg !='valid' :
                    print(msg) 
                else:
                    c.execute("update budget_t set bud_date = '{}' where bud_id = {}".format(new_b_date,int(e_budget[0]))) 
                    db_conn.commit() 
                    break    
            elif new_b_date =="" :break
                        
        new_b_amount = input('   Enter the New Amount [Q to Exit] >  ')
        if  new_b_amount in ['q','Q'] : return
        if new_b_amount > "" : 
            if input ('\n   You want to change the Budget Amount From {:,}  To {:,}. CONFIRM [Y,N] > '.format(float(e_budget[2]),float(new_b_amount))) in ['Y','y'] :
                c.execute("update budget_t set bud_amount = '{}' where bud_id = {}".format(float(new_b_amount),int(e_budget[0]))) 
                db_conn.commit() 
        else:
            print('   Budget Amount Not changed..\n')
            
        new_b_note = input('\n   Enter the New Note: [Q to Exit]  > ')
        if  new_b_note in ['q','Q'] : return
        if new_b_note > "" :
            new_b_note = " ".join([word.capitalize() for word in new_b_note.split(" ")])
            if (e_budget[3])[0] =='[' and int(new_b_amount) < 0 :
                new_b_note = "[ WITHDRAW ], " + new_b_note     
        
            c.execute("update budget_t set bud_note = '{}' where bud_id = {}".format(new_b_note,int(e_budget[0])))          
            db_conn.commit() 
    
        input('\n   ... DONE ...  Press any key to Exit.  ')
    except:
        input('\n       ... Error in User Input.  ... Press any key to Exit ...')


    
def del_budget (): 
    os.system('clear')
    print('\n   ====== Delete Budget ======\n\n') 
    show_budget (inside='Yes')
    
    try:
        del_budget= input ('\n\n    Select the Budget ID to be Deleted.  > ')
        c.execute("select * from budget_t where bud_id = {}".format(int(del_budget)))          
        to_del = c.fetchone()
        if to_del != None: 
            print('\n    You Select to Delete this Budget ..') 
        else:
            print('\n    ID Not Valid ... ')
        print('\n         ID:',to_del[0])
        print('       Date:',to_del[1])
        print('     Amount: {:,}'.format(to_del[2]))
        print('       Note:',to_del[3])   
   
        if input('\n    Are you sure you want to DELETE this Budget Record?  [Y,N] > ') in ['Y','y'] :
            c.execute("delete from budget_t where bud_id = {}".format(int(del_budget))) 
            db_conn.commit() 
            input('\n       ... One Record Deleted.  ... Press any key to Exit ...')
       
        else:
            input('\n       ... You Did NOT CONFIRM the Deleting.  ... Press any key to Exit ...')
            return 
    except:
        input('\n       ... Error in User Input.  ... Press any key to Exit ...')
                   
          
def show_budget (inside='No'): 
    if inside =='No' :
        os.system('clear')
        print('\n   ====== Show Budgets ======\n\n') 
        print('   List of Budgets ..\n')
    c.execute ("select * from budget_t where bud_id >0") 
    budgets = c.fetchall() 
  
    print('      {:<10}{:<13}{:<16}{}'.format('ID','Date','Amount','Note'))
    print("    ","-"*70)
    if len(budgets) > 0 :
        try:
            for x in range(0,len(budgets)) : 
              # print("      {:<8}{:<14}{:,}{:<7}{}".format(budgets[x][0],budgets[x][1],budgets[x][2]," ",budgets[x][3]))   format(1234567.89, ',.2f')
               print(" "*5, budgets[x][0]," "*(5 - len(str(budgets[x][0]))),budgets[x][1]," "*3,format(budgets[x][2],',.2f')," "*(15- len(str(budgets[x][2]))),budgets[x][3])
     
        except:
            pass 
        if inside =='No':
            # get total in Budget.
            c.execute ("select sum(bud_amount) from budget_t where bud_id >0") 
            budget_amount = c.fetchone() 
            print('\n\n    The Total Amount Budgets in the Account is : {:,} '.format(budget_amount[0]))
            if (budget_amount) == 0  :
                print('\n\n    The Budget/Money = 0. ')        
    else : 
        print('\n\n      There is No Budget/Money in the System. ')       
    if inside == 'No': input('\n      ... Press any key to Exit..  ')   
        

# =======================   SHARES MANAGMENT ================================== 

def share_menu() :
    while True : 
        os.system('clear')
        print('\n   ====== Shares Managment ======')
        print('   1. Add New Share.')
        print('   2. Edit a Share.')
        print('   3. Delete a Share.')
        print('   4. Show all shares.')
        print('   9. Exit.')

        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            add_share() 
            
        elif user_choice == '2' :
            edit_share()
             
        elif user_choice == '3' : 
            delete_share() 
            
        elif user_choice == '4' : 
            show_share('No') 

        elif user_choice == '9' : 
            print('\n\n   .... Press any key to  Exit.  ')
            return 

def add_share() :
        
    os.system('clear')
    print('\n   ====== Add New Share ======\n\n')
    while True :
            
        abb_name = input("   Enter the Abbreviation Name of the Share.. > ").upper() 
        full_name = " ".join([word.capitalize() for word in input('     Enter the Full Name of the Share.. > ').split(" ")])

        c.execute ("select * from shares_name where full_name ='{}' or abb_name = '{}'".format(full_name, abb_name)) 
        share_exist = c.fetchone ()
        print(share_exist)
        if share_exist != None  :
            print('\n   It seams that the Share Exist in the Database, Name or Abbreviation CAN NOT be Duplicated.')
            print('   Try another Name. ')
        else :      
            c.execute ("INSERT INTO shares_name (full_name , abb_name)  VALUES(:full_name , :abb_name)",{"full_name":full_name, "abb_name":abb_name}) 
            db_conn.commit()
            
        if input ('\n   Do you want to Enter another Share Name?.  [Y,N]. >  ')  not in ['Y','y']: 
            input ('\n    .... Press any key to  Exit.  ')
            return
                 
    
def edit_share() :
    os.system('clear')
    print('\n   ====== Edit Share Name ======\n\n')
    print('   Here is a list of Shares we have in the System .. \n')
    show_share('Yes')
    edit_share = input('\n\n   Enter the ID for the Share Name you want to Edit. [Q to Exit] >  ') 
    if edit_share in ['q', 'Q'] :
        input ('\n\n    .... Press any key to  Exit.')
        return    
    elif edit_share.isnumeric() :
        c.execute ("select * from shares_name where s_id ={}".format(int(edit_share))) 
        share_edit = c.fetchone ()
        print('\n   You select to Edit a share: ',share_edit[0])
        abb_s_name = input('\n   Current share Abbreviation is "{}", Enter the new one. [Press Enter to keep as is] >  '.format(share_edit[2]))    
        f_s_name = input('   Current share Full Name is "{}", Enter the new one. [Press Enter to keep as is] >  '.format(share_edit[1]))
            
        if abb_s_name > "" :           
            c.execute("update shares_name set abb_name = '{}' where s_id = {}".format(abb_s_name.upper(),int(edit_share))) 
            db_conn.commit() 
        
        elif f_s_name > "" : 
            # Capitalize the abb_s_name 
            f_s_name = " ".join([word.capitalize() for word in f_s_name.split(" ")])    
            c.execute("update shares_name set full_name = '{}' where s_id = {}".format(f_s_name,int(edit_share))) 
            db_conn.commit() 
  
            input ('\n    ....One Record changed. Press any key to  Exit.')
            return
    else :
            input ('\n    ....Share will NOT be Edit any. Press any key to  Exit.')
            return
    

    
def delete_share() :
    os.system('clear')
    print('\n   ====== Delete a Share  ======\n\n')
    
    print('   Here is a list of Shares we have in the System .. \n')
    show_share('Yes')
    
    del_share = input('\n\n   Enter the ID for the Share Name you want to Delete. [Q to Exit] >  ') 

    if del_share in ['q', 'Q'] :
        input ('\n\n    .... Press any key to  Exit.')
        return    
    elif del_share.isnumeric() :
        if (input ('   Are you SURE you want to DELETE Share ID {} ? [Y,N] >  '.format(del_share))) in ['y','Y'] :   
            c.execute ("delete from shares_name where s_id ={}".format(int(del_share))) 
            db_conn.commit()
            input ('\n    ....One Record DELETED. Press any key to  Exit.')
            return
        else :
            input ('\n    ....Share will NOT be Deleted. Press any key to  Exit.')
            return
            
    else :
        input ('\n    ....Invalid Inpout. Press any key to  Exit.')
        return
                
            
def show_share(inside = 'Yes') :
    if inside == 'No' :
        os.system('clear')
        print('\n   ====== Show Share List ======\n\n')
     
    c.execute ("select * from shares_name where s_id >0") 
    shares = c.fetchall() 
    if inside == 'No' :
        try:
            for x in range(0,len(shares),3) : 
                print('   {:<5}{:<25}'.format(shares[x][2],shares[x][1]),end="")
                print('   {:<5}{:<25}'.format(shares[x+1][2],shares[x+1][1]),end="")
                print('   {:<5}{:<25}'.format(shares[x+2][2],shares[x+2][1]))
        except:
            pass 
        
        input ('\n\n    .... Press any key to  Exit.')
        return

    if inside == 'Yes' :
        try:
            for x in range(0,len(shares),3) : 
                print('   {:<3}{:<5}{:<25}'.format(shares[x][0],shares[x][2],shares[x][1]),end="")
                print('   {:<3}{:<5}{:<25}'.format(shares[x+1][0],shares[x+1][2],shares[x+1][1]),end="")
                print('   {:<3}{:<5}{:<25}'.format(shares[x+2][0],shares[x+2][2],shares[x+2][1]))
        except:
            pass
        
            
# ===================================   Shares Transactions Managment    ==================================



def share_transaction_menu() :
    while True : 
        os.system('clear')
        print('\n   ====== Share Transactions Managment ======')
        print('   1. Buy Share.')
        print('   2. Sell Share.')
        print('   3. Edit a Transaction.')
        print('   4. Delete a Transaction.')
        print('   5. Show all Transactions.')
        print('   9. Exit.')

        user_choice = input('\n   Select the Action you want from the Menu: ')
        
        if  user_choice == '1' :
            buy_share() 
            
        elif user_choice == '2' :
            sell_share()
             
        elif user_choice == '3' : 
            edit_trans() 
            
        elif user_choice == '4' : 
            del_trans() 
        elif user_choice == '5' : 
            show_all_trans() 

        elif user_choice == '9' : 
            print('\n\n   .... Press any key to  Exit.  ')
            return 



def buy_share() : 

    os.system('clear')
    print('\n   ====== Buying Shares  ======\n\n')
    
    # Display all shares on the screen by Calling show_share function
    show_share(inside = 'Yes') 

    b_s_id = input('\n\n   Select the share ID  [Q To Exit] >  ')
    if b_s_id in ['q','Q'] : return 
    
    c.execute (" select full_name, abb_name from shares_name where s_id = {} ".format(int(b_s_id)) )
    share_name = c.fetchone() 
    
    c.execute ("select * from s_basket where sn_id = {} ".format(int(b_s_id)) )
    share_in = c.fetchone() 
        
    if share_in != None : 
        c.execute (" select sell_amount, sell_price from sell_t_table where sell_t_table.sn_id = {} ".format(int(b_s_id)) )
        sell_trans = c.fetchall()
    
        print('\n   We have {} Total Shares of {} ( {} ). '.format(share_in[2], share_name[0],share_name[1])) #[sum_x for x in buy_trans[0] sum_x] )   
        print('   Lowest price we bought before was {}, and the Highest was {} .'.format(share_in[3],share_in[4]))   
    
    else :
        print("\n   We Don't Have any Shares of {} ( {} ).".format(share_name[0],share_name[1]))
    
    # Collecting Buying share Record to be Saved.     
    while True :      
        buy_date = input ('\n   Enter the Date as [dd-mm-yyyy]. [Q To Exit] >  ')
        if buy_date in ['q','Q'] : return  
        msg = (date_validation (buy_date))
        if msg !='valid' :
            print(msg) 
        else:
            break

    buy_amount = input ('   Enter the Amount/Number of the Share you Bought. [Q To Exit]  >  ')  
    if buy_amount in ['q','Q'] : return 
    buy_price = input  ('   Enter the Price of the Share. [Q To Exit] > ') 
    if buy_price in ['q','Q'] : return 
    s_cost  = round(float(buy_amount) * float(buy_price),3)
   
            
    c.execute ("INSERT INTO  buy_t_table (buy_date , sn_id , buy_amount , buy_price , cost)	VALUES(:buy_date , :sn_id , :buy_amount , :buy_price , :cost)", {"buy_date":buy_date , "sn_id":int(b_s_id) , "buy_amount":int(buy_amount) , "buy_price":float(buy_price) , "cost":float(s_cost)}) 
    db_conn.commit() 
    
    # Update the budget table by Adding record to reduce the budget.  
    b_note='[ Buying ]: Subtract Because of Buying Transaction.'
    c.execute("INSERT INTO  budget_t  (bud_date, bud_amount, bud_note) Values (:bud_date, :bud_amount, :bud_note)",{"bud_date":buy_date, "bud_amount": -1 * s_cost, "bud_note":b_note})
    db_conn.commit()  
        
    # Creating a record in share-Basket table.   
    if share_in == None :
        c.execute ("INSERT INTO s_basket (sn_id , ts_amount , min_p , max_p) values (:sn_id , :ts_amount , :min_p , :max_p) ",{"sn_id":int(b_s_id) , "ts_amount":int(buy_amount) , "min_p":float(buy_price) , "max_p":float(buy_price)}) 
        db_conn.commit()  
    else :
        c.execute("update s_basket set ts_amount = {} where sn_id = {}".format((int(buy_amount) + int(share_in[2])),int(b_s_id)))
        db_conn.commit() 
                        
        if share_in[3] > float(buy_price) :
            # replace the current min_p
            c.execute("update s_basket set min_p = {} where sn_id = {}".format(float(buy_price),int(b_s_id)))          
            db_conn.commit() 
 
        if share_in[4] < float(buy_price) :
            # replace the current max_p    
            c.execute("update s_basket set max_p = {} where sn_id = {}".format(float(buy_price),int(b_s_id)))          
            db_conn.commit()

    input('\n    ..One Buying Transaction Saved.    ... Press any key to Exit.  ')


    
def sell_share():    
     
    os.system('clear')
    print('\n   ====== Selling Shares  ======\n\n')
    show_share(inside = 'Yes') 

    s_s_id = input('\n\n\n   Select the share ID. [Q To Exit] >  ')
    if s_s_id in ['Q','q'] : return
         
    c.execute (" select * from s_basket where sn_id = {} ".format(int(s_s_id)) )
    we_have = c.fetchone()   
    c.execute (" select full_name, abb_name from shares_name where s_id = {} ".format(int(s_s_id)) )
    share_name = c.fetchone()

    if (we_have == None ) or (we_have[2] == 0):
        input('\n      You Don''t have any Shares of " {} ".    ... Press any key to Exit ...  > '.format(share_name[0]))
        return    
            
    c.execute (" select bt_id,  buy_amount, buy_price, buy_date from buy_t_table where buy_t_table.sn_id = {}  ".format(int(s_s_id)) )
    buy_trans = c.fetchall()   
   
    if we_have !=  None :  
        
        c.execute (" select sell_amount, sell_price from sell_t_table where sell_t_table.sn_id = {} ".format(int(s_s_id)) )
        sell_trans = c.fetchall() 
        
        total_sold = (0 if sell_trans == None else sum(sell_trans[sold][0] for sold in range (len(sell_trans)))) 
   
        total_s_have = we_have[2] 
       
        print('\n\n   Total Shares Amount We Sell Before: ',total_sold)
        print('\n   We have {} Total Shares of {}( {} ),\n   The Minimum Buying Price was ({})\n   and The Maximum was ({}). '.format(we_have[2], share_name[0],share_name[1],we_have[3], we_have[4])) #[sum_x for x in buy_trans[0] sum_x] )   
        
    print('\n   New Selling Transaction Detail.. ')   
    while True :      
        sell_date = input ('   Enter the Date as [dd-mm-yyyy]. [Q To Exit] >  ') 
        if sell_date in ['q','Q'] : return
        msg = (date_validation (sell_date))
        if msg !='valid' :
            print(msg) 
        else:
            break

    while True :
        sell_amount = int(input ('\n   Enter the Amount/Number of the Share to Sell. [Q To Exit] >  ') ) 
        if sell_amount in ['q','Q'] : return
        if int(sell_amount) > we_have[2] :
            print('\n   You Don''t Have This Much of " {} " Shares to Sell, Currently You Have {} Shares.'.format(share_name[0],we_have[2]))
            if input('\n   If You Want to Re-Enter the Sell Amount Press " Y ", or " N " to Exit .  > ') in ['n','N'] :
                try :
                    return
                except:
                    input('   Error in User Input. Press any Key to Exit. ')    
        else:
            break    
        
    sell_price = input  ('   Enter the Price of the Share. [Q To Exit] > ') 
    if sell_price in ['q','Q'] : return
    s_profit  = round(float(sell_amount) * float(sell_price),3)
    
    if input('\n   Press " Y " to Confirm Before we Save the Sell Transaction. > ') in ['y','Y'] :
        
        c.execute ("INSERT INTO  sell_t_table (sell_date , sn_id , sell_amount , sell_price , profit )	VALUES(:sell_date , :sn_id , :sell_amount , :sell_price , :profit )", {"sell_date":sell_date , "sn_id":int(s_s_id) , "sell_amount":int(sell_amount) , "sell_price":float(sell_price) , "profit":float(s_profit) }) 
        db_conn.commit()
        
        # Reduce the shares amount in the s_basket table.  
        c.execute("update s_basket set ts_amount = {} where sn_id = {}".format(we_have[2]-( int(sell_amount) ) , int(s_s_id) ))    
        db_conn.commit()  
        
        # Update the Budget table to add/insert a record of selling amount. 
        s_note='[ Selling ], Income from Selling Transaction.'
        c.execute("INSERT INTO  budget_t  (bud_date, bud_amount, bud_note) Values (:bud_date, :bud_amount, :bud_note)",{"bud_date":sell_date, "bud_amount": s_profit, "bud_note":s_note})
        db_conn.commit()   
         
    else:
        # If the user did Not confirm to Save the Sell Transaction.  
        print('\n   You Did Not Confirm Saving the Sell Transaction.')
        input('\n   ... Press any key to Exit.. ')
        return   
        
    input('\n    ..One Selling Transaction Saved.    ... Press any key to Exit.  ')


    
def edit_trans ():
    os.system('clear')
    print('\n   ====== Edit Transaction  ======\n\n')
   
     
     
def del_trans():
    os.system('clear')
    print('\n   ====== Delete Transaction  ======\n\n')
       
    print('   Do you Want to Delete a\n       1. Buying Transaction.\n       2. Selling Transaction.')  
    del_trans = input('\n    Select Type of Transaction to be Delete. [Q to Exit]  >  ') 
    if del_trans in ['Q','q'] : return 
        
    if del_trans == '1':  
        print('\n\n    List of Transactions we have, Select the ID to Delete it.') 
        show_all_trans ('Yes', '1')
        
        del_trans = input('\n     Enter the ID of the Transaction to be Deleted.  [Q to exit]  > ')
        if del_trans in ['Q','q'] : return 
        
        # Get transaction Detail
        c.execute (" select * from buy_t_table where bt_id  = {} ".format(del_trans))  
        trans_detail = c.fetchone()   
        c.execute (" select full_name from shares_name where s_id = {}".format(trans_detail[2])) 
        full_name = c.fetchone()
        print('\n                  ID:',trans_detail[0])
        print('          Share Date:',trans_detail[1])
        print('          Share Name:',full_name[0])
        print('        Share Amount:',format(trans_detail[3],','))
        print('               Price:',format(trans_detail[4],','))
        print('                Cost:',format(trans_detail[5],','))
        
        if input('\n      Enter Y to Confirm and DELETE the Transaction.  [Y,N]  >  ') in ['y','Y'] :
           
            # Delete the Buying Transaction then Delete the Buying Record from Budget and Update the Shares Basket. 
                
            # 1. Delete the Buying Transaction from Buying Table (buy_t_table).
            c.execute ("delete from buy_t_table where bt_id ={}".format(int(del_trans))) 
            db_conn.commit()
            
            # 2. Delete the Buying Record from the Budget Table. 
            # 2.1. Get the Budget Record. 
            c.execute ("select * from budget_t where bud_date = '{}' and bud_amount = '{}' and bud_note like '[ Buying ]%' ". format(trans_detail[1],(-1* trans_detail[5])))
            budget_del = c.fetchall()
            
            # 2.2 Delete the Record from the Budget Table (budget_t).
            c.execute ("delete from budget_t where bud_id ={}".format(budget_del[0][0])) 
            db_conn.commit()
            
            # 3. Update the Share Basket Table (s_basket).
            # 3.1. Get the Record 
            c.execute("select * from s_basket where sn_id = {}".format(trans_detail[2]))    
            s_basket_re = c.fetchone()
             
            # 3.2. Update the Share Amount.  
            c.execute("update s_basket set ts_amount = {} where sn_id = {}".format(s_basket_re[2] -( trans_detail[3] ) , s_basket_re[0] ))    
            db_conn.commit()  
            
        else :
            print('\n   You DID NOT Confirm Deleting Transaction.    ... Press any key')
        
    elif del_trans =='2' :
        
        print('\n\n    List of Selling Transactions we have, Select the ID to Delete it.') 
        show_all_trans ('Yes', '2')
        
        del_trans = input('\n     Enter the ID of a Selling Transaction to be Deleted.  [Q to exit]  > ')
        if del_trans in ['Q','q'] : return 
        
        # Get transaction Detail
        c.execute (" select * from sell_t_table where st_id  = {} ".format(del_trans))  
        trans_detail = c.fetchone()   
        c.execute (" select full_name from shares_name where s_id = {}".format(trans_detail[2])) 
        full_name = c.fetchone()
        print('\n                  ID:',trans_detail[0])
        print('          Share Date:',trans_detail[1])
        print('          Share Name:',full_name[0])
        print('        Share Amount:',format(trans_detail[3],','))
        print('               Price:',format(trans_detail[4],','))
        print('              Income:',format(trans_detail[5],','))
        
        if input('\n      Enter Y to Confirm and DELETE the Transaction.  [Y,N]  >  ') in ['y','Y'] :
            # Delete the Selling Transaction and Delete the Selling Record from Budget then Update the Shares Basket 
            
            # 1. Delete the Selling Transaction from Selling Table (buy_t_table).
            c.execute ("delete from sell_t_table where st_id ={}".format(int(del_trans))) 
            db_conn.commit()
            
            # 2. Delete the Selling Record from the Selling Table. 
            # 2.1. Get the Sell Record. 
            c.execute ("select * from budget_t where sell_date = '{}' and sell_amount = '{}' and sell_note like '[ Selling ]%' ". format(trans_detail[1],(-1* trans_detail[5])))
            budget_del = c.fetchall()
            
            # 2.2 Delete the Record from the Budget Table (budget_t).
            c.execute ("delete from budget_t where bud_id ={}".format(budget_del[0][0])) 
            db_conn.commit()
            
            # 3. Update the Share Basket Table (s_basket).
            # 3.1. Get the Record 
            c.execute("select * from s_basket where sn_id = {}".format(trans_detail[2]))    
            s_basket_re = c.fetchone()
             
            # 3.2. Update the Share Amount.  
            c.execute("update s_basket set ts_amount = {} where sn_id = {}".format(s_basket_re[2] + ( trans_detail[3] ) , s_basket_re[0] ))    
            db_conn.commit()  
          
        
    else : 
        print('\n        You Must Select 1 or 2.')    
  
    input('\n   ... Press any key to Exit.. ')  
  
# ============  = = = = = = = = = = = = = = = = = = = = = = = = =
    
def show_all_trans (inside = 'No', show='3'):
        
    if inside =='No' :
        os.system('clear') 
        print('\n   ====== Show Transactions  ======\n\n')
        print('   What type of Transaction to Show:\n       1. Buying Transaction.\n       2. Selling Transaction.\n       3. All Transactions.')  
        show = input('\n    Select Type of Transaction to Show. [Q to Exit]  >  ') 
        if show in ['q','Q'] : return    
    
    if show =='1' : 
        c.execute (" select * from buy_t_table where bt_id > 0 order by bt_id desc")  
        
        show_b_trans = c.fetchall()   
 
        print("\n",'      {:<10}{:<13}{:<30}{:<16}{:<11}{:<10}'.format('ID','Date','Share Name','Buy Amount','Price','Cost'))
        print("    ","-"*100)
        total_inv = 0
        try:
            for x in range(0,len(show_b_trans)) : 
                c.execute (" select full_name from shares_name where s_id = {}".format(show_b_trans[x][2])) 
                full_name = c.fetchone()
                print(" "*5,show_b_trans[x][0]," "*(5 - len(str(show_b_trans[x][0]))),show_b_trans[x][1]," "*3,full_name[0]," "*((30 - len(full_name[0]))+(0)) ,format(show_b_trans[x][3],",") ," "*((14 - len(str(format(show_b_trans[x][3],","))))),format(show_b_trans[x][4],',.2f') ," "*((11 - len(str(format(show_b_trans[x][4],',.2f'))))),format(show_b_trans[x][5],',.2f')) 
                total_inv +=show_b_trans[x][5]
                
            print("\n    ","-"*100)    
            print(" "*62,'Total Investment is:  {:,}'.format(total_inv))
                                  
            c.execute (" select * from budget_t where bud_id > 0") 
            the_budget = c.fetchall()
                        
            print(" "*58,'Net Budget Available is:  {:,}'.format(sum (the_budget[b][2] for b in range(len(the_budget))) - total_inv))
        except:
            pass
            
    if show =='2' : 
        c.execute (" select * from sell_t_table where st_id > 0 order by st_id desc")  
        show_s_trans = c.fetchall()   
     
        print('\n      {:<10}{:<13}{:<30}{:<16}{:<11}{:<10}'.format('ID','Date','Share Name','Sell Amount','Price','Income'))
        print("    ","-"*100)
        total_inc = 0
        try:
            for x in range(0,len(show_s_trans)) : 
                c.execute (" select full_name from shares_name where s_id = {}".format(show_s_trans[x][2])) 
                full_name = c.fetchone()
                print(" "*5,show_s_trans[x][0]," "*(5 - len(str(show_s_trans[x][0]))),show_s_trans[x][1]," "*3,full_name[0]," "*((30 - len(full_name[0]))+(0)) ,format(show_s_trans[x][3],",") ," "*((13 - len(str(show_s_trans[x][3])))),format(show_s_trans[x][4],',.2f') ," "*((9 - len(str(format(show_s_trans[x][4],',.2f'))))),format(show_s_trans[x][5],',.2f')) 
                total_inc +=show_s_trans[x][5]
            
            print("\n    ","-"*100)    
            print(" "*48,'Total Incomes from Selling Shares is {}'.format(total_inc))
            
        except:
            pass
        
    if show =='3' : 
        # Get All Sell Transactions Order by Selling Date desc
        c.execute (" select * from sell_t_table where st_id > 0 order by st_id desc") 
        show_s_trans = c.fetchall()   
            
        # Get All buy Transactions Order by Buying Date desc
        c.execute (" select * from buy_t_table where bt_id > 0 order by bt_id desc") 
        show_b_trans = c.fetchall()    
           
            records = (len(show_s_trans) if len(show_s_trans) >= len(show_b_trans) else len(show_b_trans))
                      
        print("\n"," "*11,"{:<9}{:<13}{:<30}{:<16}{:<11}{:<15}{}".format('ID','Date','Share Name','SAmount','Price','Cost','Income'))
        print("    ","-"*115)
        total_inc = 0
        total_inv = 0
        try:
            
            for x in range(records) :         
                try: 
                    
                    c.execute (" select full_name from shares_name where s_id = {}".format(show_s_trans[x][2])) 
                    full_name = c.fetchone()
                
                    print(" "*3,"Selling: ",show_s_trans[x][0]," "*(5 - len(str(show_s_trans[x][0]))),show_s_trans[x][1]," "*3,full_name[0]," "*((30 - len(full_name[0]))+(0)) ,show_s_trans[x][3] ," "*((13 - len(str(show_s_trans[x][3])))+(0)),show_s_trans[x][4] ," "*(8 - len(str(show_s_trans[x][4])))," - "," "*((13 - len(str(show_s_trans[x][4])))+(0)),show_s_trans[x][5]) 
                    total_inc += show_s_trans[x][5]
                
                except:
                    pass # if the x is out of range Do nothing
                 
                try: 
                    c.execute (" select full_name from shares_name where s_id = {}".format(show_b_trans[x][2])) 
                    full_name = c.fetchone()  
                    print(" "*4,"Buying: ",show_b_trans[x][0]," "*(5 -len(str(show_b_trans[x][0])) ),show_b_trans[x][1]," "*3,full_name[0]," "*((30 - len(full_name[0]))+(0)) ,show_b_trans[x][3] ," "*((13 - len(str(show_b_trans[x][3])))+(0)),show_b_trans[x][4] ," "*((8 - len(str(show_b_trans[x][4])))+(0)),show_b_trans[x][5]," "*(13 - len(str(show_b_trans[x][5])))," - ") 
                    total_inv += show_b_trans[x][5]
                
                except:
                    pass  # if the x is out of range Do nothing
                    
        except Exception as e:
            print('  ', e)
    
        print("\n    ","-"*115)
    
        print(" "*73,'Total Investment is: {:,}'.format(total_inv)) 
        print(" "*76,'Total Incomes is: {:,}'.format(total_inc))  
        print(" "*75,"-"*30,"\n"," "*75,'   Net Profit is: {:,} '.format(total_inc - total_inv))      
   
    if inside == 'No' : input('\n\n    .. Press any key to Exit. .. ')




def roi_info():
    os.system('clear')
    print('\n   ====== Shares  ROI ======\n\n')
    
    print('   Coming ... ')
    
    input('\n    Press any key to Exit .. ')
    
    

# ===================================================================================
    

"""
    TO RUN THE APPLICATION FOR FIRST TIME.. FOLLOW THE STEPS:

        1. Remove the HASH # from the Next two code lines [ create_tables_ , insert_record_0 () ]
        2. Run the Application. Then ENTER NUMBER ( 9 ) FROM THE MENU TO EXIT.
        3. RETURN THE HASH # to the line : [ create_tables_ , insert_record_0 () ]
        4. Run the Application and have fun.

"""

#create_tables_()
#insert_record_0 ()

# ............ .,.,.,.,.,.,.,.,,.,.,.,.,.,.


main_menu()
c.close()





