import random

def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks and create a funny story.")
    
    # Template for Mad Libs
    story_template = (
        "Once upon a time, there was a {adjective} {noun} who loved to {verb}. "
        "Every day, it would go to the {place} and {verb2} happily. "
        "One day, it met a {adjective2} {animal} who became its best friend!"
    )
    
    # Taking user inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    verb2 = input("Enter another verb: ")
    adjective2 = input("Enter another adjective: ")
    animal = input("Enter an animal: ")
    
    # Filling in the template
    story = story_template.format(
        adjective=adjective, noun=noun, verb=verb, place=place,
        verb2=verb2, adjective2=adjective2, animal=animal
    )
    
    print("\nHere is your funny story!")
    print("-" * 50)
    print(story)
    print("-" * 50)

# Run the Mad Libs game
mad_libs()
