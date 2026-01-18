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
        
        # Create a scrollable frame for users
        users_container = tk.Frame(self, bg="#FFFFFF", relief="solid", bd=1)
        users_container.pack(fill="both", expand=True, pady=(0, 15))
        
        # Canvas for scrolling
        canvas = tk.Canvas(users_container, bg="#FFFFFF", highlightthickness=0, height=250)
        scrollbar = tk.Scrollbar(users_container, orient="vertical", command=canvas.yview)
        self.users_frame = tk.Frame(canvas, bg="#FFFFFF")
        
        self.users_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.users_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        
        self.load_users()
        
        # Profile Section
        tk.Label(
            self,
            text="Account 👤",
            font=("Arial", 16, "bold"),
            bg=THEME_BG,
            fg=THEME_ACCENT,
        ).pack(anchor="w", pady=(15, 10))
        
        buttons_frame = tk.Frame(self, bg=THEME_BG)
        buttons_frame.pack(fill="x")
        
        tk.Button(
            buttons_frame,
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
            buttons_frame,
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
        # Clear existing user cards
        for widget in self.users_frame.winfo_children():
            widget.destroy()
        
        users = storage.load_users()
        if not users:
            tk.Label(
                self.users_frame,
                text="No users found",
                font=("Arial", 10, "italic"),
                bg="#FFFFFF",
                fg="#999"
            ).pack(pady=20)
            return
        
        # Create user cards
        for user in users:
            self.create_user_card(user)
    
    def create_user_card(self, user):
        # Main card frame
        card = tk.Frame(self.users_frame, bg="#F8F9FA", relief="solid", bd=1)
        card.pack(fill="x", padx=10, pady=5)
        
        # Left side - User Info
        info_frame = tk.Frame(card, bg="#F8F9FA")
        info_frame.pack(side="left", fill="x", expand=True, padx=15, pady=10)
        
        # User ID - monospace font for clarity
        tk.Label(
            info_frame,
            text=f"ID: {user['id']}",
            font=("Courier New", 9, "bold"),
            bg="#F8F9FA",
            fg="#666"
        ).pack(anchor="w")
        
        # Name
        tk.Label(
            info_frame,
            text=f"👤 {user['fname']} {user['lname']}",
            font=("Arial", 11, "bold"),
            bg="#F8F9FA",
            fg=THEME_TEXT
        ).pack(anchor="w", pady=(3, 0))
        
        # Email
        tk.Label(
            info_frame,
            text=f"📧 {user['email']}",
            font=("Arial", 9),
            bg="#F8F9FA",
            fg="#666"
        ).pack(anchor="w")
        
        # Status badge
        status_color = "#27AE60" if user['status'] == 'active' else "#E74C3C"
        status_text = "✅ Active" if user['status'] == 'active' else "❌ Inactive"
        
        tk.Label(
            info_frame,
            text=status_text,
            font=("Arial", 9, "bold"),
            bg=status_color,
            fg="white",
            padx=8,
            pady=2
        ).pack(anchor="w", pady=(5, 0))
        
        # Right side - Action Buttons
        action_frame = tk.Frame(card, bg="#F8F9FA")
        action_frame.pack(side="right", padx=15, pady=10)
        
        # Activate/Deactivate button
        if user['status'] == 'active':
            tk.Button(
                action_frame,
                text="🔒 Deactivate",
                command=lambda: self.deactivate_user_direct(user['id']),
                bg="#E67E22",
                fg="white",
                font=("Arial", 9, "bold"),
                relief="flat",
                bd=0,
                padx=10,
                pady=5,
                cursor="hand2",
                width=12
            ).pack(pady=2)
        else:
            tk.Button(
                action_frame,
                text="✅ Activate",
                command=lambda: self.activate_user_direct(user['id']),
                bg="#27AE60",
                fg="white",
                font=("Arial", 9, "bold"),
                relief="flat",
                bd=0,
                padx=10,
                pady=5,
                cursor="hand2",
                width=12
            ).pack(pady=2)
        
        # Delete button
        tk.Button(
            action_frame,
            text="🗑️ Delete",
            command=lambda: self.delete_user(user['id']),
            bg="#E74C3C",
            fg="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=5,
            cursor="hand2",
            width=12
        ).pack(pady=2)
    
    def activate_user_direct(self, user_id):
        if auth_service.activate_user(user_id):
            messagebox.showinfo("Success", f"✅ User {user_id} activated!")
            self.load_users()
        else:
            messagebox.showerror("Error", "❌ Failed to activate user!")
    
    def deactivate_user_direct(self, user_id):
        if auth_service.deactivate_user(user_id):
            messagebox.showinfo("Success", f"✅ User {user_id} deactivated!")
            self.load_users()
        else:
            messagebox.showerror("Error", "❌ Failed to deactivate user!")
    
    def delete_user(self, user_id):
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete user {user_id}?\n\nThis action cannot be undone!"):
            users = storage.load_users()
            users = [u for u in users if u['id'] != user_id]
            storage.save_users(users)
            messagebox.showinfo("Success", f"✅ User {user_id} deleted!")
            self.load_users()
    
    def view_all_users(self):
        users = storage.load_users()
        if not users:
            messagebox.showinfo("Users", "No users found!")
        else:
            user_list = "\n".join([f"👤 {u['fname']} {u['lname']}\n   ID: {u['id']}\n   Email: {u['email']}\n   Status: {u['status']}\n" for u in users])
            messagebox.showinfo("All Users", user_list)
    
    def activate_user(self):
        user_id = simpledialog.askstring("Activate User", "Enter User ID:")
        if user_id:
            if auth_service.activate_user(user_id):
                messagebox.showinfo("Success", f"✅ User {user_id} activated!")
                self.load_users()
            else:
                messagebox.showerror("Error", "❌ Failed to activate user!")
    
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