import tkinter as tk
from GUIs.vote_candidate import Candidate
class View_Poll(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        inner = tk.Frame(self)
        inner.pack(expand=True)
        #dummy data for gui
        candidate_dictionary = {
            "Joe Joe": Candidate("Joe ", "Joe", party="Democratic Party"),
            "Barry Allen": Candidate("Barry ", "Allen", party="Republican Party", vote=1), }
        vote=[]
        for name,candidate in candidate_dictionary.items():
            cvote=candidate.votes

            vote.append(cvote)

        highest_vote=max(vote)
        for vote_count in range(highest_vote,-1,-1):
            #^^^^^^ end of dummy data, can most likely make an importable function in different file.
            for name,candidate in candidate_dictionary.items():
                if vote_count==candidate.votes:
                    label=tk.Label(inner, text=f"{candidate.party}-{name}: {vote_count} votes")
                    label.pack(pady=10)




        return_button = tk.Button(
            inner,
            text="Return Home",
            command=lambda: self.controller.show_frame(controller.VOTE_MENU_CLASS)
        )
        return_button.pack(pady=10)