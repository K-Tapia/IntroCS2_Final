from Classes.candidate_class import Candidate
from tkinter import messagebox
import tkinter as tk
def candidate_save(candidate: Candidate)->None:
    """
    save candidate by appending them to a candidates.txt file
    :param candidate:
    """
    with open("candidates.txt", "a") as file:
        file.write(f"{candidate.get_first_name()}|{candidate.get_last_name()}|{candidate.get_party()}|{candidate.get_votes()}\n")
def validate_name(name:str)->str|None:
    """
    This function validates if the name entered is solely letters, no spaces or numbers allowed since isalpha() is called,
    if the name isnt valid display an error message box
    and return none
    if valid return name but capitalize the first letter in the string
    :param name: str
    :return: str or None
    """
    #AI used for line 8 and 11, simpler way to check for letters and capitalize starting letter in name
    if not name.isalpha():
        messagebox.showerror("Input Error","Please enter a valid name (letters only)")
        return None
    return name.capitalize()

def candidate_read()->list:
    """
    This file use a+ to read candidates.txt file, if candidates.txt does
    not exist, a+ creates the file. Split the txt file contents to retrieve
    candidates class values. Append the candidates to a list and return it
    :return: List
    """
    with open ("candidates.txt","a+") as file:
        file.seek(0)
        candidate_list=[]
        for line in file:
            line=line.strip()
            firstname=line.split("|")[0]
            lastname=line.split("|")[1]
            party=line.split("|")[2]
            votes=line.split("|")[3]
            votes=int(votes)
            candidate=Candidate(firstname,lastname,party,votes)
            candidate_list.append(candidate)
        return candidate_list



def candidate_add(add_candid,main_window):
    """
    This serves to be functionality for when a button gets pressed
    first call functions to validate the user inputs, if user inputs are invalid
    stop the function. After read candidates.txt file and log any candidates in an array.
    Check for similar first names, if similar first names check the last name, if first and last name are similar,
    show an error message showing that candidate already exists.
    Otherwise save candidate and add it to the txt file. display a message box showing success.
    clear all content in the add_candidate entry fields and redirect to the vote menu.
    :param add_candid: frame
    :param main_window: root window
    :return: none
    """
    firstname=validate_name(add_candid.first_name_input.get())
    if firstname==None:
        return
    lastname=validate_name(add_candid.last_name_input.get())
    if lastname==None:
        return
    party=add_candid.party_checkbox_val.get()
    if party=="N/A":
        messagebox.showerror("Choice Error","Please select a Party Affiliation")
        return
    candidate_list=candidate_read()
    for candidate in candidate_list:
        if candidate.get_first_name()==firstname:
            if candidate.get_last_name()==lastname:
                messagebox.showerror("Save Error","This candidate already exists")
                return
    candidate=Candidate(firstname,lastname,party)
    candidate_save(candidate)
    messagebox.showinfo("Success","Candidate Added Successfully")
    add_candid.first_name_input.delete(0, tk.END)
    add_candid.last_name_input.delete(0, tk.END)
    add_candid.party_checkbox_val.set("N/A")
    main_window.show_frame(main_window.VOTE_MENU_CLASS)
def return_btn(add_candid,main_window)->None:
    """
    when you press return button in add candidate, clear all content
    in the entry fields and return to the vote menu
    :param add_candid: frame
    :param main_window: root window    """
    add_candid.first_name_input.delete(0, tk.END)
    add_candid.last_name_input.delete(0, tk.END)
    add_candid.party_checkbox_val.set("N/A")
    main_window.show_frame(main_window.VOTE_MENU_CLASS)




