from email import message
from re import X
import tkinter as tk
import sqlite3
from tkinter import messagebox
from turtle import title
import numpy as np
import matplotlib.pyplot as plt
import datetime





root = tk.Tk()
root.title('Finances')
root.geometry("")
root.resizable(width=False,height=False)


date_time = datetime.datetime.now()
data_base = 'income&expenses.db'
#create data-base
con = sqlite3.connect(data_base)

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Finances
                    (day real PRIMARY KEY, income real, expenses real)''')

def check_balance():
    
    con = sqlite3.connect(data_base)

    cur = con.cursor()


    cur.execute("SELECT * FROM Finances")
    Balance = cur.fetchall()


    User_balance_income = [x[1] for x in Balance]
    User_balance_expences = [x[2] for x in Balance]


    total_balance = sum(User_balance_income) - sum(User_balance_expences)
    current_balance = tk.Label(root, text=f'')
    current_balance = tk.Label(root, text=(f'${total_balance}'),font=20)
    current_balance.grid(row=0,column=2)


def graph():
    con = sqlite3.connect(data_base)
    cur = con.cursor()
    cur.execute("SELECT * FROM Finances")


    data_fetched = cur.fetchall()
    date_fetch = data_fetched[0]
    
    
    income_y = tuple([x[1] for x in data_fetched])
    expenses_y = tuple([x[2] for x in data_fetched])
    days = tuple([x[0] for x in data_fetched])

    plt.xlabel("Days")
    plt.ylabel("Income & Expenses")
    plt.title("Finances")
    plt.grid(True)
    plt.plot(days,income_y, color='blue', marker='o')
    plt.plot(days,expenses_y, color='red', marker='o')
    plt.show()
    
    con.commit()
    con.close()

def edit_record():
    editor = tk.Tk()
    editor.title('Editor')
    editor.geometry("300x300")
    def delete_all():
        con = sqlite3.connect(data_base)
        cur = con.cursor()
        warning_pop_up = messagebox.askyesno("Warning","Are you sure you want to delete all data" )
        if warning_pop_up == 1:

            cur.execute("DELETE from Finances")

        con.commit()
        con.close()
    delete_all_btn = tk.Button(editor,text="delete all records", command=delete_all)
    delete_all_btn.grid(row=0, column=0)
    delete_all_btn.place(relx=0.5,rely=0.5,anchor='center')



def delete():
    

    con = sqlite3.connect(data_base)
    cur = con.cursor()


    cur.execute("DELETE from Finances WHERE oid= " + id_select.get())

    con.commit()
    con.close()



# submit function for database
def submit():
    con = sqlite3.connect(data_base)
    cur = con.cursor()
    


    #insert to table
    cur.execute("INSERT INTO Finances VALUES (:date, :income, :expenses)",{'date': date.get(),'income': income.get(), 'expenses': expenses.get()})


    con.commit()
    con.close()



    #Clear the Text Boxes
    date.delete(0, tk.END)
    income.delete(0,tk.END)
    expenses.delete(0,tk.END)



# Create Query Function
def query():
    con = sqlite3.connect(data_base)
    cur = con.cursor()
    
    cur.execute("SELECT *, oid FROM Finances")
    finance_data = cur.fetchall()


    #loop thru results
    print_finance = ''
    for records in finance_data:
        print_finance += str(records[0:3]) + "\t" + str(records[3]) + "\n"
    

    query_label = tk.Label(root, text=print_finance)
    query_label.grid(row=8, column=0, columnspan=2)
    con.commit()
    con.close()




# Create Text boxes
date = tk.Entry(root, width=30)
date.grid(row=0, column=1, padx=20)

income = tk.Entry(root, width=30)
income.grid(row=1, column=1)

expenses = tk.Entry(root, width=30)
expenses.grid(row=2, column=1)

# Delete record entry text
id_select = tk.Entry(root, width=30)
id_select.grid(row=3, column=1, padx=10)



# Create Text Box Lables
id_select_label = tk.Label(root,text=" ID record")
id_select_label.grid(row=3, column=0)

date_label = tk.Label(root, text="Date")
date_label.grid(row=0,column=0)

income_label = tk.Label(root, text="Income")
income_label.grid(row=1,column=0)

expenses_label = tk.Label(root, text="Expsenses")
expenses_label.grid(row=2,column=0)


current_date_title = tk.Label(root, text="Current date")
current_date_title.grid(row=3, column=2)

current_date = tk.Label(root, text=f'{date_time.strftime("%m/%d/%y")}')
current_date.grid(row=4, column=2)



#check current balance
current_balance_btn = tk.Button(root, text="Check current balance", command=check_balance)
current_balance_btn.grid(row=2, column=2,padx=20)

#Create edit button
edit_btn = tk.Button(root, text="Edit record", command=edit_record)
edit_btn.grid(row=10,column=0,columnspan=2, pady=10,padx=10,ipadx=132)


#create delete
delete_btn = tk.Button(root, text="Delete record", command=delete)
delete_btn.grid(row=9,column=0,columnspan=2, pady=10, padx=10,ipadx=125)


#Create Submit button
sumit_btn = tk.Button(root, text="Add record to database", command=submit)
sumit_btn.grid(row=6, column=0, columnspan=2, pady=10,padx=10,ipadx=100)

# Create a Query Button
query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

#Graph button
graph_btn = tk.Button(root, text="Graph", command=graph)
graph_btn.grid(row=12, column=0,columnspan=2, pady=10,padx=10, ipadx=145 )


con.commit()

con.close()


root.mainloop()