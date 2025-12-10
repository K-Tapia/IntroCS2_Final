import tkinter as tk
from Logic.add_candidate_functions import *
class Add_Candidate(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        main_window = controller
        inner = tk.Frame(self)
        inner.pack(expand=True)
        tk.Label(inner, text="Add Candidate",font=("Times New Roman", 24)).pack(pady=10)
        first_name_label = tk.Label(inner, text="First Name")
        self.first_name_input= tk.Entry(inner)
        first_name_label.pack(pady=10)
        self.first_name_input.pack(pady=10)

        last_name_label = tk.Label(inner, text="Last Name")
        self.last_name_input= tk.Entry(inner)
        last_name_label.pack(pady=10)
        self.last_name_input.pack(pady=10)

        self.party_checkbox_val=tk.StringVar(value="N/A")
        party_affiliate_label= tk.Label(inner, text="Party Affiliation")
        party_affiliate_label.pack(pady=10)
        demcrat_checkbox= tk.Radiobutton(inner, text="Democratic Party",
                                         variable=self.party_checkbox_val,value="Democratic Party")
        demcrat_checkbox.pack(pady=10)

        republic_checkbox= tk.Radiobutton(inner, text="Republican Party",
                                         variable=self.party_checkbox_val,value="Republican Party")
        republic_checkbox.pack(pady=10)
        independent_checkbox= tk.Radiobutton(inner, text="Independent Party",
                                         variable=self.party_checkbox_val,value="Independent Party")
        independent_checkbox.pack(pady=10)

        save_button= tk.Button(inner, text="Save Candidate",
                               command=lambda:candidate_add(self,main_window))#adjust functionality later
        save_button.pack(pady=10)

        return_button = tk.Button(
            inner,
            text="See Current Voting Poll",
            command=lambda: return_btn(self,main_window)
        )
        return_button.pack(pady=10)