import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string

# Pre-defined adjectives and nouns lists
adjectives = ["Cool", "Happy", "Brave", "Clever", "Mighty", "Swift", "Shiny", "Funky", "Chill", "Bold"]
nouns = ["Tiger", "Dragon", "Falcon", "Wizard", "Knight", "Panda", "Wolf", "Phoenix", "Ninja", "Bear"]

def generate_username(include_numbers, include_specials, length, count):
    """Generate random usernames based on preferences."""
    usernames = []
    for _ in range(count):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        username = adjective + noun

        if include_numbers:
            username += str(random.randint(10, 99))
        if include_specials:
            username += random.choice(string.punctuation)

        # The length check is removed to allow usernames to include numbers and specials
        if length and len(username) > length:
            username = username[:length]
        
        usernames.append(username)
    return usernames
def on_generate():
    try:
        count = int(entry_count.get())
        length = int(entry_length.get()) if entry_length.get() else 0
        include_numbers = var_numbers.get()
        include_specials = var_specials.get()
        
        usernames = generate_username(include_numbers, include_specials, length, count)
        text_output.delete("1.0", tk.END)  # Clear previous output
        text_output.insert(tk.END, "\n".join(usernames))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for count and length.")

def save_usernames():
    usernames = text_output.get("1.0", tk.END).strip()
    if not usernames:
        messagebox.showwarning("No Usernames", "No usernames to save!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(usernames)
        messagebox.showinfo("Saved", f"Usernames saved to {file_path}")

# Create main window
root = tk.Tk()
root.title("Random Username Generator")
root.geometry("500x500")

# Input options
frame_options = tk.Frame(root)
frame_options.pack(pady=10)

tk.Label(frame_options, text="Number of Usernames:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_count = tk.Entry(frame_options, width=10)
entry_count.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_options, text="Max Username Length:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_length = tk.Entry(frame_options, width=10)
entry_length.grid(row=1, column=1, padx=5, pady=5)

var_numbers = tk.BooleanVar(value=True)
chk_numbers = tk.Checkbutton(frame_options, text="Include Numbers", variable=var_numbers)
chk_numbers.grid(row=2, column=0, columnspan=2, sticky="w")

var_specials = tk.BooleanVar(value=False)
chk_specials = tk.Checkbutton(frame_options, text="Include Special Characters", variable=var_specials)
chk_specials.grid(row=3, column=0, columnspan=2, sticky="w")

# Generate button
btn_generate = tk.Button(root, text="Generate Usernames", command=on_generate, bg="blue", fg="white")
btn_generate.pack(pady=10)

# Output display
text_output = tk.Text(root, height=15, width=50)
text_output.pack(pady=10)

# Save button
btn_save = tk.Button(root, text="Save to File", command=save_usernames, bg="green", fg="white")
btn_save.pack(pady=10)

# Run the app
root.mainloop()