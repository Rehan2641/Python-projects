
import random
import tkinter as tk

print("• Hello guys this is Number Guessing game in python.")
print("• You have 10 chance to win the game, so best of luck👍.")
print()

Random = random.randint(1,100)
chance = 10

def guess():
    global chance
    
    a = int(entry.get())
        
    if a == Random:
            feedback.config(text="You Won! 🎉", fg="green")
            button.config(state="disabled")
    elif a<Random:
            feedback.config(text="Too Low! ⬇️", fg="blue")
    elif a>Random:
            feedback.config(text="Too High! ⬆️", fg="red") 
            
    chance -= 1
    attempts.config(text=f"Attempts: {chance}") 
    entry.delete(0, tk.END) 
                    
    if chance > 10 and a != Random:
        feedback.config(text=f"Game Over❌ Number was {Random}", fg="red")
        button.config(state="disabled")

   
# graphics user interface

gui = tk.Tk()
gui.title("GAME")
gui.geometry('500x400')

label = tk.Label(gui, text="Guess the number".upper(), font=("Helvetica", 10, "bold"),bg="orange",fg="white",bd=4,relief="ridge")
label.pack()

entry = tk.Entry(gui, width=10,font=("Helvetica", 10),bg="white",fg="black",bd=4,relief="ridge")
entry.pack(pady=2)

button = tk.Button(gui, text="Guess", font=("Arial",10), bg='green', fg='white',command=guess,bd=4,relief="ridge")
button.pack(pady=1)

feedback = tk.Label(gui, text="", font=("Arial", 10), fg="black")
feedback.pack(pady=3)

attempts = tk.Label(gui, text="Attempts:", font=("Arial", 12), fg="black")
attempts.pack()

gui.bind("<Return>", lambda event: guess())

gui.config(bg="#00FFFF")
gui.mainloop()