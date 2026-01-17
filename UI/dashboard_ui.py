import tkinter as tk
from tkinter import messagebox
from services import auth_service
from UI.task_management_ui import TaskManagementScreen

THEME_BG = "#FFE0E9"
THEME_ACCENT = "#B9375E"
THEME_TEXT = "#434343"
THEME_LIGHT = "#CEDDBB"

class DashboardScreen(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=30, pady=30)
        self.user = user
        self.build_ui()
    
    def build_ui(self):
        # Header Section
        header_frame = tk.Frame(self, bg=THEME_BG)
        header_frame.pack(fill="x", pady=(0, 30))
        
        tk.Label(
            header_frame,
            text=f"Welcome, {self.user.fname}! 👋",
            font=("Arial", 28, "bold"),
            bg=THEME_BG,
            fg=THEME_ACCENT,
        ).pack(anchor="w")
        
        tk.Label(
            header_frame,
            text="What would you like to do today?",
            font=("Arial", 11, "italic"),
            bg=THEME_BG,
            fg="#666",
        ).pack(anchor="w", pady=(5, 0))
        
        # Main Actions Frame
        actions_frame = tk.Frame(self, bg="#FFFFFF", relief="solid", bd=2, highlightbackground=THEME_ACCENT, highlightthickness=2)
        actions_frame.pack(fill="both", expand=True, pady=20)
        
        # Task Management Card
        task_card = tk.Frame(actions_frame, bg="#FFF5F7", relief="solid", bd=1)
        task_card.pack(fill="x", padx=15, pady=15)
        
        tk.Label(
            task_card,
            text="📋 Task Management",
            font=("Arial", 14, "bold"),
            bg="#FFF5F7",
            fg=THEME_ACCENT,
        ).pack(anchor="w", padx=15, pady=(10, 5))
        
        tk.Label(
            task_card,
            text="Create, edit, and manage your daily tasks",
            font=("Arial", 10, "italic"),
            bg="#FFF5F7",
            fg="#666",
        ).pack(anchor="w", padx=15, pady=(0, 10))
        
        tk.Button(
            task_card,
            text="Open Tasks →",
            command=self.go_to_tasks,
            bg=THEME_ACCENT,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            bd=0,
            padx=15,
            pady=8,
            cursor="hand2",
        ).pack(anchor="w", padx=15, pady=(0, 10))
        
        # Profile Card
        profile_card = tk.Frame(actions_frame, bg="#FFF5F7", relief="solid", bd=1)
        profile_card.pack(fill="x", padx=15, pady=15)
        
        tk.Label(
            profile_card,
            text="👤 Profile Settings",
            font=("Arial", 14, "bold"),
            bg="#FFF5F7",
            fg=THEME_ACCENT,
        ).pack(anchor="w", padx=15, pady=(10, 5))
        
        tk.Label(
            profile_card,
            text="Update your personal information",
            font=("Arial", 10, "italic"),
            bg="#FFF5F7",
            fg="#666",
        ).pack(anchor="w", padx=15, pady=(0, 10))
        
        tk.Button(
            profile_card,
            text="Edit Profile →",
            command=self.go_to_profile,
            bg=THEME_ACCENT,
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            bd=0,
            padx=15,
            pady=8,
            cursor="hand2",
        ).pack(anchor="w", padx=15, pady=(0, 10))
        
        # Bottom Section
        bottom_frame = tk.Frame(self, bg=THEME_BG)
        bottom_frame.pack(fill="x", pady=(20, 0))
        
        tk.Label(
            bottom_frame,
            text="Account Status: Active ✅",
            font=("Arial", 9),
            bg=THEME_BG,
            fg="#666",
        ).pack(anchor="w", pady=(0, 10))
        
        tk.Button(
            bottom_frame,
            text="🚪 Logout",
            command=self.logout,
            bg=THEME_LIGHT,
            fg=THEME_TEXT,
            font=("Arial", 11, "bold"),
            relief="flat",
            bd=0,
            padx=15,
            pady=10,
            cursor="hand2",
            width=40,
        ).pack(fill="x")
    
    def go_to_tasks(self):
        self.master.clear_screen()
        TaskManagementScreen(self.master, is_admin=False).pack(expand=True, fill="both")
    
    def go_to_profile(self):
        self.master.show_profile(self.user)
    
    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            auth_service.logout()
            self.master.show_login()