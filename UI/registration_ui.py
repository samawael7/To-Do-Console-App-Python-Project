import tkinter as tk
from tkinter import messagebox
from services import auth_service

THEME_BG = "#FFE0E9"
THEME_ACCENT = "#B9375E"
THEME_TEXT = "#434343"
THEME_LIGHT = "#CEDDBB"
THEME_BORDER = "#BE9A60"

class RegistrationScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=0, pady=0)
        
        # Create a canvas with scrollbar
        self.canvas = tk.Canvas(self, bg=THEME_BG, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=THEME_BG)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Center the window horizontally
        window_id = self.canvas.create_window((275, 0), window=self.scrollable_frame, anchor="n", width=550)
        
        def resize_window(event):
            self.canvas.itemconfig(window_id, width=event.width)
        
        self.canvas.bind("<Configure>", resize_window)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        self.build_ui()
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def build_ui(self):
        tk.Label(
            self.scrollable_frame,
            text="Create Account",
            font=("Arial", 28, "bold"),
            bg=THEME_BG,
            fg=THEME_ACCENT,
        ).pack(pady=(24, 8), padx=32)
        
        tk.Label(
            self.scrollable_frame,
            text="Join us today",
            font=("Arial", 11),
            bg=THEME_BG,
            fg="#6b6b6b",
        ).pack(pady=(0, 20), padx=32)
        
        tk.Label(self.scrollable_frame, text="ID (14 digits)", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(8, 4), padx=32)
        self.id_entry = tk.Entry(self.scrollable_frame, width=40, bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.id_entry.pack(anchor="w", pady=(0, 10), fill="x", ipady=8, padx=32)
        
        tk.Label(self.scrollable_frame, text="First Name", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(8, 4), padx=32)
        self.fname_entry = tk.Entry(self.scrollable_frame, width=40, bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.fname_entry.pack(anchor="w", pady=(0, 10), fill="x", ipady=8, padx=32)
        
        tk.Label(self.scrollable_frame, text="Last Name", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(8, 4), padx=32)
        self.lname_entry = tk.Entry(self.scrollable_frame, width=40, bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.lname_entry.pack(anchor="w", pady=(0, 10), fill="x", ipady=8, padx=32)
        
        tk.Label(self.scrollable_frame, text="Email", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(8, 4), padx=32)
        self.email_entry = tk.Entry(self.scrollable_frame, width=40, bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.email_entry.pack(anchor="w", pady=(0, 10), fill="x", ipady=8, padx=32)
        
        tk.Label(self.scrollable_frame, text="Mobile", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(8, 4), padx=32)
        self.mobile_entry = tk.Entry(self.scrollable_frame, width=40, bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.mobile_entry.pack(anchor="w", pady=(0, 10), fill="x", ipady=8, padx=32)
        
        tk.Label(self.scrollable_frame, text="Password", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(8, 4), padx=32)
        self.password_entry = tk.Entry(self.scrollable_frame, width=40, bg="white", fg=THEME_TEXT, relief="solid", show="*", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.password_entry.pack(anchor="w", pady=(0, 10), fill="x", ipady=8, padx=32)
        
        tk.Label(self.scrollable_frame, text="Confirm Password", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(8, 4), padx=32)
        self.confirm_entry = tk.Entry(self.scrollable_frame, width=40, bg="white", fg=THEME_TEXT, relief="solid", show="*", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.confirm_entry.pack(anchor="w", pady=(0, 18), fill="x", ipady=7, padx=32)
        
        tk.Button(
            self.scrollable_frame,
            text="Create Account",
            command=self.register,
            bg=THEME_ACCENT,
            fg="white",
            activebackground="#8B2340",
            relief="flat",
            padx=12,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(pady=(8, 10), fill="x", ipady=6, padx=32)
        
        tk.Button(
            self.scrollable_frame,
            text="Back to Login",
            command=self.go_to_login,
            bg=THEME_LIGHT,
            fg="#333333",
            activebackground="#B8D0A8",
            relief="flat",
            padx=12,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(fill="x", ipady=6, padx=32, pady=(0, 24))
    
    def register(self):
        user_id = self.id_entry.get()
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        email = self.email_entry.get()
        mobile = self.mobile_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()
        
        if not all([user_id, fname, lname, email, mobile, password, confirm]):
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        # Call auth_service.register_user()
        success = auth_service.register_user(user_id, fname, lname, email, mobile, password, confirm)
        
        if success:
            messagebox.showinfo("Success", "Registration successful!")
            self.go_to_login()
        else:
            messagebox.showerror("Error", "Registration failed! Check your inputs.")
    
    def go_to_login(self):
        self.master.show_login()