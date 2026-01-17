import tkinter as tk
from tkinter import messagebox, simpledialog
from services import task_services

THEME_BG = "#FFE0E9"
THEME_ACCENT = "#B9375E"
THEME_TEXT = "#434343"
THEME_LIGHT = "#CEDDBB"

class TaskManagementScreen(tk.Frame):
    def __init__(self, master, is_admin=False):
        super().__init__(master, bg=THEME_BG)
        self.configure(padx=20, pady=20)
        self.is_admin = is_admin
        self.build_ui()
    
    def build_ui(self):
        # Header
        header_frame = tk.Frame(self, bg=THEME_BG)
        header_frame.pack(fill="x", pady=(0, 20))
        
        if self.is_admin:
            tk.Label(
                header_frame,
                text="All Tasks (Admin View) 📋",
                font=("Arial", 26, "bold"),
                bg=THEME_BG,
                fg=THEME_ACCENT,
            ).pack(anchor="w", side="left")
        else:
            tk.Label(
                header_frame,
                text="My Tasks 📋",
                font=("Arial", 26, "bold"),
                bg=THEME_BG,
                fg=THEME_ACCENT,
            ).pack(anchor="w", side="left")
        
        # Options Frame
        options_frame = tk.Frame(self, bg="#FFFFFF", relief="solid", bd=1)
        options_frame.pack(fill="x", pady=(0, 15))
        
        # Regular User Options (Create, Search)
        if not self.is_admin:
            tk.Button(
                options_frame,
                text="➕ New Task",
                command=self.create_new_task,
                bg=THEME_ACCENT,
                fg="white",
                font=("Arial", 9, "bold"),
                relief="flat",
                bd=0,
                padx=10,
                pady=8,
                cursor="hand2",
            ).pack(side="left", padx=5, pady=5)
        
        # Both can search
        tk.Button(
            options_frame,
            text="🔍 Search",
            command=self.search_task,
            bg=THEME_ACCENT,
            fg="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=10,
            pady=8,
            cursor="hand2",
        ).pack(side="left", padx=5, pady=5)
            
        # Admin: Sort & Filter ALL tasks
        if self.is_admin:
            tk.Button(
                options_frame,
                text="📊 Sort",
                command=self.sort_task,
                bg="#F0A500",
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
                text="⚙️ Filter",
                command=self.filter_task,
                bg="#F0A500",
                fg="white",
                font=("Arial", 9, "bold"),
                relief="flat",
                bd=0,
                padx=10,
                pady=8,
                cursor="hand2",
            ).pack(side="left", padx=5, pady=5)
        else:
            # Regular User: Sort & Filter OWN tasks only
            tk.Button(
                options_frame,
                text="📊 Sort",
                command=self.sort_task,
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
                text="⚙️ Filter",
                command=self.filter_task,
                bg=THEME_ACCENT,
                fg="white",
                font=("Arial", 9, "bold"),
                relief="flat",
                bd=0,
                padx=10,
                pady=8,
                cursor="hand2",
            ).pack(side="left", padx=5, pady=5)
        
        # Tasks Display
        self.tasks_frame = tk.Frame(self, bg=THEME_BG)
        self.tasks_frame.pack(fill="both", expand=True, pady=10)
        
        self.refresh_tasks()
        
        # Back Button
        tk.Button(
            self,
            text="← Back to Dashboard",
            command=self.go_back,
            bg=THEME_LIGHT,
            fg=THEME_TEXT,
            font=("Arial", 10, "bold"),
            relief="flat",
            bd=0,
            padx=15,
            pady=10,
            cursor="hand2",
        ).pack(fill="x", pady=(10, 0))
        
    def refresh_tasks(self):
            for widget in self.tasks_frame.winfo_children():
                widget.destroy()
            
            tasks = task_services.view_tasks()
            
            if not tasks:
                tk.Label(
                    self.tasks_frame,
                    text="📭 No tasks yet! Create one to get started.",
                    font=("Arial", 12, "italic"),
                    bg=THEME_BG,
                    fg="#999"
                ).pack(pady=30)
                return
            
            for task in tasks:
                self.create_task_card(task)
    
    def create_task_card(self, task):
        card = tk.Frame(self.tasks_frame, bg="#FFFFFF", relief="solid", bd=1)
        card.pack(fill="x", pady=8)
        
        # Task Info
        info_frame = tk.Frame(card, bg="#FFFFFF")
        info_frame.pack(fill="x", padx=15, pady=12, side="left", expand=True)
        
        tk.Label(
            info_frame,
            text=f"📌 {task['title']}",
            font=("Arial", 12, "bold"),
            bg="#FFFFFF",
            fg=THEME_TEXT,
        ).pack(anchor="w")
        
        # Show owner if admin
        if self.is_admin:
            details = f"Owner: {task['owner_id']} | Status: {task['task_status']} | Priority: {task['priority']} | Due: {task['due_date']}"
        else:
            details = f"Status: {task['task_status']} | Priority: {task['priority']} | Due: {task['due_date']}"
        
        tk.Label(
            info_frame,
            text=details,
            font=("Arial", 9),
            bg="#FFFFFF",
            fg="#666",
        ).pack(anchor="w", pady=(5, 0))
        
        if task.get('description'):
            tk.Label(
                info_frame,
                text=f"Description: {task['description']}",
                font=("Arial", 9, "italic"),
                bg="#FFFFFF",
                fg="#888",
                wraplength=300,
            ).pack(anchor="w", pady=(3, 0))
        
        # Action Buttons
        action_frame = tk.Frame(card, bg="#FFFFFF")
        action_frame.pack(side="right", padx=15, pady=12)
        
        # Regular User: Edit/Delete own tasks only
        if not self.is_admin:
            from services import auth_service
            current_user = auth_service.get_current_user()
            
            if task['owner_id'] == current_user.id:
                tk.Button(
                    action_frame,
                    text="✏️ Edit",
                    command=lambda: self.edit_task(task['title']),
                    bg="#F0A500",
                    fg="white",
                    font=("Arial", 9, "bold"),
                    relief="flat",
                    bd=0,
                    padx=8,
                    pady=5,
                    cursor="hand2",
                ).pack(side="left", padx=3)
                
                tk.Button(
                    action_frame,
                    text="🗑️ Delete",
                    command=lambda: self.delete_task(task['title']),
                    bg="#E74C3C",
                    fg="white",
                    font=("Arial", 9, "bold"),
                    relief="flat",
                    bd=0,
                    padx=8,
                    pady=5,
                    cursor="hand2",
                ).pack(side="left", padx=3)
        else:
            # Admin: Delete any task
            tk.Button(
                action_frame,
                text="🗑️ Delete",
                command=lambda: self.delete_task(task['title']),
                bg="#E74C3C",
                fg="white",
                font=("Arial", 9, "bold"),
                relief="flat",
                bd=0,
                padx=8,
                pady=5,
                cursor="hand2",
            ).pack(side="left", padx=3)
    
    def create_new_task(self):
    # Pop-up بسيط للـ create task
        title = simpledialog.askstring("Create Task", "Task Title:")
        if not title:
            return
        
        description = simpledialog.askstring("Create Task", "Description (optional):")
        if description is None:
            description = ""
        
        priority = simpledialog.askstring("Create Task", "Priority (Low/Medium/High):")
        if not priority:
            return
        
        status = simpledialog.askstring("Create Task", "Status (To-Do/In Progress/Completed):")
        if not status:
            return
        
        due_date = simpledialog.askstring("Create Task", "Due Date (YYYY-MM-DD):")
        if not due_date:
            return
        
        if task_services.create_task(title, description, priority, status, due_date):
            messagebox.showinfo("Success", "✅ Task created successfully!")
            self.refresh_tasks()
        else:
            messagebox.showerror("Error", "❌ Failed to create task!")
    
    def edit_task(self, task_title):
        new_title = simpledialog.askstring("Edit", "New title (leave empty to skip):")
        if new_title is None:
            return
        
        new_desc = simpledialog.askstring("Edit", "New description (leave empty to skip):")
        if new_desc is None:
            return
        
        new_priority = simpledialog.askstring("Edit", "New priority - Low/Medium/High (leave empty to skip):")
        if new_priority is None:
            return
        
        new_status = simpledialog.askstring("Edit", "New status - To-Do/In Progress/Completed (leave empty to skip):")
        if new_status is None:
            return
        
        new_date = simpledialog.askstring("Edit", "New due date YYYY-MM-DD (leave empty to skip):")
        if new_date is None:
            return
        
        if task_services.edit_task(task_title, new_title or None, new_desc or None, new_priority or None, new_date or None, new_status or None):
            messagebox.showinfo("Success", "✅ Task updated!")
            self.refresh_tasks()
        else:
            messagebox.showerror("Error", "❌ Failed to update task!")
    
    def delete_task(self, task_title):
        if messagebox.askyesno("Confirm", f"Delete '{task_title}'?"):
            if task_services.delete_task(task_title):
                messagebox.showinfo("Success", "✅ Task deleted!")
                self.refresh_tasks()
            else:
                messagebox.showerror("Error", "❌ Failed to delete task!")
    
    def search_task(self):
        keyword = simpledialog.askstring("Search", "Search tasks by title:")
        if keyword:
            results = task_services.search_tasks(keyword)
            if results:
                self.tasks_frame.destroy()
                self.tasks_frame = tk.Frame(self, bg=THEME_BG)
                self.tasks_frame.pack(fill="both", expand=True, pady=10)
                for task in results:
                    self.create_task_card(task)
            else:
                messagebox.showinfo("Search", "❌ No tasks found!")
    
    def sort_task(self):
        sort_by = simpledialog.askstring("Sort", "Sort by (due_date/priority/status):")
        if sort_by:
            sorted_tasks = task_services.sort_tasks(sort_by)
            self.tasks_frame.destroy()
            self.tasks_frame = tk.Frame(self, bg=THEME_BG)
            self.tasks_frame.pack(fill="both", expand=True, pady=10)
            for task in sorted_tasks:
                self.create_task_card(task)
    
    def filter_task(self):
        filter_by = simpledialog.askstring("Filter", "Filter by (priority/status/due_date):")
        if filter_by:
            filter_value = simpledialog.askstring("Filter", f"Enter {filter_by} value:")
            if filter_value:
                filtered = task_services.filter_tasks(filter_by, filter_value)
                self.tasks_frame.destroy()
                self.tasks_frame = tk.Frame(self, bg=THEME_BG)
                self.tasks_frame.pack(fill="both", expand=True, pady=10)
                for task in filtered:
                    self.create_task_card(task)
    
    def go_back(self):
        self.master.show_dashboard(self.master.current_user)