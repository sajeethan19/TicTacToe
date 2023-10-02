import customtkinter
import game
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("304x304")
        self.title("TikTacToe")

        # add widgets to app
        self.button1 = customtkinter.CTkButton(self, text=game.plane[0][0], width=100, height=100, command=self.button_click1)
        self.button1.grid(row=0, column=0, padx=1, pady=1)
        self.button2 = customtkinter.CTkButton(self, text=game.plane[0][1], width=100, height=100, command=self.button_click2)
        self.button2.grid(row=0, column=1, padx=1, pady=1)
        self.button3 = customtkinter.CTkButton(self, text=game.plane[0][2], width=100, height=100, command=self.button_click3)
        self.button3.grid(row=0, column=2, padx=1, pady=1)
        self.button4 = customtkinter.CTkButton(self, text=game.plane[1][0], width=100, height=100, command=self.button_click4)
        self.button4.grid(row=1, column=0, padx=1, pady=1)
        self.button5 = customtkinter.CTkButton(self, text=game.plane[1][1], width=100, height=100, command=self.button_click5)
        self.button5.grid(row=1, column=1, padx=1, pady=1)
        self.button6 = customtkinter.CTkButton(self, text=game.plane[1][2], width=100, height=100, command=self.button_click6)
        self.button6.grid(row=1, column=2, padx=1, pady=1)
        self.button7 = customtkinter.CTkButton(self, text=game.plane[2][0], width=100, height=100, command=self.button_click7)
        self.button7.grid(row=2, column=0, padx=1, pady=1)
        self.button8 = customtkinter.CTkButton(self, text=game.plane[2][1], width=100, height=100, command=self.button_click8)
        self.button8.grid(row=2, column=1, padx=1, pady=1)
        self.button9 = customtkinter.CTkButton(self, text=game.plane[2][2], width=100, height=100, command=self.button_click9)
        self.button9.grid(row=2, column=2, padx=1, pady=1)

    # add methods to app
    def button_click1(self):
        print("button click")
        game.clicked(0,0)
        self.button1 = customtkinter.CTkButton(self, text=game.plane[0][0], width=100, height=100)
        self.button1.grid(row=0, column=0, padx=1, pady=1)
    def button_click2(self):
        print("button click")
        game.clicked(0,1)
        self.button1 = customtkinter.CTkButton(self, text=game.plane[0][1], width=100, height=100)
        self.button1.grid(row=0, column=1, padx=1, pady=1)
    def button_click3(self):
        print("button click")
        game.clicked(0,2)
        self.button1 = customtkinter.CTkButton(self, text=game.plane[0][2], width=100, height=100)
        self.button1.grid(row=0, column=2, padx=1, pady=1)
    def button_click4(self):
        print("button click")
        game.clicked(1,0)
        self.button1 = customtkinter.CTkButton(self, text=game.plane[1][0], width=100, height=100)
        self.button1.grid(row=1, column=0, padx=1, pady=1)
    def button_click5(self):
        print("button click")
        game.clicked(1,1)
        self.button1 = customtkinter.CTkButton(self, text=game.plane[1][1], width=100, height=100)
        self.button1.grid(row=1, column=1, padx=1, pady=1)
    def button_click6(self):
        print("button click")
        game.clicked(1,2)
        self.button1 = customtkinter.CTkButton(self, text=game.plane[1][2], width=100, height=100)
        self.button1.grid(row=1, column=2, padx=1, pady=1)
    def button_click7(self):
        print("button click")
        game.clicked(2,0)
        self.button1 = customtkinter.CTkButton(self, text=game.plane[2][0], width=100, height=100)
        self.button1.grid(row=2, column=0, padx=1, pady=1)
    def button_click8(self):
        print("button click")
        game.clicked(2,1)
        self.button1 = customtkinter.CTkButton(self, text=game.plane[2][1], width=100, height=100)
        self.button1.grid(row=2, column=1, padx=1, pady=1)
    def button_click9(self):
        print("button click")
        game.clicked(2,2)
        self.button1 = customtkinter.CTkButton(self, text=game.plane[2][2], width=100, height=100)
        self.button1.grid(row=2, column=2, padx=1, pady=1)


app = App()
app.mainloop()