import tkinter as tk
from tkinter import messagebox
from services import auth_service

THEME_BG = "#FFE0E9"
THEME_ACCENT = "#B9375E"
THEME_TEXT = "#434343"
THEME_LIGHT = "#CEDDBB"
THEME_BORDER = "#BE9A60"

class ProfileScreen(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=32, pady=32)
        self.user = user
        self.build_ui()
    
    def build_ui(self):
        tk.Label(
            self,
            text="Edit Profile",
            font=("Arial", 26, "bold"),
            bg=THEME_BG,
            fg=THEME_ACCENT,
        ).pack(pady=(0, 8))
        
        tk.Label(
            self,
            text="Update your personal information",
            font=("Arial", 10),
            bg=THEME_BG,
            fg="#6b6b6b",
        ).pack(pady=(0, 28))
        
        tk.Label(self, text="First Name", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(0, 6))
        self.fname_entry = tk.Entry(self, width=40, bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.fname_entry.insert(0, self.user.fname)
        self.fname_entry.pack(anchor="w", pady=(0, 14), fill="x", ipady=8)
        
        tk.Label(self, text="Last Name", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(0, 6))
        self.lname_entry = tk.Entry(self, width=40, bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.lname_entry.insert(0, self.user.lname)
        self.lname_entry.pack(anchor="w", pady=(0, 14), fill="x", ipady=8)
        
        tk.Label(self, text="Mobile", bg=THEME_BG, fg=THEME_TEXT, font=("Arial", 9, "bold")).pack(anchor="w", pady=(0, 6))
        self.mobile_entry = tk.Entry(self, width=40, bg="white", fg=THEME_TEXT, relief="solid", font=("Arial", 10), insertbackground=THEME_ACCENT, bd=1)
        self.mobile_entry.insert(0, self.user.mobile)
        self.mobile_entry.pack(anchor="w", pady=(0, 24), fill="x", ipady=8)
        
        tk.Button(
            self,
            text="💾 Save Changes",
            command=self.save_profile,
            bg=THEME_ACCENT,
            fg="white",
            activebackground="#8B2340",
            relief="flat",
            padx=12,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(pady=(0, 10), fill="x", ipady=6)
        
        tk.Button(
            self,
            text="← Back",
            command=self.go_back,
            bg=THEME_LIGHT,
            fg="#333333",
            activebackground="#B8D0A8",
            relief="flat",
            padx=12,
            pady=10,
            font=("Arial", 11, "bold"),
            cursor="hand2",
            bd=0,
        ).pack(fill="x", ipady=6)
    
    def save_profile(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        mobile = self.mobile_entry.get()
        
        if not all([fname, lname, mobile]):
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        success = auth_service.update_profile(fname=fname, lname=lname, mobile=mobile)

        if success:
            messagebox.showinfo("Success", "Profile updated successfully!!")
            self.user.fname = fname
            self.user.lname = lname
            self.user.mobile = mobile
            self.go_back()
        else:
            messagebox.showerror("Error", "failed to update profile")

    
    def go_back(self):
        self.master.show_dashboard(self.user)