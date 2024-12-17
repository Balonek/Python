import tkinter as tk
import random
from PIL import Image, ImageTk

class Resize_image:
    def __init__(self, size=(250, 250)):
        self.size = size

    def resize(self, filepath):
        image = Image.open(filepath)
        image = image.resize(self.size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)

class RPS_appgame(tk.Frame):
    def __init__(self, master=None, title="Kamień, Papier, Nożyce"):
        super().__init__(master)
        self.master = master
        self.config(bg="white")
        self.master.title(title)
        self.master.config(bg="white")
        
        self.image_manager = Resize_image()
        self.grid(sticky="nsew") 
        
        self.images = {
            "rock": self.image_manager.resize("rock.png"),
            "paper": self.image_manager.resize("paper.png"),
            "scissors": self.image_manager.resize("scissors.png"),
        }
        
        self.result_text = tk.StringVar(value="Wybierz swój ruch")
        self.create_widgets()
    
    def create_widgets(self):

        choices_frame = tk.Frame(self, bg="white")
        choices_frame.grid(row=0, column=0, columnspan=3, pady=20, sticky="n")

        tk.Label(choices_frame, text="Twój wybór", bg="white", font=("Georgia", 16, "bold")).grid(row=0, column=0, padx=10)
        tk.Label(choices_frame, text="Wybór komputera", bg="white", font=("Georgia", 16, "bold")).grid(row=0, column=1, padx=10)
        
        self.player_choice_label = tk.Label(choices_frame, bg="white")
        self.player_choice_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.computer_choice_label = tk.Label(choices_frame, bg="white")
        self.computer_choice_label.grid(row=1, column=1, padx=10, pady=10)
        
        self.result_label = tk.Label(self, textvariable=self.result_text, bg="white", font=("Georgia", 16, "bold"))
        self.result_label.grid(row=1, column=0, columnspan=3, pady=20)
        
        button_options = {'bg': "white",'fg': "black",'activebackground': "#d3d3d3",'font': ("Georgia", 14),'width': 10}

        tk.Button(self, text="Kamień", command=lambda: self.play("rock"), **button_options).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self, text="Papier", command=lambda: self.play("paper"), **button_options).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self, text="Nożyce", command=lambda: self.play("scissors"), **button_options).grid(row=2, column=2, padx=10, pady=10)


    def determine_winner(self, player, computer):
        if player == computer:
            return "REMIS! :/ \nKliknij poniżej by zagrać ponownie"
        elif (
            (player == "rock" and computer == "scissors") or 
            (player == "paper" and computer == "rock") or 
            (player == "scissors" and computer == "paper")
        ):
            return "WYGRAŁEŚ! :)\nKliknij poniżej by zagrać ponownie"
        else:
            return "PRZEGRAŁEŚ! :( \nKliknij poniżej by zagrać ponownie"

    def play(self, player_choice):
        self.config(bg="white")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        self.player_choice_label.config(image=self.images[player_choice])
        self.computer_choice_label.config(image=self.images[computer_choice])
        result = self.determine_winner(player_choice, computer_choice)
        self.result_text.set(result)

if __name__ == "__main__":
    root = tk.Tk()
    app1 = RPS_appgame(root)
    root.mainloop()