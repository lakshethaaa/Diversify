import tkinter as tk

# Function to be called when the "Calculate" button is clicked
def calculate_output():
    # Get values from the input fields
    button1_value = button1_entry.get()
    button2_value = button2_entry.get()
    button3_value = button3_entry.get()
    
    # Perform some operation or calculation using the input values
    # For demonstration, we'll just concatenate the input values
    output_text = list_of_percentage_returns(button1_value,button2_value,button3_value)
    
    # Update the text area with the result
    output_textarea.config(state=tk.NORMAL)  # Enable text area for editing
    output_textarea.delete(1.0, tk.END)  # Clear previous text
    output_textarea.insert(tk.END, output_text)  # Insert new text
    output_textarea.config(state=tk.DISABLED)  # Disable text area for editing

# Create the main window
root = tk.Tk()
root.title("Button Input App")

# Input fields for button values
button1_label = tk.Label(root, text="Button 1 Value:")
button1_label.pack()

button1_entry = tk.Entry(root)
button1_entry.pack()

button2_label = tk.Label(root, text="Button 2 Value:")
button2_label.pack()

button2_entry = tk.Entry(root)
button2_entry.pack()

button3_label = tk.Label(root, text="Button 3 Value:")
button3_label.pack()

button3_entry = tk.Entry(root)
button3_entry.pack()

# Button to trigger the function
calculate_button = tk.Button(root, text="Calculate", command=calculate_output)
calculate_button.pack()

# Text area to display the output
output_textarea = tk.Text(root, height=5, width=30)
output_textarea.pack()
output_textarea.config(state=tk.DISABLED)  # Disable text area for editing

# Start the Tkinter main loop
root.mainloop()
