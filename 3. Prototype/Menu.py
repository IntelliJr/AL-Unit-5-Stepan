# "change password" button
# function that closes ANY current window and opens menu

import tkinter as tk
from tkinter import *
from tkinter import ttk
from library_database import insert_book_data, insert_member_data, insert_loan_data
from get_table_records import display_table_records
from switch_windows import back_to_menu, closing_using_x


def open_add_book_window():
    """Opens the add_book_window and closes the menu_window"""
    
    def get_book_data():
        """Gets the values of all StringVars in "Book data capture window" and adds them to a list, then inserts the list's elements into "Books" table"""
        list_of_stringvars = [isbn_ent_var, book_title_ent_var, series_ent_var, author_ent_var, genre_ent_var, publisher_ent_var, publication_date_ent_var,
                              price_ent_var, summary_ent_var, keywords_ent_var, cover_type_cbx_var, charge_if_lost_ent_var, charge_if_damaged_ent_var,
                              copies_owned_ent_var, copies_available_ent_var, date_added_ent_var]  # stores the names of all the StringVars
        list_of_values = []  # stores the values of all the StringVars from list_of_fields
        for stringvar in list_of_stringvars:
            list_of_values.append(stringvar.get())
        print(list_of_values)
        insert_book_data(list_of_values)  # imported from book_database
        list_of_values.clear()  # clears the list for next database record

    menu_window.withdraw()  # menu_window.destroy() | .withdraw() keeps the menu_window hidden -> needs to be revealed again when X is clicked, or else the program keeps running
    add_book_window = Tk()
    add_book_window.title("Book data capture window")

    # add_book_window - labels - instantiation
    isbn_lbl = Label(add_book_window, text="ISBN:")
    book_title_lbl = Label(add_book_window, text="Book title:")
    series_lbl = Label(add_book_window, text="Series:")
    author_lbl = Label(add_book_window, text="Author:")
    genre_lbl = Label(add_book_window, text="Genre:")
    publisher_lbl = Label(add_book_window, text="Publisher:")
    publication_date_lbl = Label(add_book_window, text="Publication date:")
    price_lbl = Label(add_book_window, text="Price:")
    summary_lbl = Label(add_book_window, text="Summary:")
    keywords_lbl = Label(add_book_window, text="Keywords:")
    cover_type_lbl = Label(add_book_window, text="Cover type:")
    charge_if_lost_lbl = Label(add_book_window, text="Charge if lost:")
    charge_if_damaged_lbl = Label(add_book_window, text="Charge if damaged:")
    copies_owned_lbl = Label(add_book_window, text="Copies owned:")
    copies_available_lbl = Label(add_book_window, text="Copies available:")
    date_added_lbl = Label(add_book_window, text="Date added:")

    # add_book_window geometry - labels - geometry
    isbn_lbl.grid(row=0, column=0, padx=5, pady=5)
    book_title_lbl.grid(row=1, column=0, padx=5, pady=5)
    series_lbl.grid(row=2, column=0, padx=5, pady=5)
    author_lbl.grid(row=3, column=0, padx=5, pady=5)
    genre_lbl.grid(row=4, column=0, padx=5, pady=5)
    publisher_lbl.grid(row=5, column=0, padx=5, pady=5)
    publication_date_lbl.grid(row=6, column=0, padx=5, pady=5)
    price_lbl.grid(row=7, column=0, padx=5, pady=5)
    summary_lbl.grid(row=8, column=0, padx=5, pady=5)
    keywords_lbl.grid(row=9, column=0, padx=5, pady=5)
    cover_type_lbl.grid(row=10, column=0, padx=5, pady=5)
    charge_if_lost_lbl.grid(row=11, column=0, padx=5, pady=5)
    charge_if_damaged_lbl.grid(row=12, column=0, padx=5, pady=5)
    copies_owned_lbl.grid(row=13, column=0, padx=5, pady=5)
    copies_available_lbl.grid(row=14, column=0, padx=5, pady=5)
    date_added_lbl.grid(row=15, column=0, padx=5, pady=5)

    # add_book_window - entry fields - instantiation & StringVars
    isbn_ent_var = StringVar()
    isbn_ent = Entry(add_book_window, textvariable=isbn_ent_var)
    book_title_ent_var = StringVar()
    book_title_ent = Entry(add_book_window, textvariable=book_title_ent_var)
    series_ent_var = StringVar()
    series_ent = Entry(add_book_window, textvariable=series_ent_var)
    author_ent_var = StringVar()
    author_ent = Entry(add_book_window, textvariable=author_ent_var)
    genre_ent_var = StringVar()
    genre_ent = Entry(add_book_window, textvariable=genre_ent_var)
    publisher_ent_var = StringVar()
    publisher_ent = Entry(add_book_window, textvariable=publisher_ent_var)
    publication_date_ent_var = StringVar()
    publication_date_ent = Entry(add_book_window, textvariable=publication_date_ent_var)  # date picker?
    price_ent_var = StringVar()
    price_ent = Entry(add_book_window, textvariable=price_ent_var)
    summary_ent_var = StringVar()
    summary_ent = Entry(add_book_window, textvariable=summary_ent_var)
    keywords_ent_var = StringVar()
    keywords_ent = Entry(add_book_window, textvariable=keywords_ent_var)
    cover_type_cbx_var = StringVar()
    cover_type_cbx = ttk.Combobox(add_book_window, values=["Paperback", "Hardback"], textvariable=cover_type_cbx_var)
    charge_if_lost_ent_var = StringVar()
    charge_if_lost_ent = Entry(add_book_window, textvariable=charge_if_lost_ent_var)
    charge_if_damaged_ent_var = StringVar()
    charge_if_damaged_ent = Entry(add_book_window, textvariable=charge_if_damaged_ent_var)
    copies_owned_ent_var = StringVar()
    copies_owned_ent = Entry(add_book_window, textvariable=copies_owned_ent_var)
    copies_available_ent_var = StringVar()
    copies_available_ent = Entry(add_book_window, textvariable=copies_available_ent_var)
    date_added_ent_var = StringVar()
    date_added_ent = Entry(add_book_window, textvariable=date_added_ent_var)

    # add_book_window - entry fields - geometry
    isbn_ent.grid(row=0, column=1, padx=5, pady=5)
    book_title_ent.grid(row=1, column=1, padx=5, pady=5)
    series_ent.grid(row=2, column=1, padx=5, pady=5)
    author_ent.grid(row=3, column=1, padx=5, pady=5)
    genre_ent.grid(row=4, column=1, padx=5, pady=5)
    publisher_ent.grid(row=5, column=1, padx=5, pady=5)
    publication_date_ent.grid(row=6, column=1, padx=5, pady=5)
    price_ent.grid(row=7, column=1, padx=5, pady=5)
    summary_ent.grid(row=8, column=1, padx=5, pady=5)
    keywords_ent.grid(row=9, column=1, padx=5, pady=5)
    cover_type_cbx.grid(row=10, column=1, padx=5, pady=5)
    charge_if_lost_ent.grid(row=11, column=1, padx=5, pady=5)
    charge_if_damaged_ent.grid(row=12, column=1, padx=5, pady=5)
    copies_owned_ent.grid(row=13, column=1, padx=5, pady=5)
    copies_available_ent.grid(row=14, column=1, padx=5, pady=5)
    date_added_ent.grid(row=15, column=1, padx=5, pady=5)

    # add_book_window - buttons - instantiation
    book_insert_database_btn = Button(add_book_window, text="Save to the database", command=get_book_data)
    back_to_menu_btn = Button(add_book_window, text="Back to Menu", command=lambda: back_to_menu(add_book_window, menu_window))  # imported from switch_windows.py

    # add_book_window geometry - buttons - geometry
    book_insert_database_btn.grid(row=16, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=16, column=1, padx=5, pady=5)

    add_book_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(add_book_window, menu_window))  # imported from switch_windows.py
    add_book_window.mainloop()
    
    
def open_add_member_window():
    """Opens the add_member_window and closes the menu_window"""

    def get_member_data():
        """Gets the values of all StringVars in "Member data capture window" and adds them to a list, then inserts the list's elements into "Members" table"""
        list_of_stringvars = [member_title_ent_var, first_name_ent_var, last_name_ent_var, date_of_birth_ent_var,
                              email_lbl_ent_var, school_year_ent_var,
                              member_type_ent_var]  # stores the names of all the StringVars
        list_of_values = []  # stores the values of all the StringVars from list_of_stringvars
        for stringvar in list_of_stringvars:
            list_of_values.append(stringvar.get())
        print(list_of_values)
        insert_member_data(list_of_values)  # imported from library_database
        list_of_values.clear()  # clears the list for next database record

    menu_window.withdraw()
    add_member_window = Tk()
    add_member_window.title("Member data capture window")
    
    # add_member_window - labels - instantiation
    member_id_lbl = Label(add_member_window, text="Member ID:")
    member_title_lbl = Label(add_member_window, text="Member title:")
    first_name_lbl = Label(add_member_window, text="First name:")
    last_name_lbl = Label(add_member_window, text="Last name:")
    date_of_birth_lbl = Label(add_member_window, text="Date of birth:")
    email_lbl = Label(add_member_window, text="Email:")
    school_year_lbl = Label(add_member_window, text="School year (if applicable):")
    member_type_lbl = Label(add_member_window, text="Member type:")
    
    # add_member_window - labels - geometry
    member_id_lbl.grid(row=0, column=0, padx=5, pady=5)
    member_title_lbl.grid(row=1, column=0, padx=5, pady=5)
    first_name_lbl.grid(row=2, column=0, padx=5, pady=5)
    last_name_lbl.grid(row=3, column=0, padx=5, pady=5)
    date_of_birth_lbl.grid(row=4, column=0, padx=5, pady=5)
    email_lbl.grid(row=5, column=0, padx=5, pady=5)
    school_year_lbl.grid(row=6, column=0, padx=5, pady=5)
    member_type_lbl.grid(row=7, column=0, padx=5, pady=5)
    
    # add_member_window - entry fields - instantiation & StringVars
    member_id_ent_var = StringVar()
    member_id_ent = Entry(add_member_window, textvariable=member_id_ent_var)
    member_title_ent_var = StringVar()
    member_title_ent = Entry(add_member_window, textvariable=member_title_ent_var)
    first_name_ent_var = StringVar()
    first_name_ent = Entry(add_member_window, textvariable=first_name_ent_var)
    last_name_ent_var = StringVar()
    last_name_ent = Entry(add_member_window, textvariable=last_name_ent_var)
    date_of_birth_ent_var = StringVar()
    date_of_birth_ent = Entry(add_member_window, textvariable=date_of_birth_ent_var)
    email_lbl_ent_var = StringVar()
    email_lbl_ent = Entry(add_member_window, textvariable=email_lbl_ent_var)
    school_year_ent_var = StringVar()
    school_year_ent = Entry(add_member_window, textvariable=school_year_ent_var)
    member_type_ent_var = StringVar()
    member_type_ent = Entry(add_member_window, textvariable=member_type_ent_var)
    
    # add_member_window - entry fields - geometry
    member_id_ent.grid(row=0, column=1, padx=5, pady=5)
    member_title_ent.grid(row=1, column=1, padx=5, pady=5)
    first_name_ent.grid(row=2, column=1, padx=5, pady=5)
    last_name_ent.grid(row=3, column=1, padx=5, pady=5)
    date_of_birth_ent.grid(row=4, column=1, padx=5, pady=5)
    email_lbl_ent.grid(row=5, column=1, padx=5, pady=5)
    school_year_ent.grid(row=6, column=1, padx=5, pady=5)
    member_type_ent.grid(row=7, column=1, padx=5, pady=5)
    
    # add_member_window - buttons - instantiation
    member_insert_btn = Button(add_member_window, text="Save to the database", command=get_member_data)
    back_to_menu_btn = Button(add_member_window, text="Back to Menu", command=lambda: back_to_menu(add_member_window, menu_window))  # imported from switch_windows.py
    
    # add_member_window - buttons - geometry
    member_insert_btn.grid(row=8, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=8, column=1, padx=5, pady=5)

    add_member_window.protocol("WM_DELETE_WINDOW",lambda: closing_using_x(add_member_window, menu_window))  # imported from switch_windows.py
    add_member_window.mainloop()
    
    
def open_add_loan_window():
    """Opens the add_loan_window and closes the menu_window"""
    
    def get_loan_data():
        """Gets the values of all StringVars in "Loan data capture window" and adds them to a list, then inserts the list's elements into "Loans" table"""
        list_of_stringvars = [loan_id_ent_var, loan_date_ent_var, loan_duration_ent_var, due_for_return_ent_var, is_damaged_ent_var, is_lost_ent_var, isbn_ent_var, member_id_ent_var]  # add names of stringvars
        list_of_values = []
        for stringvar in list_of_stringvars:
            list_of_values.append(stringvar.get())
        print(list_of_values)
        insert_loan_data(list_of_values)
        list_of_values.clear()
    
    menu_window.withdraw()
    add_loan_window = Tk()
    add_loan_window.title("Loan data capture window")
    
    # add_loan_window - labels - instantiation
    loan_id_lbl = Label(add_loan_window, text="Loan ID:")
    loan_date_lbl = Label(add_loan_window, text="Loan date:")
    loan_duration_lbl = Label(add_loan_window, text="Loan duration:")
    due_for_return_lbl = Label(add_loan_window, text="Due for return:")
    is_damaged_lbl = Label(add_loan_window, text="Is damaged:")
    is_lost_lbl = Label(add_loan_window, text="Is lost:")
    isbn_lbl = Label(add_loan_window, text="ISBN:")
    member_id_lbl = Label(add_loan_window, text="Member ID:")
    
    # add_loan_window - labels - geometry
    loan_id_lbl.grid(row=0, column=0, padx=5, pady=5)
    loan_date_lbl.grid(row=1, column=0, padx=5, pady=5)
    loan_duration_lbl.grid(row=2, column=0, padx=5, pady=5)
    due_for_return_lbl.grid(row=3, column=0, padx=5, pady=5)
    is_damaged_lbl.grid(row=4, column=0, padx=5, pady=5)
    is_lost_lbl.grid(row=5, column=0, padx=5, pady=5)
    isbn_lbl.grid(row=6, column=0, padx=5, pady=5)
    member_id_lbl.grid(row=7, column=0, padx=5, pady=5)
    
    # add_loan_window - entry fields - instantiation and StringVars
    loan_id_ent_var = StringVar()
    loan_id_ent = Entry(add_loan_window, textvariable=loan_id_ent_var)
    loan_date_ent_var = StringVar()
    loan_date_ent = Entry(add_loan_window, textvariable=loan_date_ent_var)
    loan_duration_ent_var = StringVar()
    loan_duration_ent = Entry(add_loan_window, textvariable=loan_duration_ent_var)
    due_for_return_ent_var = StringVar()
    due_for_return_ent = Entry(add_loan_window, textvariable=due_for_return_ent_var)
    is_damaged_ent_var = StringVar()
    is_damaged_ent = Entry(add_loan_window, textvariable=is_damaged_ent_var)
    is_lost_ent_var = StringVar()
    is_lost_ent = Entry(add_loan_window, textvariable=is_lost_ent_var)
    isbn_ent_var = StringVar()
    isbn_ent = Entry(add_loan_window, textvariable=isbn_ent_var)
    member_id_ent_var = StringVar()
    member_id_ent = Entry(add_loan_window, textvariable=member_id_ent_var)
    
    # add_loan_window - entry fields - geometry
    loan_id_ent.grid(row=0, column=1, padx=5, pady=5)
    loan_date_ent.grid(row=1, column=1, padx=5, pady=5)
    loan_duration_ent.grid(row=2, column=1, padx=5, pady=5)
    due_for_return_ent.grid(row=3, column=1, padx=5, pady=5)
    is_damaged_ent.grid(row=4, column=1, padx=5, pady=5)
    is_lost_ent.grid(row=5, column=1, padx=5, pady=5)
    isbn_ent.grid(row=6, column=1, padx=5, pady=5)
    member_id_ent.grid(row=7, column=1, padx=5, pady=5)
    
    # add_loan_window - buttons - instantiation
    loan_insert_btn = Button(add_loan_window, text="Save to the database", command=get_loan_data)
    back_to_menu_btn = Button(add_loan_window, text="Back to Menu", command=lambda: back_to_menu(add_loan_window, menu_window))  # imported from switch_windows.py
    
    
    # add_loan_window - buttons - geometry
    loan_insert_btn.grid(row=8, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=8, column=1, padx=5, pady=5)
    
    add_loan_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(add_loan_window, menu_window))  # imported from switch_windows.py
    add_loan_window.mainloop()
    
    
def open_add_book_request_window():
    """Opens the add_book_request_window and closes the menu_window"""
    menu_window.withdraw()
    add_book_request_window = Tk()
    book_request_test_lbl = Label(add_book_request_window, text="book request test").pack()

    add_book_request_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(add_book_request_window, menu_window))  # imported from switch_windows.py
    add_book_request_window.mainloop()
    
    
def open_view_books_table_window():
    """Opens the view_books_table_window and closes the menu_window"""
    menu_window.withdraw()
    view_books_table_window = Tk()
    view_books_table_window.title("View Books Table")
    
    # .column(minwidth=0, width=100, stretch=NO)
    # Treeview:
    view_books_table_treeview = ttk.Treeview(view_books_table_window, columns=("col_1", "col_2", "col_3", "col_4",
                                                                               "col_5", "col_6", "col_7", "col_8",
                                                                               "col_9", "col_10", "col_11", "col_12",
                                                                               "col_13", "col_14", "col_15", "col_16"),
                                             show='headings')
    view_books_table_treeview.column("#1", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#1", text="ISBN")
    view_books_table_treeview.column("#2", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#2", text="BookTitle")
    view_books_table_treeview.column("#3", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#3", text="Series")
    view_books_table_treeview.column("#4", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#4", text="Author")
    view_books_table_treeview.column("#5", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#5", text="Genre")
    view_books_table_treeview.column("#6", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#6", text="Publisher")
    view_books_table_treeview.column("#7", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#7", text="PublicationDate")
    view_books_table_treeview.column("#8", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#8", text="Price")
    view_books_table_treeview.column("#9", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#9", text="Summary")
    view_books_table_treeview.column("#10", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#10", text="Keywords")
    view_books_table_treeview.column("#11", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#11", text="CoverType")
    view_books_table_treeview.column("#12", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#12", text="ChargeIfLost")
    view_books_table_treeview.column("#13", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#13", text="ChargeIfDamaged")
    view_books_table_treeview.column("#14", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#14", text="CopiesOwned")
    view_books_table_treeview.column("#15", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#15", text="CopiesAvailable")
    view_books_table_treeview.column("#16", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#16", text="DateAdded")

    view_books_table_treeview.grid(row=0, column=0, padx=5, pady=5)
    display_books_table_btn = Button(view_books_table_window, text="Display data", command=lambda: display_table_records("Books", view_books_table_treeview, tk.END))  # imported from get_table_records.py
    back_to_menu_btn = Button(view_books_table_window, text="Back to Menu", command=lambda: back_to_menu(view_books_table_window, menu_window))
    display_books_table_btn.grid(row=1, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=2, column=0, padx=5, pady=5)

    view_books_table_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(view_books_table_window, menu_window))  # imported from switch_windows.py
    view_books_table_window.mainloop()


def open_view_members_table_window():
    menu_window.withdraw()
    view_members_table_window = Tk()
    view_members_table_window.title("View Members Table")

    # Treeview
    view_members_table_treeview = ttk.Treeview(view_members_table_window, columns=("col_1", "col_2", "col_3", "col_4",
                                                                                   "col_5", "col_6", "col_7"),
                                               show="headings")
    #view_members_table_treeview.column("#1", anchor=CENTER, width=100, stretch=NO)
    #view_members_table_treeview.heading("#1", text="MemberID")
    view_members_table_treeview.column("#1", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#1", text="MemberTitle")
    view_members_table_treeview.column("#2", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#2", text="FirstName")
    view_members_table_treeview.column("#3", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#3", text="LastName")
    view_members_table_treeview.column("#4", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#4", text="DateOfBirth")
    view_members_table_treeview.column("#5", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#5", text="Email")
    view_members_table_treeview.column("#6", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#6", text="SchoolYear")
    view_members_table_treeview.column("#7", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#7", text="MemberType")

    view_members_table_treeview.grid(row=0, column=0, padx=5, pady=5)

    # view_members_table_window - buttons - instantiation
    display_members_table_btn = Button(view_members_table_window, text="Display data", command=lambda: display_table_records("Members", view_members_table_treeview, tk.END))  # imported from get_table_records.py
    back_to_menu_btn = Button(view_members_table_window, text="Back to Menu", command=lambda: back_to_menu(view_members_table_window, menu_window))

    # view_members_table_window - buttons - geometry
    display_members_table_btn.grid(row=1, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=2, column=0, padx=5, pady=5)

    view_members_table_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(view_members_table_window, menu_window))  # imported from switch_windows.py
    view_members_table_window.mainloop()


#def open_menu_window():
#   """Opens menu_window"""
menu_window = Tk()
menu_window.title("Menu")
menu_window.resizable(width=False, height=False)

# menu_window - buttons - instantiation
add_book_btn = Button(menu_window, text="Add a new book", command=open_add_book_window)
add_member_btn = Button(menu_window, text="Add a new member", command=open_add_member_window)
add_loan_btn = Button(menu_window, text="Add a new loan", command=open_add_loan_window)
add_request_btn = Button(menu_window, text="Add a new book request (not working)", command=open_add_book_request_window)
close_menu_btn = Button(menu_window, text="Close Menu", command=menu_window.destroy)
view_books_table_btn = Button(menu_window, text="View Books table", command=open_view_books_table_window)
view_members_table_btn = Button(menu_window, text="View Members table", command=open_view_members_table_window)
view_loans_table_btn = Button(menu_window, text="View Loans table")
view_book_requests_table_btn = Button(menu_window, text="View Book Requests table (not working)")

# menu_window - buttons - geometry
add_book_btn.grid(row=0, column=0, padx=5, pady=5)
add_member_btn.grid(row=0, column=1, padx=5, pady=5)
add_loan_btn.grid(row=0, column=2, padx=5, pady=5)
add_request_btn.grid(row=0, column=3, padx=5, pady=5)
close_menu_btn.grid(row=0, column=4, padx=5, pady=5)
view_books_table_btn.grid(row=1, column=0, padx=5, pady=5)
view_members_table_btn.grid(row=1, column=1, padx=5, pady=5)
view_loans_table_btn.grid(row=1, column=2, padx=5, pady=5)
view_book_requests_table_btn.grid(row=1, column=3, padx=5, pady=5)

menu_window.mainloop()
