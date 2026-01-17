import tkinter as tk
from tkinter import messagebox
from services import auth_service

THEME_BG = "#FFE0E9"
THEME_ACCENT = "#B9375E"
THEME_TEXT = "#434343"
THEME_LIGHT = "#CEDDBB"
THEME_BORDER = "#BE9A60"

class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=32, pady=40)
        self.build_ui()
    
    def build_ui(self):
        tk.Label(
            self,
            text="Welcome Back",
            font=("Arial", 28, "bold"),
            bg=THEME_BG,
            fg=THEME_ACCENT,
        ).pack(pady=(0, 8))
        
        tk.Label(
            self,
            text="Sign in to your account",
            font=("Arial", 11),
            bg=THEME_BG,
            fg="#6b6b6b",
        ).pack(pady=(0, 32))
        
        tk.Label(self, text="Email", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 6))
        self.email_entry = tk.Entry(self, width=40, bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 11), insertbackground=THEME_ACCENT, bd=1)
        self.email_entry.pack(anchor="w", pady=(0, 18), fill="x", ipady=8)
        
        tk.Label(self, text="Password", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 6))
        self.password_entry = tk.Entry(self, width=40, show="*", bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 11), insertbackground=THEME_ACCENT, bd=1)
        self.password_entry.pack(anchor="w", pady=(0, 28), fill="x", ipady=8)
        
        tk.Button(
            self,
            text="Sign In",
            command=self.login,
            bg=THEME_ACCENT,
            fg="white",
            activebackground="#8B2340",
            relief="flat",
            padx=12,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(pady=(0, 12), fill="x", ipady=6)
        
        tk.Button(
            self, 
            text="Create Account", 
            command=self.go_to_register,
            bg=THEME_LIGHT, 
            fg="#434343",
            activebackground="#B8D0A8",
            relief="flat",
            padx=12,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(fill="x", ipady=6)
    
    def login(self):
        email = self.email_entry.get().strip().lower()
        password = self.password_entry.get()
        
        if not email or not password:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        # Call auth_service.login_with_email()
        success = auth_service.login_with_email(email, password)
        
        if success:
            user = auth_service.get_current_user()
            if auth_service.is_admin():
                self.master.show_admin_dashboard(user)

            else:
                self.master.show_dashboard(user)
        else:
            messagebox.showerror("Error", "Invalid credentials or inactive account")

    
    def go_to_register(self):
        self.master.show_registration()