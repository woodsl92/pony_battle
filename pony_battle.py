"""
This script sets up a Pony class object to define the stats of the competing ponies
and a battle function to determine the winner of the battle between two ponies.
"""
import argparse
import random

class Pony:
    def __init__(self, name, magic, kindness, laughter, generosity, loyalty, honesty):
        self.name = name
        self.stats = {
            'magic': magic,
            'kindness': kindness,
            'laughter': laughter,
            'generosity': generosity,
            'loyalty': loyalty,
            'honesty': honesty
        }

    def generate_random_modifier(self):
        """Generates a random modifier between -2 and 2 for each trait"""
        return {trait: random.randint(-2, 2) for trait in self.stats}

    def calculate_total_score(self):
        """
        Calculates the total score for the pony
        Total score is the sum of the base scores and the random modifier
        """
        random_modifiers = self.generate_random_modifier()
        total_score = sum(self.stats[trait] + random_modifiers[trait] for trait in self.stats)
        return total_score

# Create the ponies TODO: store and get these from a database
ponies = {
    'twilight sparkle': Pony('Twilight Sparkle', magic=10, kindness=7, laughter=6, generosity=8, loyalty=6, honesty=5),
    'rainbow dash': Pony('Rainbow Dash', magic=7, kindness=6, laughter=7, generosity=6, loyalty=10, honesty=6),
    'fluttershy': Pony('Fluttershy', magic=6, kindness=10, laughter=6, generosity=7, loyalty=6, honesty=6),
    'applejack': Pony('Applejack', magic=6, kindness=6, laughter=6, generosity=6, loyalty=10, honesty=10),
    'rarity': Pony('Rarity', magic=7, kindness=6, laughter=6, generosity=10, loyalty=6, honesty=6),
    'pinkie pie': Pony('Pinkie Pie', magic=6, kindness=6, laughter=10, generosity=6, loyalty=6, honesty=6)
}

# Set up argument parsing
parser = argparse.ArgumentParser(prog="hoof_to_hoof", description="Pony Battle: Pit your favourite ponies head to head in the ultimate battle of friendship.")
parser.add_argument('-p1', '--pony1', type=str, help="Name of the first pony", required=False)
parser.add_argument('-p2', '--pony2', type=str, help="Name of the second pony", required=False)
parser.add_argument('--list_ponies', action="store_true", help="List the names of available competitors")

def main():
    args = parser.parse_args()

    # If --list_ponies in args print list of available names 
    if args.list_ponies:
        print("The ponies ready to compete are:")
        for pony in ponies:
            print(pony)
        exit()
    # If pony1 or pony2 weren't supplied, print help and exit.
    if not args.pony1 or not args.pony2:
        parser.print_help()
        exit()

    # Convert pony names from args to lowercase
    args.pony1 = args.pony1.lower()
    args.pony2 = args.pony2.lower()

    # Get the ponies from the arguments
    pony1 = ponies.get(args.pony1)
    pony2 = ponies.get(args.pony2)

    if pony1 and pony2:
        print(f"{pony1.name} vs {pony2.name}")
        score1 = pony1.calculate_total_score()
        score2 = pony2.calculate_total_score()

        print(f"{pony1.name} score: {score1}")
        print(f"{pony2.name} score: {score2}")
        if score1 > score2:
            print(f"{pony1.name} wins!")
        elif score2 > score1:
            print(f"{pony2.name} wins!")
        else:
            print("It's a tie!")
    else:
        print("One or both pony names are invalid.")

if __name__ == '__main__':
    main()
