# Python program to read in a blog post and instert it into the sql database

import mariadb
import sql_com_class
import os

# general syntax for connecting to MariaDB server
# mysql -u root -p
# USE to connect
# SHOW to display
# SELECT FROM to read
# DROP to delete

def clear_screen():
    _ = os.system("clear")

def menu(current_file,current_date,current_summary):
    menu_selection = 0

    print("Current file: {}".format(current_file))
    print("Current date: {}\n".format(current_date))
    print("Current summary: \n{}\n".format(current_summary))
    print("1. Enter file name.")
    print("2. Enter date.")
    print("3. Enter summary.")
    print("4. Read in mardown file.")
    print("5. List existing entries.")
    print("9. Quit.\n")
    try:
        menu_selection = int(input("Enter selection:> "))
    except:
        _ = input("Please make sure you entered a number between 1 and 4!")

    return menu_selection

def enter_file():
    try:
        file_name = input("Enter File Name:> ")
    except:
        _ = input("Please make sure you entered a string.")
    return file_name

def enter_date():
    try:
        date_name = input("Enter date:> ")
    except:
        _ = input("Please make sure you entered a string.")
    return date_name

def enter_summary():
    current_summary = input("Enter blog summary:\n\n")
    return current_summary

def read_markdown(current_file):
    dir_file = "./posts/"+current_file
    md_data = ""
    try:
        f = open(dir_file,"r")
        md_data = f.read()
    except:
        print("File was not read correctly")
        _ = input("")
    return md_data

def sql_input(current_date,current_summary,markdown_data):
    data = sql_com_class.database()
    data.connect()
    data.addTable(current_date)
    data.addData(current_date,current_summary,markdown_data)
    data.disconnect()

# Returns an array
def list_posts():
    tables_list = []
    data = sql_com_class.database()
    data.connect()
    tables_list = data.returnTables()
    print("\nList of Current Entries:\n")
    for i in tables_list:
        print(i)
    data.disconnect()
    _ = input("")

if __name__ == "__main__":
    menu_selection = 0
    current_file = ""
    current_date = ""
    current_summary = ""
    markdown_data = ""

    clear_screen()
    while(menu_selection != 9):
        clear_screen()
        menu_selection = menu(current_file,current_date,current_summary)
        if menu_selection == 1:
            current_file = enter_file()
        if menu_selection == 2:
            current_date = enter_date()
        if menu_selection == 3:
            current_summary = enter_summary()
        if menu_selection == 4: 
            markdown_data = read_markdown(current_file)
            print(markdown_data)
            sql_input(current_date,current_summary,markdown_data)
            _ = input("")
        if menu_selection == 5:
            list_posts()
