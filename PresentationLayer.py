import BusinessLayer as bl
import tkinter as tk

actions = bl.BusinessLayer()
signedIn = False

# create main window
root = tk.Tk()
root.title("IN450 Unit 2 Assignment")
root.geometry("820x500")

# create login frame
loginFrame = tk.Frame(root, height=500, width=400)
functionsFrame = tk.Frame(root, height=500, width=400)

# create output area
outputArea = tk.Text(functionsFrame, height=10, width=50)


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

def onSingInClick(username, password):
    #verify username and password
    #pass username and password to db

    pass


# create buttons
button1 = tk.Button(functionsFrame, text="Show Table A Row Count", command=lambda:onButtonClick("A") , width=20, height=2)
button2 = tk.Button(functionsFrame, text="List Table B Names", command=lambda:onButtonClick("B"), width=20, height=2)


# login fields
loginUsernameLabel = tk.Label(loginFrame, text="Username: ")
loginUsernameLabel.grid(row=0, column=0, padx=10, pady=5, sticky="e")

loginUsername = tk.Entry(loginFrame)
loginUsername.grid(row=0, column=1, padx=10, pady=5)

loginPasswordLabel = tk.Label(loginFrame, text="Password: ")
loginPasswordLabel.grid(row=1, column=0, padx=10, pady=5, sticky="e")

loginPassword = tk.Entry(loginFrame)
loginPassword.grid(row=1, column=1, padx=10, pady=5)

loginServerLabel = tk.Label(loginFrame, text="Server: ")
loginServerLabel.grid(row=2, column=0, padx=10, pady=5, sticky="e")

loginServer = tk.Entry(loginFrame)
loginServer.grid(row=2, column=1, padx=10, pady=5)

loginDatabaseLabel = tk.Label(loginFrame, text="Database: ")
loginDatabaseLabel.grid(row=3, column=0, padx=10, pady=5, sticky="e")

loginDatabase = tk.Entry(loginFrame)
loginDatabase.grid(row=3, column=1, padx=10, pady=5)


# place elements on window
loginFrame.grid(row=0, column=0, sticky="nsew")
functionsFrame.grid(row=0, column=1, sticky="nsew")


button1.pack(padx=10, pady=20)
button2.pack(padx=10, pady=10)
outputArea.pack(padx=10,  pady=20)

# cun the app
root.mainloop()