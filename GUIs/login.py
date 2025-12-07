import tkinter as tk
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
        user_entry=tk.Entry(inner)
        user_entry.pack(pady=10)
        proceed_btn= tk.Button(
            inner, text="proceed",
            command=lambda: main_window.show_frame(main_window.VOTE_MENU_CLASS)
        )
        proceed_btn.pack(pady=10)