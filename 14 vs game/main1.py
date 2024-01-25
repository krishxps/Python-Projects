from art import logo , vs
from random import choice
from game_data import data
from os import system

def Random_person():
    Random = choice(data)
    return Random


def details(Person):
    name = Person['name']
    country_names = Person['country']
    detail = Person['description']
    return f"{name}, {detail}, from {country_names}"


def compare(person_a , person_b):
    a_followers = person_a['follower_count']
    b_followers = person_b['follower_count']
    if a_followers > b_followers:
        return person_a
    else:
        return person_b
    
    
def play():
    score = 0
    playing = True
    person_a = Random_person()
    person_b = Random_person()
    while playing:
        print(logo)
        
        while person_a == person_b:
            person_b = Random_person()
            
        detail_of_a = details(person_a)
        detail_of_b = details(person_b)
        
        print(f"Compare A: {detail_of_a}")
        print(vs)
        print(f"Against B: {detail_of_b}")
        
        choice = input("Who has more follower 'a' or 'b'?\n Your choice:")
        winner = compare(person_a , person_b)
        
        if choice == "a" and person_a == winner:
            score += 1
            _ = system('cls')
            print(f"You Guess Right {person_a['name']} has {person_a['follower_count']}Million Followers and {person_b['name']} has {person_b['follower_count']}Million Followers.")
            print(f"Your Score = {score}")
            person_b = person_a
            
        elif choice == 'b' and person_b == winner:
            score += 1
            _ = system('cls')
            print(f"You Guess Right {person_b['name']} has {person_b['follower_count']}Million Followers and {person_a['name']} has {person_a['follower_count']}Million Followers.")
            print(f"Your Score = {score}")
            person_a = person_b
            
        else:
            playing = False
            _ = system('cls')
            print(f"Final Score = {score}")
            print(f"Wrong Guess {person_a['name']} has {person_a['follower_count']} Million Followers and {person_b['name']} has {person_b['follower_count']}Million Followers.")
            
play()