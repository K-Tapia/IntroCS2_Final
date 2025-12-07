import tkinter as tk
class Vote_Menu(tk.Frame):
    def __init__(self, parent, controller)->None:
        """
           Custom Vote Menu Frame that appears when app first runs/user logout,
           any instance of lambda is to call a different frame
           to switch too
           :param parent: container from Main class
           :param controller: Main class is controller, switches frames
           """

        super().__init__(parent)
        main_window=controller

        inner = tk.Frame(self)
        inner.pack(expand=True)
        label = tk.Label(inner, text="Voting Ballot", font=("Times New Roman", 24))
        label.pack(pady=20)

        vote_button = tk.Button(
            inner,
            text="Vote for Candidate",
            #lambda has to be used because class imports were causing circular errors
            #without lambda command triggers the function immediately at runtime
            command=lambda: main_window.show_frame(main_window.VOTE_CANDIDATE_CLASS)
        )
        vote_button.pack(pady=10)
        add_button = tk.Button(
            inner,
            text="Add Candidate",
            command=lambda:main_window.show_frame(main_window.ADD_CANDIDATE_CLASS)
        )
        add_button.pack(pady=10)
        view_button = tk.Button(
            inner,
            text="See Current Voting Poll",
            command=lambda:main_window.show_frame(main_window.VIEW_POLL_CLASS)
        )
        view_button.pack(pady=10)
        logout_button = tk.Button(
            inner,
            text="logout",
            command=lambda: main_window.show_frame(main_window.LOGIN_CLASS)
        )
        logout_button.pack(pady=10)
