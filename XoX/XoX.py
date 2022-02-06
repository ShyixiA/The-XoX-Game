import os

class XOX():

    def __init__(self):

        self.First_transactions()

        self.Start_game()
# These two purposes are to play as soon as we derive an object from the class.
    def First_transactions(self):

        self.Wood = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']    
        self.Player = 1  # The game will start with Player 1
# Since our game board will be 3x3, we defined a 9-element list.
        # Oyun Durumları
        self.WİN = 1    
        self.DRAW = -1    
        self.Contunie = 0        
        #################
 
        self.Game = self.Contunie  # The game first started with the continuation.    
        self.sign = 'X'  # Since it's the first player's turn, the mark is X..
# Now we need to define three functions that we will use in the_startgame function.
    def Draw_Wood(self): # This function will allow us to redraw the game board every round.
        os.system('cls') # This function clears the board we DRAW before, so we don't crowd the console.

        print("   |   |   ") 
        print(" {} | {} | {} ".format(self.Wood[1], self.Wood[2], self.Wood[3]))    
        print("___|___|___")
        print("   |   |   ")     
        print(" {} | {} | {} ".format(self.Wood[4], self.Wood[5], self.Wood[6]))    
        print("___|___|___") 
        print("   |   |   ")    
        print(" {} | {} | {} ".format(self.Wood[7], self.Wood[8], self.Wood[9]))    
        print("   |   |   ") 
        
        # The process we do here is purely for appearance purposes.
        # We printed the lines that define the rows and columns and the values ​​on our board between them.
        # You can understand this better once we run the code.
    def Space_control(self,x): # This function will check if a cell on the board is empty.
        
        if(self.Wood[x] == ' '):    
            return True    
        else:    
            return False 
    def state_control(self): # This function will check the win, draw and attendance status.


         #Horizontal Win Check 
           
        if(self.Wood[1] == self.Wood[2] and self.Wood[2] == self.Wood[3] and self.Wood[1] != ' '): 
            # If the 1st, 2nd and 3rd cells are all equal and not equal to the space, a player has won the game.
    
            self.Game = self.WİN 
        
        elif(self.Wood[4] == self.Wood[5] and self.Wood[5] == self.Wood[6] and self.Wood[4] != ' '):    
            self.Game = self.WİN

        elif(self.Wood[7] == self.Wood[8] and self.Wood[8] == self.Wood[9] and self.Wood[7] != ' '):    
            self.Game = self.WİN 
        #Dikey WİN Kontrolü    
        elif(self.Wood[1] == self.Wood[4] and self.Wood[4] == self.Wood[7] and self.Wood[1] != ' '):    
            self.Game = self.WİN    

        elif(self.Wood[2] == self.Wood[5] and self.Wood[5] == self.Wood[8] and self.Wood[2] != ' '):    
            self.Game = self.WİN   
 
        elif(self.Wood[3] == self.Wood[6] and self.Wood[6] == self.Wood[9] and self.Wood[3] != ' '):    
            self.Game = self.WİN  
        #Çapraz WİN Kontrolü    
        elif(self.Wood[1] == self.Wood[5] and self.Wood[5] == self.Wood[9] and self.Wood[5] != ' '):    
            self.Game = self.WİN    

        elif(self.Wood[3] == self.Wood[5] and self.Wood[5] == self.Wood[7] and self.Wood[5] != ' '):    
            self.Game = self.WİN  
        #DRAW Kontrolü
        
        elif(self.Wood[1] != ' ' and self.Wood[2] != ' ' and self.Wood[3] != ' ' and self.Wood[4] != ' ' and self.Wood[5] != ' ' and self.Wood[6] != ' ' and self.Wood[7] != ' ' and self.Wood[8] != ' ' and self.Wood[9] != ' '):

            self.Game = self.DRAW   

        else:           
            self.Game = self.Contunie
    def Start_game(self):
        
        print("\n --- Welcome to XOX Game --- \n")

        Player_one = input("Enter The one player name: ")
        Player_two = input("Enter The two player name: ")

        print(f"{Player_one} [X] --- {Player_two} [O]\n")    

        input("press start to enter ")
        while(self.Game == self.Contunie): # Our cycle will continue as long as the game continues.
               
            self.Draw_Wood()  # We will redraw the board every round.

            if(self.Player % 2 != 0): # If it's player-1, the sign value will be 'X'.
                print(f"next player {Player_one}")    
                self.sign = 'X'    

            else:  # Otherwise it will be 'O'
                print(f"next player {Player_two}")    
                self.sign = 'O'    

            selecktt = int(input("Enter a number between 1 and 9 to mark : "))    
            
            if(self.Space_control(selecktt)): 

                self.Wood[selecktt] = self.sign  
                self.Player += 1  
                self.state_control()  
        self.Woodyı_çiz()    

        if(self.Game == self.DRAW):    
            print("* GAME DRAW *")    

        elif(self.Game == self.WİN):    
            self.Player -= 1    

            if(self.Player % 2 != 0):    
                print(f"* {Player_one} WİN *")
                print(f"* {Player_two} LOSE *")        
                
            else:    
                print(f"* {Player_two} WİN *")  
                print(f"* {Player_one} LOSE *")       

XOX() 