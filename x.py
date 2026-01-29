import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime

class LostAndFoundDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Lost & Found System")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f8fafc")
        
        # Sample data
        self.lost_items = [
            {"id": 1, "title": "iPhone 14 Pro", "category": "Electronics", "location": "Library - 2nd Floor", 
             "date": "2026-01-10", "description": "Black iPhone with blue case", "contact": "john@email.com", "status": "Lost"},
            {"id": 2, "title": "Blue Backpack", "category": "Bags", "location": "Cafeteria", 
             "date": "2026-01-09", "description": "Nike backpack with laptop inside", "contact": "sarah@email.com", "status": "Lost"},
            {"id": 3, "title": "Silver Watch", "category": "Accessories", "location": "Gym", 
             "date": "2026-01-08", "description": "Citizen eco-drive watch", "contact": "mike@email.com", "status": "Lost"}
        ]
        
        self.found_items = [
            {"id": 1, "title": "Wallet", "category": "Accessories", "location": "Parking Lot B", 
             "date": "2026-01-10", "description": "Brown leather wallet with ID cards", "contact": "admin@email.com", "status": "Found"},
            {"id": 2, "title": "Keys", "category": "Keys", "location": "Main Entrance", 
             "date": "2026-01-09", "description": "Car keys with Toyota keychain", "contact": "security@email.com", "status": "Found"},
            {"id": 3, "title": "Laptop Charger", "category": "Electronics", "location": "Room 301", 
             "date": "2026-01-07", "description": "Dell laptop charger 65W", "contact": "staff@email.com", "status": "Found"}
        ]
        
        self.current_view = "lost"
        
        # Main container
        main_container = tk.Frame(root, bg="#f8fafc")
        main_container.pack(fill="both", expand=True)
        
        # Sidebar
        self.create_sidebar(main_container)
        
        # Main content area
        self.content_frame = tk.Frame(main_container, bg="#f8fafc")
        self.content_frame.pack(side="left", fill="both", expand=True)
        
        # Header
        self.create_header()
        
        # Show initial view
        self.show_lost_items()
    
    def create_sidebar(self, parent):
        sidebar = tk.Frame(parent, bg="#1e293b", width=250)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)
        
        # Logo/Title
        logo_frame = tk.Frame(sidebar, bg="#1e293b")
        logo_frame.pack(pady=30, padx=20)
        
        tk.Label(logo_frame, text="🔍", font=("Arial", 32), bg="#1e293b").pack()
        tk.Label(logo_frame, text="Lost & Found", font=("Helvetica", 16, "bold"), 
                bg="#1e293b", fg="white").pack()
        
        # Navigation buttons
        nav_frame = tk.Frame(sidebar, bg="#1e293b")
        nav_frame.pack(fill="x", padx=15, pady=20)
        
        self.lost_btn = self.create_nav_button(nav_frame, "📋 Lost Items", 
                                                lambda: self.switch_view("lost"), active=True)
        self.lost_btn.pack(fill="x", pady=5)
        
        self.found_btn = self.create_nav_button(nav_frame, "✅ Found Items", 
                                                 lambda: self.switch_view("found"))
        self.found_btn.pack(fill="x", pady=5)
        
        self.post_btn = self.create_nav_button(nav_frame, "➕ Post Item", 
                                                lambda: self.switch_view("post"))
        self.post_btn.pack(fill="x", pady=5)
        
        self.matches_btn = self.create_nav_button(nav_frame, "🎯 Matches", 
                                                   lambda: self.switch_view("matches"))
        self.matches_btn.pack(fill="x", pady=5)
        
        # Stats section
        stats_frame = tk.Frame(sidebar, bg="#0f172a", highlightbackground="#334155", 
                              highlightthickness=1)
        stats_frame.pack(fill="x", padx=15, pady=20)
        
        tk.Label(stats_frame, text="Statistics", font=("Helvetica", 12, "bold"), 
                bg="#0f172a", fg="white").pack(pady=15)
        
        self.create_stat_item(stats_frame, "Total Lost", len(self.lost_items), "#ef4444")
        self.create_stat_item(stats_frame, "Total Found", len(self.found_items), "#10b981")
        self.create_stat_item(stats_frame, "Matched", "0", "#3b82f6")
        
        # User info at bottom
        user_frame = tk.Frame(sidebar, bg="#0f172a")
        user_frame.pack(side="bottom", fill="x", pady=20, padx=15)
        
        tk.Label(user_frame, text="👤", font=("Arial", 24), bg="#0f172a").pack()
        tk.Label(user_frame, text="John Doe", font=("Helvetica", 11, "bold"), 
                bg="#0f172a", fg="white").pack()
        tk.Label(user_frame, text="john@email.com", font=("Helvetica", 9), 
                bg="#0f172a", fg="#94a3b8").pack()
    
    def create_nav_button(self, parent, text, command, active=False):
        bg_color = "#3b82f6" if active else "#334155"
        
        btn = tk.Button(parent, text=text, font=("Helvetica", 11), bg=bg_color, 
                       fg="white", border=0, cursor="hand2", anchor="w", padx=15,
                       activebackground="#2563eb", activeforeground="white", command=command)
        btn.config(height=2)
        
        def on_enter(e):
            if btn.cget("bg") != "#3b82f6":
                btn.config(bg="#475569")
        
        def on_leave(e):
            if btn.cget("bg") != "#3b82f6":
                btn.config(bg="#334155")
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn
    
    def create_stat_item(self, parent, label, value, color):
        frame = tk.Frame(parent, bg="#0f172a")
        frame.pack(fill="x", padx=15, pady=10)
        
        tk.Label(frame, text=str(value), font=("Helvetica", 20, "bold"), 
                bg="#0f172a", fg=color).pack()
        tk.Label(frame, text=label, font=("Helvetica", 9), 
                bg="#0f172a", fg="#94a3b8").pack()
    
    def create_header(self):
        header = tk.Frame(self.content_frame, bg="white", highlightbackground="#e2e8f0", 
                         highlightthickness=1)
        header.pack(fill="x", padx=20, pady=20)
        
        header_content = tk.Frame(header, bg="white")
        header_content.pack(fill="x", padx=20, pady=15)
        
        self.header_title = tk.Label(header_content, text="Lost Items", 
                                     font=("Helvetica", 24, "bold"), bg="white", fg="#0f172a")
        self.header_title.pack(side="left")
        
        # Search bar
        search_frame = tk.Frame(header_content, bg="#f1f5f9", highlightbackground="#cbd5e1", 
                               highlightthickness=1)
        search_frame.pack(side="right")
        
        tk.Label(search_frame, text="🔍", bg="#f1f5f9", font=("Arial", 12)).pack(side="left", padx=(10, 5))
        search_entry = tk.Entry(search_frame, font=("Helvetica", 10), bg="#f1f5f9", 
                               border=0, width=25)
        search_entry.insert(0, "Search items...")
        search_entry.pack(side="left", padx=(0, 10), pady=8)
    
    def switch_view(self, view):
        self.current_view = view
        
        # Update button states
        for btn in [self.lost_btn, self.found_btn, self.post_btn, self.matches_btn]:
            btn.config(bg="#334155")
        
        if view == "lost":
            self.lost_btn.config(bg="#3b82f6")
            self.show_lost_items()
        elif view == "found":
            self.found_btn.config(bg="#3b82f6")
            self.show_found_items()
        elif view == "post":
            self.post_btn.config(bg="#3b82f6")
            self.show_post_form()
        elif view == "matches":
            self.matches_btn.config(bg="#3b82f6")
            self.show_matches()
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children()[1:]:
            widget.destroy()
    
    def show_lost_items(self):
        self.header_title.config(text="Lost Items")
        self.clear_content()
        self.display_items(self.lost_items, "#ef4444")
    
    def show_found_items(self):
        self.header_title.config(text="Found Items")
        self.clear_content()
        self.display_items(self.found_items, "#10b981")
    
    def display_items(self, items, color):
        container = tk.Frame(self.content_frame, bg="#f8fafc")
        container.pack(fill="both", expand=True, padx=20)
        
        # Create scrollable frame
        canvas = tk.Canvas(container, bg="#f8fafc", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f8fafc")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Display items in grid
        for idx, item in enumerate(items):
            self.create_item_card(scrollable_frame, item, color, idx)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def create_item_card(self, parent, item, color, idx):
        row = idx // 2
        col = idx % 2
        
        card = tk.Frame(parent, bg="white", highlightbackground="#e2e8f0", 
                       highlightthickness=1)
        card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        
        # Status badge
        badge = tk.Label(card, text=item["status"], font=("Helvetica", 8, "bold"), 
                        bg=color, fg="white", padx=8, pady=3)
        badge.pack(anchor="ne", padx=15, pady=15)
        
        # Content
        content = tk.Frame(card, bg="white")
        content.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        tk.Label(content, text=item["title"], font=("Helvetica", 16, "bold"), 
                bg="white", fg="#0f172a").pack(anchor="w")
        
        tk.Label(content, text=f"📁 {item['category']}", font=("Helvetica", 9), 
                bg="white", fg="#64748b").pack(anchor="w", pady=2)
        
        tk.Label(content, text=f"📍 {item['location']}", font=("Helvetica", 9), 
                bg="white", fg="#64748b").pack(anchor="w", pady=2)
        
        tk.Label(content, text=f"📅 {item['date']}", font=("Helvetica", 9), 
                bg="white", fg="#64748b").pack(anchor="w", pady=2)
        
        tk.Label(content, text=item["description"], font=("Helvetica", 10), 
                bg="white", fg="#334155", wraplength=220).pack(anchor="w", pady=(10, 0))
        
        # Contact button
        contact_btn = tk.Button(content, text="Contact", font=("Helvetica", 10, "bold"),
                               bg="#3b82f6", fg="white", border=0, cursor="hand2",
                               command=lambda: self.contact_owner(item))
        contact_btn.pack(anchor="w", pady=(15, 0), ipadx=15, ipady=5)
    
    def show_post_form(self):
        self.header_title.config(text="Post New Item")
        self.clear_content()
        
        form_container = tk.Frame(self.content_frame, bg="white")
        form_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        form = tk.Frame(form_container, bg="white")
        form.pack(padx=40, pady=30, fill="both", expand=True)
        
        tk.Label(form, text="Item Type", font=("Helvetica", 11, "bold"), 
                bg="white").pack(anchor="w", pady=(0, 10))
        
        type_frame = tk.Frame(form, bg="white")
        type_frame.pack(fill="x", pady=(0, 20))
        
        self.item_type = tk.StringVar(value="lost")
        tk.Radiobutton(type_frame, text="Lost Item", variable=self.item_type, value="lost",
                      font=("Helvetica", 10), bg="white", activebackground="white").pack(side="left", padx=(0, 20))
        tk.Radiobutton(type_frame, text="Found Item", variable=self.item_type, value="found",
                      font=("Helvetica", 10), bg="white", activebackground="white").pack(side="left")
        
        # Form fields
        self.title_entry = self.create_form_field(form, "Item Title*", "e.g., iPhone 14 Pro")
        self.category_entry = self.create_form_field(form, "Category*", "e.g., Electronics")
        self.location_entry = self.create_form_field(form, "Location*", "e.g., Library - 2nd Floor")
        
        tk.Label(form, text="Description*", font=("Helvetica", 11, "bold"), 
                bg="white").pack(anchor="w", pady=(10, 5))
        
        self.description_text = scrolledtext.ScrolledText(form, height=6, font=("Helvetica", 10),
                                                          bg="#f8fafc", border=1, relief="solid")
        self.description_text.pack(fill="x", pady=(0, 20))
        
        self.contact_entry = self.create_form_field(form, "Contact Email*", "your@email.com")
        
        # Submit button
        submit_btn = tk.Button(form, text="Post Item", font=("Helvetica", 12, "bold"),
                              bg="#3b82f6", fg="white", border=0, cursor="hand2",
                              command=self.submit_item)
        submit_btn.pack(fill="x", pady=20, ipady=12)
    
    def create_form_field(self, parent, label, placeholder):
        tk.Label(parent, text=label, font=("Helvetica", 11, "bold"), 
                bg="white").pack(anchor="w", pady=(10, 5))
        
        entry = tk.Entry(parent, font=("Helvetica", 10), bg="#f8fafc", border=1, relief="solid")
        entry.insert(0, placeholder)
        entry.config(fg="#94a3b8")
        entry.pack(fill="x", ipady=8, pady=(0, 10))
        
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, "end")
                entry.config(fg="black")
        
        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, placeholder)
                entry.config(fg="#94a3b8")
        
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        
        return entry
    
    def submit_item(self):
        title = self.title_entry.get()
        if title in ["", "e.g., iPhone 14 Pro"]:
            messagebox.showerror("Error", "Please enter item title")
            return
        
        messagebox.showinfo("Success", f"Your {self.item_type.get()} item has been posted successfully!")
        self.switch_view("lost" if self.item_type.get() == "lost" else "found")
    
    def show_matches(self):
        self.header_title.config(text="Potential Matches")
        self.clear_content()
        
        info_frame = tk.Frame(self.content_frame, bg="white")
        info_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(info_frame, text="🎯", font=("Arial", 48), bg="white").pack(pady=(100, 20))
        tk.Label(info_frame, text="No matches found yet", font=("Helvetica", 18, "bold"), 
                bg="white", fg="#64748b").pack()
        tk.Label(info_frame, text="We'll notify you when potential matches are detected", 
                font=("Helvetica", 11), bg="white", fg="#94a3b8").pack(pady=10)
    
    def contact_owner(self, item):
        messagebox.showinfo("Contact", f"Contact: {item['contact']}\n\nYou can reach out regarding:\n{item['title']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LostAndFoundDashboard(root)
    root.mainloop()