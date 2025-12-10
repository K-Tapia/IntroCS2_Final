from tkinter import messagebox
from Classes.user_class import User
def user_save(user:User)->None:
    """
    This function appends users to the users.txt file,
    if users.txt doesn't exist it creates it.
    """
    with open("users.txt", "a")as file:
        file.write(f'{user.get_username()}|{user.get_voted()}\n')

def user_read()->list:
    """
    This function reads users from users.txt with line splitting,
    it saves users into a list for later use
    if no users.txt just create the file
    :return: List of users
    """

    user_list=[]
    with open("users.txt","a+")as file:
        file.seek(0)
        for line in file:
            line=line.strip()
            username=line.split("|")[0]
            vote_status=line.split("|")[1]
            vote_bool=(vote_status=="True")
            user=User(username,vote_bool)
            user_list.append(user)
    return user_list

def user_voted(user_id:int)->None:
    """
    For the user_id entered, search users in user list and
    set voted from, False to True, for that user.
    Overwrite text file with the adjusted users list.
    :param user_id: str
    """
    users=user_read()
    for user in users:
        if user.get_username() == user_id:
            user.user_voted()
    with open("users.txt","w") as file:
        for user in users:
            file.write(f"{user.get_username()}|{user.get_voted()}\n")



def user_login(login_frame,main_window)->None:
    """
    (valid :4 number id)
    Validate the user entry from login page.
    Save the user id entered from login and create txt file to log it.
    Redirect to Vote Menu if valid.
    If invalid display error and stop this function before save/redirect.
    If user already exists, don't save, just redirect to vote_menu

    :param login_frame: Login frame
    :param main_window: (root)
    """
    user_entry= (login_frame.user_entry.get())
    if not (user_entry.isdigit() and len(user_entry)==4):
        #AI used for line 64 along with import associated with messagebox (line 1)
        messagebox.showerror("Invalid Entry","Please enter a valid numeric user id that is 4 characters in length")
        return
    main_window.current_user_id=user_entry
    user_list=user_read()
    user=User(user_entry)
    for u in user_list:
        if (u.get_username()==user_entry):
            main_window.show_frame(main_window.VOTE_MENU_CLASS)
            return
    user_save(user)
    main_window.show_frame(main_window.VOTE_MENU_CLASS)