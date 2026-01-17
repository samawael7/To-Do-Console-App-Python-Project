import tkinter as tk
from UI.login_ui import LoginScreen
from UI.registration_ui import RegistrationScreen
from UI.dashboard_ui import DashboardScreen
from UI.profile_ui import ProfileScreen
from services import auth_service
from models.user import User
from models.task import Task

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Management App")
        self.geometry("550x750")
        self.configure(bg="#FFE0E9")
        self.resizable(False, False)
        self.current_user = None
        self.show_login()
    
    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def show_login(self):
        self.clear_screen()
        LoginScreen(self).pack(expand=True, fill="both")
    
    def show_registration(self):
        self.clear_screen()
        RegistrationScreen(self).pack(expand=True, fill="both")
    
    def show_dashboard(self, user):
        self.current_user = user
        self.clear_screen()
        DashboardScreen(self, user).pack(expand=True, fill="both")
    
    def show_profile(self, user):
        self.clear_screen()
        ProfileScreen(self, user).pack(expand=True, fill="both")

    def show_admin_dashboard(self, user):
        self.current_user = user
        self.clear_screen()
        DashboardScreen(self, user, is_admin=True).pack(expand=True, fill="both")


if __name__ == "__main__":
    app = App()
    app.mainloop()