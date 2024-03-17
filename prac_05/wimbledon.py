import csv
from collections import defaultdict


# Read the CSV file and parse the data
def read_wimbledon_data(filename):
    champions = defaultdict(int)  # Keep track of the number of wins for each champion
    countries = set()  # Record all unique countries
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            champion = row[2]
            country = row[1]
            champions[champion] += 1  # Increment the number of wins for the champion
            countries.add(country)  # Add the country to the set
    return champions, countries


# Print the champions and the number of times they have won
def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, count in sorted(champions.items(), key=lambda x: x[1], reverse=True):
        print(f"{champion} {count}")


# Print the different countries that have won Wimbledon
def display_countries(countries):
    countries = sorted(countries)
    print("\nThese {} countries have won Wimbledon:".format(len(countries)))
    print(", ".join(countries))


# Main function
def main():
    filename = "wimbledon.csv"  # Name of the CSV file
    champions, countries = read_wimbledon_data(filename)
    display_champions(champions)
    display_countries(countries)



if __name__ == "__main__":
    main()
