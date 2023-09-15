# Define the base class player
class Player:
      def play(self):
             Print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(Player):
       def play(self):
              Print("The Batsman is batting.")

# Define the derived class Bowler
Class Bowler(Player):
        def play(self):
               Print("The Bowler is bowling.")

# create objects of Batsman and Bowler classes
batsman = Batsman ()
bowler = Bowler()

# call the play() method for each object
batsman.play()
bowler.play()