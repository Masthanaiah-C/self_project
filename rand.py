import random
#class to generate computer choice
class gen:
    def com_choice(self):
        k=random.Random()
        c=k.randrange(1,4,1)
        return c
#class to say the winner of each turn
class comp:
  def result (self,my,com):
    if [my,com] in [["rock","scissors"],["scissors","paper"],["paper","rock"]]:
      return [1,0]
    elif [com,my] in [["rock","scissors"],["scissors","paper"],["paper","rock"]]:
      return [0,1]
    else:
      return [0,0]
