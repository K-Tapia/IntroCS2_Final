import tkinter as tk

from Logic.vote_candid_functions import *


class Vote_Candidate(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.selected_candid = tk.StringVar(self)

        inner = tk.Frame(self)
        inner.pack(expand=True)
        tk.Label(inner, text="Candidates", font=("Times New Roman", 24)).pack(pady=10)

        self.radio_button_container = tk.Frame(inner)
        self.radio_button_container.pack(pady=5)
        save_btn=tk.Button(
            inner,text="Confirm Vote",
            command=lambda: submit_vote(self,self.controller)
        )
        save_btn.pack(pady=10)
        tk.Button(
            inner,
            text="See Current Voting Poll",
            command=lambda: controller.show_frame(controller.VOTE_MENU_CLASS)
        ).pack(pady=10)

        ###I had to use ai to figure out the lines below
        ###I tried my best to get the current candidates.txt file to update the widget content but no matter what i tried
        ### it didn't work. My original logic for the radio buttons is  on line 38-45 that was
        self.refresh
    def refresh(self):
        """
        Function deletes all radio btn widgets. It than checks to see if there are candidates in the dictionary.
        If there isn't any cnadidates dispay a label indicating the lack of candidates.
        If candidates do exist iterate through the dictionary and make a radio button in the format of Key: Value.get_party.
        make the radio button value the full name which is the key.
        param: current frame
        :return:
        """
        for widget in self.radio_button_container.winfo_children():
            widget.destroy()

        candidates = candidate_dictionary()
        if not candidates:
            tk.Label(self.radio_button_container, text="No candidates registered.").pack()
            self.selected_candid.set("")
            return

        for name, cand in candidates.items():
            tk.Radiobutton(
                self.radio_button_container,
                text=f"{name}: {cand.get_party()}",
                variable=self.selected_candid,
                value=name,
                anchor='w'
            ).pack(fill='x', pady=5)



