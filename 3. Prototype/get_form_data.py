def get_form_data_func(list_of_ent_fields, insert_form_data_func):
    """Gets the inputs from all the entry fields in a form and adds them to a list, then inserts the list's elements into a database table"""
    list_of_values = []  # stores the values of all the StringVars from list_of_fields
    for field_input in list_of_ent_fields:
        list_of_values.append(field_input.get())
    print(list_of_values)  # for testing purposes
    insert_form_data_func(list_of_values)  # insert_form_data_func is a function from library_database.py
