import tkinter as tk
from tkinter import messagebox

class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

# Function to handle adding expenses to the expense list
def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    
    if category and amount:
        try:
            amount = float(amount)
            expense = Expense(category, amount)
            expenses.append(expense)
            update_expense_list()
            update_category_totals()
            clear_entry_fields()
        except ValueError:
            messagebox.showwarning("Invalid Amount", "Please enter a valid numerical amount.")
    else:
        messagebox.showwarning("Incomplete Information", "Please enter both category and amount.")

# Function to update the expense list in the Listbox
def update_expense_list():
    listbox.delete(0, tk.END)
    for expense in expenses:
        listbox.insert(tk.END, f"{expense.category} - ${expense.amount:.2f}")

# Function to update the category totals
def update_category_totals():
    category_totals = {}
    for expense in expenses:
        if expense.category in category_totals:
            category_totals[expense.category] += expense.amount
        else:
            category_totals[expense.category] = expense.amount
    
    totals_text.set("\n".join([f"{category}: ${total:.2f}" for category, total in category_totals.items()]))

# Function to clear entry fields
def clear_entry_fields():
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

# Create the main Tkinter window
root = tk.Tk()
root.title("Expense Tracker")

# Entry widgets for adding expenses
category_entry = tk.Entry(root, width=30)
category_entry.pack(pady=5)

amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)

# Buttons to add expenses
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack(pady=5)

# Listbox to display expenses
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack(pady=10)

# Label to display category totals
totals_text = tk.StringVar()
totals_label = tk.Label(root, textvariable=totals_text)
totals_label.pack()

# Start with some sample expenses
expenses = [Expense("Groceries", 50.25), Expense("Dining Out", 30.50)]
update_expense_list()
update_category_totals()

# Start the Tkinter event loop
root.mainloop()
