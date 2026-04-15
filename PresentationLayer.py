import IN450_BusinessLayer as bl
import tkinter as tk

actions = bl.BusinessLayer()

# create main window
root = tk.Tk()
root.title("IN450 Unit 2 Assignment")
root.geometry("800x500")

# create output area
outputArea = tk.Text(root, height=10, width=50)

# function to display output (built in presentation layer for text box display insert functionality)
def onButtonClick(function):
    outputArea.delete("1.0", tk.END)
    if function == "A":
        output = actions.numberOfRowsA()
        outputArea.insert(tk.END, output)
        return output
    elif function == "B":
        listInput = actions.listNamesB()
        for item in listInput:
            outputArea.insert(tk.END, f"{item}\n")

# create buttons
button1 = tk.Button(root, text="Show Table A Row Count", command=lambda:onButtonClick("A") , width=20, height=2)
button2 = tk.Button(root, text="List Table B Names", command=lambda:onButtonClick("B"), width=20, height=2)

# place elements on window
button1.pack(pady=20)
button2.pack(pady=10)
outputArea.pack(pady=20)

# cun the app
root.mainloop()