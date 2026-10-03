import random
cards = ["jack", "queen", "king"]

def main():
    random.seed(1)
    print(random.choices(cards, weights=[0, 50, 50], k=2))
   
    
main()    
    