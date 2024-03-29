"""Generate funny names by randomly combining names from 2 separate lists."""
import sys
import random

# I see now that the book made a few mistakes on purpose to teach about some
# things related to code style and formatting.  Still, some things, like the
# use of string.format instead of f-strings, are just me disagreeing with the
# author's implementation.
def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    # Adding italics, assuming your terminal supports it
    # From: https://stackoverflow.com/a/13559470
    print("Welcome to the \x1B[3mPsych\x1B[0m 'Sidekick Name Picker'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread',
             'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
             'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
             'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
             "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil',
             'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"',
             'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
             'Pitchfork Ben', 'Potato Bug', 'Pushmeet','Rock Candy',
             'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'",
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
             'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
             'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
            'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
            'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
            'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
            'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
            'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed',
            'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners',
            'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        
        # This is how the book does it, but I think I can do it cleaner
        # print("\n\n")
        # print("{} {}".format(first_name, last_name), file=sys.stderr)
        # print("\n\n")
        
        # Like above, using terminal escape codes to color the output
        # Also, an f-string instead of string.format
        print(f"\n\n \033[31m{first_name} {last_name}\033[0m \n\n")
        
        try_again = input("\n\n Try again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break
        
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
