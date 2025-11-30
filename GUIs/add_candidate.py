import tkinter as tk
class Add_Candidate(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        inner = tk.Frame(self)
        inner.pack(expand=True)
        tk.Label(inner, text="Add Candidate",font=("Times New Roman", 24)).pack(pady=10)
        first_name_label = tk.Label(inner, text="First Name")
        first_name_input= tk.Entry(inner)
        first_name_label.pack(pady=10)
        first_name_input.pack(pady=10)

        last_name_label = tk.Label(inner, text="Last Name")
        last_name_input= tk.Entry(inner)
        last_name_label.pack(pady=10)
        last_name_input.pack(pady=10)

        party_checkbox_val=tk.StringVar(value="N/A")
        party_affiliate_label= tk.Label(inner, text="Party Affiliation")
        party_affiliate_label.pack(pady=10)
        demcrat_checkbox= tk.Checkbutton(inner, text="Democratic Party",
                                         variable=party_checkbox_val,onvalue="Democratic Party"
                                         ,offvalue="N/A")
        demcrat_checkbox.pack(pady=10)

        republic_checkbox= tk.Checkbutton(inner, text="Republican Party",
                                         variable=party_checkbox_val,onvalue="Republican Party"
                                         ,offvalue="N/A")
        republic_checkbox.pack(pady=10)
        independent_checkbox= tk.Checkbutton(inner, text="Independent Party",
                                         variable=party_checkbox_val,onvalue="Independent Party"
                                         ,offvalue="N/A")
        independent_checkbox.pack(pady=10)

        save_button= tk.Button(inner, text="Save Candidate",)#adjust functionality later
        save_button.pack(pady=10)

        return_button = tk.Button(
            inner,
            text="See Current Voting Poll",
            command=lambda: self.controller.show_frame(controller.VOTE_MENU_CLASS)
        )
        return_button.pack(pady=10)