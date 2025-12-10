from tkinter.messagebox import showerror

from Logic.add_candidate_functions import candidate_read
from Classes.candidate_class import Candidate
from Logic.login_functions import user_voted,user_read
from tkinter import messagebox
import tkinter as tk
def candidate_dictionary()->dict:
    """
    This function serves the purpose of creating a dictionary of candidates.
    It first combines the values of first and last name like this "John Doe", in
    order to create a fullname
    the dictionary has a format of Fullname:Candidate(object).
    :return: dictionary
    """
    candid=candidate_read()
    candid_dict={}
    for candidate in candid:
        fullname=f"{candidate.get_first_name()} {candidate.get_last_name()}"
        candid_dict[fullname]=candidate
    return candid_dict
def submit_vote(frame,root)->None:
    """
    What this function does is first reading the user text file, gathering a list of users
    and checking to see if the saved user from login matches any in the list. If it matches any in the list,
    the function checks if user.voted is False or True, if True display the message box error and stop the function.
    if user is not True the function will update the user to True. Voted_for takes the value of the radio btn that is selected,
    if no input messagebox error to select a candidate. then use candidate_dictionary to save a dictionary of candidates by fullname: and candidate object.
    if full name equals to the full name value in the radio button increment vote count by 1.
    write out to candidates.txt to update vote count.
    :param frame:
    :param root:
    """
    users = user_read()
    for u in users:
        if root.current_user_id == u.get_username():
            if u.get_voted():
                messagebox.showerror("Voted", "You have already voted")
                return
    user_voted(root.current_user_id)

    voted_for=frame.selected_candid.get()
    if not voted_for:
        messagebox.showerror("Input Error","Please select a candidate for voting")
    candid_dict=candidate_dictionary()
    for name,candidate in candid_dict.items():
        if name==voted_for:
            candidate.increase_votes()
            break

    with open("candidates.txt","w") as file:
        for candidate in candid_dict.values():
            file.write(f"{candidate.get_first_name()}|{candidate.get_last_name()}|{candidate.get_party()}|{candidate.get_votes()}\n")


