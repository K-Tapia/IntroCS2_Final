import tkinter as tk

from GUIs.vote_menu import Vote_Menu
from GUIs.add_candidate import Add_Candidate
from GUIs.view_poll import View_Poll
from GUIs.vote_candidate import Vote_Candidate
from GUIs.login import Login
#Video link that helped me understand how to make frames using classes: https://www.youtube.com/watch?v=eaxPK9VIkFM
class Main(tk.Tk):
    def __init__(self)->None:
        """
        Constructor for our main window,
        will inherit child frames that will be interchangeable
        :Return:None
        """
        super().__init__()
        self.title("Voting GUI Final")
        self.geometry("800x600")
        self.resizable(False, False)
        self.VOTE_MENU_CLASS=Vote_Menu
        self.VOTE_CANDIDATE_CLASS = Vote_Candidate
        self.ADD_CANDIDATE_CLASS = Add_Candidate
        self.VIEW_POLL_CLASS= View_Poll
        self.LOGIN_CLASS=Login
        self.current_user_id = None

        container = tk.Frame(self)
        container.pack( expand=True)
        self.frames={}
        #Ai used lines 30-36
        for F in (Login,Vote_Menu,Add_Candidate,View_Poll,Vote_Candidate):
            #for loop that saves frames into a dictionary
            #Frames are stacked in same location, switches between whichever frame is raised.
            frame=F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login)

    def show_frame(self, Page)->None:
        """
        This will raise whichever frame
        to show on the main windows
        :Return: None
        """
        frame=self.frames[Page]
        # ai usage line 47 and 48
        if hasattr(frame, 'refresh'):
            frame.refresh()
        frame.tkraise()

if __name__ == "__main__":
    app = Main()
    app.mainloop()
