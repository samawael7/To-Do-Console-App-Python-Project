import tkinter as tk
from services import auth_service

THEME_BG = "#FFE0E9"
THEME_ACCENT = "#B9375E"
THEME_TEXT = "#434343"
THEME_LIGHT = "#CEDDBB"
THEME_BORDER = "#BE9A60"

class DashboardScreen(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=32, pady=32)
        self.user = user
        self.build_ui()
    
    def build_ui(self):
        tk.Label(
            self,
            text=f"Welcome back, {self.user.fname}!",
            font=("Arial", 26, "bold"),
            bg=THEME_BG,
            fg=THEME_ACCENT,
        ).pack(pady=(0, 8), anchor="w")
        
        tk.Label(
            self,
            text="Manage your tasks efficiently",
            font=("Arial", 10),
            bg=THEME_BG,
            fg="#6b6b6b",
        ).pack(pady=(0, 28), anchor="w")
        
        tk.Button(
            self,
            text="📋 View Tasks",
            command=self.view_tasks,
            bg=THEME_ACCENT,
            fg="white",
            activebackground="#8B2340",
            relief="flat",
            padx=12,
            pady=11,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(pady=8, fill="x", ipady=6)
        
        tk.Button(
            self,
            text="➕ Create Task",
            command=self.create_task,
            bg=THEME_ACCENT,
            fg="white",
            activebackground="#8B2340",
            relief="flat",
            padx=12,
            pady=11,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(pady=8, fill="x", ipady=6)
        
        tk.Button(
            self,
            text="👤 Update Profile",
            command=self.go_to_profile,
            bg=THEME_ACCENT,
            fg="white",
            activebackground="#8B2340",
            relief="flat",
            padx=12,
            pady=11,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(pady=8, fill="x", ipady=6)
        
        tk.Button(
            self,
            text="🚪 Logout",
            command=self.logout,
            bg=THEME_LIGHT,
            fg=THEME_TEXT,
            activebackground="#B8D0A8",
            relief="flat",
            padx=12,
            pady=11,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(pady=8, fill="x", ipady=6)
    
    def view_tasks(self):
        print("📋 View Tasks")
    
    def create_task(self):
        print("➕ Create Task")
    
    def go_to_profile(self):
        self.master.show_profile(self.user)
    
    def logout(self):
        auth_service.logout()
        self.master.show_login()