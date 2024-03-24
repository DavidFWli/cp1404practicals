# Import CSV module
import csv


# Define Guitar class
class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year


# Function to read guitars from CSV
def read_guitars(filename):
    guitars = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


# Function to write guitars to CSV
def write_guitars(filename, guitars):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


# Main function
def main():
    # Read existing guitars from CSV
    filename = 'guitars.csv'
    guitars = read_guitars(filename)

    # Display existing guitars
    print("Existing Guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort guitars by year
    guitars.sort()

    # Display sorted guitars
    print("\nSorted Guitars:")
    for guitar in guitars:
        print(guitar)

    # Ask user for new guitars
    while True:
        name = input("Enter guitar name (or enter to stop): ")
        if not name:
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))

    # Write guitars back to CSV
    write_guitars(filename, guitars)
    print("Guitars written to guitars.csv")


if __name__ == "__main__":
    main()
