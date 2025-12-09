import tkinter as tk
from Logic.login_functions import *
class Login(tk.Frame):
    def __init__(self, parent, controller)->None:
        """
        Custom Login Frame that appears when app first runs/user logout,
        any instance of lambda is to call a different frame
        to switch too
        :param parent: container from Main class
        :param controller: Main class is controller, switches frames
        """
        super().__init__(parent)
        main_window = controller
        inner=tk.Frame(self)
        inner.pack(expand=True)
        tk.Label(inner, text="Enter User for Login",font=("Times New Roman", 24)).pack(pady=10)
        tk.Label(inner, text="Create/Login User").pack(pady=10)
        self.user_entry=tk.Entry(inner)
        self.user_entry.pack(pady=10)
        proceed_btn= tk.Button(
            inner, text="proceed",
            command=lambda: [user_login(self,main_window),self.user_entry.delete(0, tk.END)]
        )
        proceed_btn.pack(pady=10)