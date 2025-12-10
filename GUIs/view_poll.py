import tkinter as tk
from GUIs.vote_candidate import Candidate
from Logic.vote_candid_functions import candidate_dictionary
class View_Poll(tk.Frame):
    def __init__(self, parent, controller):
        """
           Custom View Poll Frame that appears when app first runs/user logout,
           any instance of lambda is to call a different frame
           to switch too
           :param parent: container from Main class
           :param controller: Main class is controller, switches frames
           """
        super().__init__(parent)
        self.controller = controller
        inner = tk.Frame(self)
        inner.pack(expand=True)
        self.label=tk.Frame(inner)
        self.label.pack(pady=10)

        return_button = tk.Button(
            inner,
            text="Return Home",
            command=lambda: self.controller.show_frame(controller.VOTE_MENU_CLASS)
        )
        return_button.pack(pady=10,anchor="w")
        self.refresh()
    def refresh(self)->None:
        """
        Pretty similar to the other refresh in vote_candidate
        deletes widgets held in self.label
        then refills self.label with content.
        checks candidate dictionary and appends votes into a vote list
        check to see the highest value in the list. from there each individual
        vote is organized from greatest to least
        then check to see if candidate has votes and add text to a label
        if no candidates simply show no candidates available
        :return:None
        """
        for widget in self.label.winfo_children():
            widget.destroy()
        vote = []
        candidate_dict = candidate_dictionary()
        for name, candidate in candidate_dict.items():
            cvote = candidate.get_votes()
            vote.append(cvote)

        if vote:
            highest_vote = max(vote)
            for vote_count in range(highest_vote, -1, -1):
                for name, candidate in candidate_dict.items():
                    if vote_count == candidate.get_votes():
                        label = tk.Label(self.label, text=f"{candidate.get_party()}-{name}: {vote_count} votes")
                        label.pack(pady=10)
        else:
            tk.Label(self.label, text="No candidates available").pack(pady=10)