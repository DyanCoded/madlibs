def main():
    print("Welcome")
    print("Ready to have medium levels of fun?")
    print("Let's make some madlibs")
    prompt()
    pick_madlib()

def prompt():
    input("Enter to continue")

def pick_madlib():
    print("Pick A Madlib (1-3): ")
    print("1. The Day at the Zoo.")
    print("2. The Alien Encounter.")
    print("3. The First Date.")
    pick = input("Enter your Pick: ")
    if pick == "1":
        day_at_the_zoo()
    elif pick == "2":
        alien_encounter()
    elif pick == "3":
        first_date()
    else:
        print("Invalid Pick")
        pick_madlib()

def day_at_the_zoo():
    adjective1 = input("An Adjective: ")
    animal1 = input("An Animal: ")
    verb1 = input("A Verb, past tense: ")
    adjective2 = input("An Adjective: ")
    noun1 = input("A Noun: ")
    animal2 = input("An Animal: ")
    adjective3 = input("An Adjective: ")
    verb2 = input("A Verb: ")
    adverb1 = input("An Adverb: ")
    verb3 = input("A Verb, past tense: ")
    adjective4 = input("An Adjective: ")

    prompt()
    
    The_Day_at_the_Zoo = {f"Today I went to the zoo. I saw a {adjective1} {animal1} jumping up and down in its tree. It {verb1} through the large tunnel that led to its {adjective2} {noun1}. I got some peanuts and passed them through the cage to a gigantic {animal2} towering above my head. Feeding that animal made me hungry. I went to get a {adjective3} scoop of ice cream. it filled my stomach. Afterwards, I had to {verb2} {adverb1} to catch our bus. When I got home, I {verb3} my mom for a {adjective4} day at the zoo."}

    print(The_Day_at_the_Zoo)

def alien_encounter():
    adjective1 = input("An Adjective: ")
    colour = input("A Colour: ")
    number1 = input("A Number: ")
    plural_noun1 = input("Plural Noun: ")
    adjective2 = input("An Adjective: ")
    body_part1 = ("A Body Part: ")
    noun1 = input("A Noun: ")
    emotion1 = input("An Emotion: ")
    verb1 = input("A Verb: ")
    adjective3 = input("An Adjective: ")
    noun2 = input("A noun: ")
    food = input("food: ")
    silly_word = input("A Silly Word: ")

    The_Alien_Encounter = {f"Last night, I saw a {adjective1} light in the sky. Suddenly, a {colour} spaceship landed in my place! Out came {number1} {plural_noun1} with {adjective2} heads and {body_part1} for eyes. They said, 'Take us to your {noun1}!' I was so {emotion1} that I could only {verb1}. Then they gave me a {adjective3} gift, a glowing {noun2} that smelled like {food}. Before I could say '{silly_word}', they disappeared back into space!"}

    print(The_Alien_Encounter)

def first_date():
    name1 = input("A Name: ")
    place1 = input("A Place(restaurant, etc.): ")
    food1 = input("A Food: ")
    drink1 = input("A Drink: ")
    musician_name = input("A Musician Name: ")
    adjective1 = input("An Adjective: ")
    verb1 = input("A Verb(ending in -ing): ")
    funny_noise = input("A Funny Noise: ")
    animal1 = input("An Animal: ")
    random1 = input("A Random Object")
    reaction1 = input("A Reaction or Emotion")
    place2 = input("A Place to Escape to: ")

    prompt()

    The_First_Date = {f"It was a {adjective1} Friday evening when you met {name1} at {place1}. Everything started out normal — the waiter brought out a giant plate of {food1} and two tall glasses of {drink1}. You were just about to compliment {name1}’s smile when the background music changed to {musician_name}, and {name1} started {verb1} loudly. The whole restaurant froze. Somewhere in the distance, a {animal1} made a dramatic {funny_noise} sound. Trying to calm things down, you picked up a {random1} from the table and pretended it was a microphone. {name1} looked at you in {reaction1}, then joined in, singing along with {musician_name} like it was a concert. By the time the manager came over, half the restaurant was clapping, and someone even threw napkins like confetti. You both ran out laughing and escaped to the {place2}, swearing it was the weirdest but somehow perfect first date ever."}

    print(The_First_Date)

if __name__ == "__main__":
    main()