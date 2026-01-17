import tkinter as tk
from tkinter import messagebox, simpledialog
from services import auth_service, task_services
from utils import storage
from UI.task_management_ui import TaskManagementScreen

THEME_BG = "#FFE0E9"
THEME_ACCENT = "#B9375E"
THEME_TEXT = "#434343"
THEME_LIGHT = "#CEDDBB"

class AdminDashboardScreen(tk.Frame):
    def __init__(self, master, admin_user):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=20, pady=20)
        self.admin_user = admin_user
        self.build_ui()
    
    def build_ui(self):
        # Header
        tk.Label(
            self,
            text=f"🔐 Admin Panel - {self.admin_user.fname}",
            font=("Arial", 26, "bold"),
            bg=THEME_BG,
            fg=THEME_ACCENT,
        ).pack(pady=(0, 25), anchor="w")
        
        # Admin Options Frame
        options_frame = tk.Frame(self, bg="#FFFFFF", relief="solid", bd=1)
        options_frame.pack(fill="x", pady=(0, 15))
        
        tk.Button(
            options_frame,
            text="👥 View All Users",
            command=self.view_all_users,
            bg=THEME_ACCENT,
            fg="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=8,
            cursor="hand2",
        ).pack(side="left", padx=5, pady=5)
        
        tk.Button(
            options_frame,
            text="🔒 Deactivate User",
            command=self.deactivate_user,
            bg="#E67E22",
            fg="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=8,
            cursor="hand2",
        ).pack(side="left", padx=5, pady=5)
        
        tk.Button(
            options_frame,
            text="📋 View All Tasks",
            command=self.view_all_tasks,
            bg=THEME_ACCENT,
            fg="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=8,
            cursor="hand2",
        ).pack(side="left", padx=5, pady=5)
        
        tk.Button(
            options_frame,
            text="🗑️ Delete Task",
            command=self.delete_task_admin,
            bg="#E74C3C",
            fg="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=8,
            cursor="hand2",
        ).pack(side="left", padx=5, pady=5)
        
        # User Management Section
        tk.Label(
            self,
            text="User Management 👥",
            font=("Arial", 16, "bold"),
            bg=THEME_BG,
            fg=THEME_ACCENT,
        ).pack(anchor="w", pady=(15, 10))
        
        users_frame = tk.Frame(self, bg="#FFFFFF", relief="solid", bd=1)
        users_frame.pack(fill="x", pady=(0, 15))
        
        self.users_display = tk.Label(
            users_frame,
            text="Loading users...",
            font=("Arial", 9),
            bg="#FFFFFF",
            fg=THEME_TEXT,
            justify="left",
            wraplength=400,
        )
        self.users_display.pack(padx=15, pady=15, anchor="w")
        self.load_users()
        
        # Profile Section
        tk.Label(
            self,
            text="Account 👤",
            font=("Arial", 16, "bold"),
            bg=THEME_BG,
            fg=THEME_ACCENT,
        ).pack(anchor="w", pady=(15, 10))
        
        tk.Button(
            self,
            text="Update Profile",
            command=self.update_profile,
            bg=THEME_ACCENT,
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            bd=0,
            padx=15,
            pady=10,
            cursor="hand2",
            width=20,
        ).pack(side="left", padx=5, pady=5)
        
        tk.Button(
            self,
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
            width=20,
        ).pack(side="left", padx=5, pady=5)
    
    def load_users(self):
        users = storage.load_users()
        if users:
            user_text = "\n".join([f"👤 {u['fname']} {u['lname']} | {u['email']} | Status: {u['status']}" for u in users])
            self.users_display.config(text=user_text)
        else:
            self.users_display.config(text="No users found")
    
    def view_all_users(self):
        users = storage.load_users()
        if not users:
            messagebox.showinfo("Users", "No users found!")
        else:
            user_list = "\n".join([f"👤 {u['fname']} {u['lname']}\n   Email: {u['email']} | Status: {u['status']}\n" for u in users])
            messagebox.showinfo("All Users", user_list)
    
    def deactivate_user(self):
        user_id = simpledialog.askstring("Deactivate User", "Enter User ID:")
        if user_id:
            if auth_service.deactivate_user(user_id):
                messagebox.showinfo("Success", f"✅ User {user_id} deactivated!")
                self.load_users()
            else:
                messagebox.showerror("Error", "❌ Failed to deactivate user!")
    
    def view_all_tasks(self):
        tasks = task_services.view_tasks()
        if not tasks:
            messagebox.showinfo("Tasks", "No tasks found!")
        else:
            task_list = "\n".join([f"📌 {t['title']}\n   Owner: {t['owner_id']} | Status: {t['task_status']}\n   Priority: {t['priority']} | Due: {t['due_date']}\n" for t in tasks])
            messagebox.showinfo("All Tasks", task_list)
    
    def delete_task_admin(self):
        task_title = simpledialog.askstring("Delete Task", "Enter task title to delete:")
        if task_title:
            if task_services.delete_task(task_title):
                messagebox.showinfo("Success", f"✅ Task '{task_title}' deleted!")
            else:
                messagebox.showerror("Error", "❌ Failed to delete task!")
    
    
    def update_profile(self):
        self.master.show_profile(self.admin_user)

    def task_management(self):
        self.master.clear_screen()
        TaskManagementScreen(self.master, is_admin=True).pack(expand=True, fill="both")
    
    def logout(self):
        auth_service.logout()
        self.master.show_login()