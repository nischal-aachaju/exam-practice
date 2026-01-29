import tkinter as tk
from tkinter import messagebox
import re

class ModernLoginUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")
        
        # Center window
        self.center_window()
        
        # Create main container
        main_frame = tk.Frame(root, bg="#0f172a")
        main_frame.pack(expand=True, fill="both", padx=40, pady=40)
        
        # Logo/Title
        title = tk.Label(main_frame, text="Welcome Back", font=("Helvetica", 28, "bold"), 
                        bg="#0f172a", fg="#f8fafc")
        title.pack(pady=(0, 5))
        
        subtitle = tk.Label(main_frame, text="Sign in to your account", 
                           font=("Helvetica", 11), bg="#0f172a", fg="#94a3b8")
        subtitle.pack(pady=(0, 40))
        
        # Email field
        email_label = tk.Label(main_frame, text="Email", font=("Helvetica", 10, "bold"), 
                              bg="#0f172a", fg="#e2e8f0", anchor="w")
        email_label.pack(fill="x", pady=(0, 5))
        
        self.email_entry = self.create_entry(main_frame, "Enter your email")
        self.email_entry.pack(fill="x", pady=(0, 20))
        
        # Password field
        password_label = tk.Label(main_frame, text="Password", font=("Helvetica", 10, "bold"), 
                                 bg="#0f172a", fg="#e2e8f0", anchor="w")
        password_label.pack(fill="x", pady=(0, 5))
        
        self.password_entry = self.create_entry(main_frame, "Enter your password", show="•")
        self.password_entry.pack(fill="x", pady=(0, 10))
        
        # Forgot password
        forgot_frame = tk.Frame(main_frame, bg="#0f172a")
        forgot_frame.pack(fill="x", pady=(0, 25))
        
        forgot_btn = tk.Label(forgot_frame, text="Forgot password?", 
                             font=("Helvetica", 9), bg="#0f172a", fg="#60a5fa", 
                             cursor="hand2")
        forgot_btn.pack(side="right")
        forgot_btn.bind("<Button-1>", lambda e: self.forgot_password())
        
        # Login button
        login_btn = tk.Button(main_frame, text="Sign In", font=("Helvetica", 12, "bold"),
                             bg="#3b82f6", fg="white", border=0, cursor="hand2",
                             activebackground="#2563eb", activeforeground="white",
                             command=self.login)
        login_btn.pack(fill="x", ipady=12)
        
        # Hover effects for login button
        login_btn.bind("<Enter>", lambda e: login_btn.config(bg="#2563eb"))
        login_btn.bind("<Leave>", lambda e: login_btn.config(bg="#3b82f6"))
        
        # Divider
        divider_frame = tk.Frame(main_frame, bg="#0f172a")
        divider_frame.pack(fill="x", pady=25)
        
        tk.Frame(divider_frame, bg="#334155", height=1).pack(side="left", fill="x", expand=True, padx=(0, 10))
        tk.Label(divider_frame, text="OR", bg="#0f172a", fg="#64748b", font=("Helvetica", 9)).pack(side="left")
        tk.Frame(divider_frame, bg="#334155", height=1).pack(side="left", fill="x", expand=True, padx=(10, 0))
        
        # Social login buttons
        google_btn = self.create_social_button(main_frame, "Continue with Google", "#4285f4")
        google_btn.pack(fill="x", pady=(0, 10))
        
        github_btn = self.create_social_button(main_frame, "Continue with GitHub", "#333333")
        github_btn.pack(fill="x")
        
        # Sign up link
        signup_frame = tk.Frame(main_frame, bg="#0f172a")
        signup_frame.pack(side="bottom", pady=(20, 0))
        
        tk.Label(signup_frame, text="Don't have an account? ", 
                bg="#0f172a", fg="#94a3b8", font=("Helvetica", 9)).pack(side="left")
        
        signup_link = tk.Label(signup_frame, text="Sign up", 
                              bg="#0f172a", fg="#60a5fa", font=("Helvetica", 9, "bold"),
                              cursor="hand2")
        signup_link.pack(side="left")
        signup_link.bind("<Button-1>", lambda e: self.signup())
        
        # Bind Enter key to login
        self.root.bind("<Return>", lambda e: self.login())
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_entry(self, parent, placeholder, show=None):
        frame = tk.Frame(parent, bg="#1e293b", highlightbackground="#334155", 
                        highlightthickness=1, highlightcolor="#3b82f6")
        
        entry = tk.Entry(frame, font=("Helvetica", 11), bg="#1e293b", fg="#f8fafc",
                        border=0, insertbackground="#f8fafc", show=show)
        entry.insert(0, placeholder)
        entry.config(fg="#64748b")
        entry.pack(padx=15, pady=12, fill="x")
        
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, "end")
                entry.config(fg="#f8fafc")
                if show:
                    entry.config(show="•")
        
        def on_focus_out(event):
            if entry.get() == "":
                entry.config(show="")
                entry.insert(0, placeholder)
                entry.config(fg="#64748b")
        
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        
        return frame
    
    def create_social_button(self, parent, text, color):
        btn = tk.Button(parent, text=text, font=("Helvetica", 10),
                       bg=color, fg="white", border=0, cursor="hand2",
                       activebackground=color, activeforeground="white")
        btn.config(command=lambda: messagebox.showinfo("Info", f"{text} clicked"))
        
        def on_enter(e):
            btn.config(bg=self.adjust_color(color, -20))
        
        def on_leave(e):
            btn.config(bg=color)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.config(height=2)
        
        return btn
    
    def adjust_color(self, hex_color, amount):
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        rgb = tuple(max(0, min(255, c + amount)) for c in rgb)
        return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
    
    def login(self):
        email = self.email_entry.winfo_children()[0].get()
        password = self.password_entry.winfo_children()[0].get()
        
        if email == "Enter your email" or not email:
            messagebox.showerror("Error", "Please enter your email")
            return
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Please enter a valid email")
            return
        
        if password == "Enter your password" or not password:
            messagebox.showerror("Error", "Please enter your password")
            return
        
        messagebox.showinfo("Success", f"Login successful!\n\nEmail: {email}")
    
    def forgot_password(self):
        messagebox.showinfo("Forgot Password", "Password reset link would be sent to your email")
    
    def signup(self):
        messagebox.showinfo("Sign Up", "Redirecting to sign up page...")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernLoginUI(root)
    root.mainloop()