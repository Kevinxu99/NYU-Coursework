import random
class Die:
    def __init__(self,faces=6):
        self.number_of_faces=faces
        self.curr_face_value=random.randint(1,faces)
        
    def roll(self):
        self.curr_face_value=random.randint(1,self.number_of_faces)

    def __repr__(self):
        return "You rolled "+str(self.curr_face_value)+"."

class PigGamePlayer:
    def __init__(self,name):
        self.name=name
        self.die=Die()
        self.score=0

    def play_turn(self):
        print(self.name,"'s turn:",sep="")
        score=0
        while 1:
            self.die.roll()
            print(repr(self.die))
            if(self.die.curr_face_value==1):
                score=0
                break
            score+=self.die.curr_face_value
            print("Your score for this turn is:",score)
            t=input("Roll again? (tyoe 'r' for roll, or 'h' for hold): ")
            if(t=='h'):
                break
        self.score+=score
        print("You scored",score,"points this turn. Your total score is",self.score)
            
class PigGame:
    def __init__(self,player1_name,player2_name):
        self.player1=PigGamePlayer(player1_name)
        self.player2=PigGamePlayer(player2_name)

    def play(self):
        while(self.player1.score<100 and self.player2.score<100):
            print("")
            self.player1.play_turn()
            if(self.player1.score>=100):
                break
            print("")
            self.player2.play_turn()
        print("")
        if(self.player1.score>=100):
            print(self.player1.name,"won!")
        else:
            print(self.player2.name,"won!")
        
def main():
    name1=input("Player #1, enter your name: ")
    name2=input("Player #2, enter your name: ")
    game1=PigGame(name1,name2)
    game1.play()

main()
