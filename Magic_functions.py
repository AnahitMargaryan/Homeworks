# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def __repr__(self) :
#         rep = 'Person(' + self.name + ',' + str(self.age) + ')'
#         return rep

# person = Person("John", 20)
# print(person)

class PlayingCard: 
    
    card = ("Jack","Queen", "King", "Ace")
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit 

    def __str__(self):
        rep = 'PlayingCard(' + self.rank + ',' + self.suit + ')'
        return rep
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        return self.rank != other.rank or self.suit != other.suit

    def __lt__(self, other):
        return PlayingCard.card.index(self.rank) < PlayingCard.card.index(other.rank)

    def __le__(self, other):
        return PlayingCard.card.index(self.rank) <= PlayingCard.card.index(other.rank)

    def __gt__(self, other):
        return PlayingCard.card.index(self.rank) >= PlayingCard.card.index(other.rank)

    def __ge__(self, other):
        return PlayingCard.card.index(self.rank) >= PlayingCard.card.index(other.rank)

card1 = PlayingCard("Jack", "Spades")
card2 = PlayingCard("Queen", "Clubs")
card3 = PlayingCard("King", "Diamond")
card4 = PlayingCard("Ace", "Heart")

print(card1, card2, card3, card4)
print(card1 == card2)
print(card2 != card3)
print(card4 < card3)
print(card1 <= card4)
print(card4 > card1)
print(card1 >= card3)
