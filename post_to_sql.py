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

def menu(file_name,table_name,post_date,post_title,post_summary):
    menu_selection = 0

    print("File Name: {}".format(file_name))
    print("Table name: {}".format(table_name))
    print("Post date: {}".format(post_date))
    print("Post title: {}".format(post_title))
    print("Post summary: \n{}\n".format(post_summary))
    print("1. Enter file name.")
    print("2. Enter table name (P200723)")
    print("3. Enter post date.")
    print("4. Enter post title.")
    print("5. Enter post summary.")
    print("6. Read in mardown file.")
    print("7. List existing entries.")
    print("9. Quit.\n")
    try:
        menu_selection = int(input("Enter selection:> "))
    except:
        _ = input("Please make sure you entered a number between 1 and 4!")

    return menu_selection

def enter_file():
    try:
        file_name = input("Enter File Name to be read:> ")
    except:
        _ = input("Please make sure you entered a string.")
    return file_name

def enter_tablename():
    try:
        table_name = input("Enter table name:> ")
    except:
        _ = input("Please make sure you entered a string.")
    return table_name

def enter_date():
    try:
        date_name = input("Enter post date:> ")
    except:
        _ = input("Please make sure you entered a string.")
    return date_name

def enter_title():
    try:
        post_title = input("Enter post title:> ")
    except:
        _ = input("Please make sure you entered a string.")
    return post_title

def enter_summary():
    current_summary = input("Enter blog post summary:\n\n")
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

def sql_input(table_name,post_date,post_title,post_summary,markdown_data):
    data = sql_com_class.database()
    data.connect()
    data.addTable(table_name)
    data.addData(table_name,post_date,post_title,post_summary,markdown_data)
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
    file_name = ""
    table_name = ""
    post_date = ""
    post_title = ""
    post_summary = ""
    markdown_data = ""

    clear_screen()
    while(menu_selection != 9):
        clear_screen()
        menu_selection = menu(file_name,table_name,post_date,post_title,post_summary)
        if menu_selection == 1:
            file_name = enter_file()
        if menu_selection == 2:
            table_name = enter_tablename()
        if menu_selection == 3:
            post_date = enter_date()
        if menu_selection == 4:
            post_title = enter_title()
        if menu_selection == 5:
            post_summary = enter_summary()
        if menu_selection == 6: 
            markdown_data = read_markdown(file_name)
            print(markdown_data)
            sql_input(table_name,post_date,post_title,post_summary,markdown_data)
            _ = input("")
        if menu_selection == 7:
            list_posts()
