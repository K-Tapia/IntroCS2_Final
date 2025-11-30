import tkinter as tk

class Candidate:
    def __init__(self, firstname, lastname, party, vote=0):
        self.firstname = firstname
        self.lastname = lastname
        self.party = party
        self.votes = vote

    def vote(self):
        self.votes += 1

class Vote_Candidate(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        #dummy data
        candidate_dictionary={
            "Joe Joe":Candidate("Joe ", "Joe", party="Democratic Party"),
            "Barry Allen":Candidate("Barry ", "Allen", party="Republican Party"),}
        checkbox_vars = {}


        inner = tk.Frame(self)
        inner.pack(expand=True)
        tk.Label(inner, text="Candidates",font=("Times New Roman", 24)).pack(pady=10)

        for name, candidate in candidate_dictionary.items():
            var = tk.BooleanVar()
            checkbox_vars[name] = var
            cb = tk.Checkbutton(inner, text=f"{name} ({candidate.party})", variable=var)
            cb.pack(anchor="w")


        return_button = tk.Button(
            inner,
            text="See Current Voting Poll",
            command=lambda: self.controller.show_frame(controller.VOTE_MENU_CLASS)
        )
        return_button.pack(pady=10)
