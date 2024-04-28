import os
import json
import datetime  # Add this line to import the datetime module

# Import the Project class from project.py
from project import Project

# Constants
DATA_FILE = "projects.txt"


def load_projects(filename):
    projects = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            # Skip the header line
            next(file)
            for line in file:
                name, start_date, priority, estimate, completion = line.strip().split('\t')
                projects.append(Project(name, start_date, int(priority), float(estimate), int(completion)))
        print(f"Loaded {len(projects)} projects from {filename}.")
    else:
        print(f"No data file found at {filename}.")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        json.dump([project.to_dict() for project in projects], file)
    print(f"Projects saved to {filename}.")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > date]
        print("Filtered projects:")
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, estimate, completion))
    print("New project added successfully.")


def update_project(projects):
    print("Current projects:")
    for idx, project in enumerate(projects):
        print(f"{idx}: {project}")
    choice = int(input("Project choice: "))
    if 0 <= choice < len(projects):
        project = projects[choice]
        new_completion = input("New Percentage: ")
        if new_completion:
            project.update_completion(int(new_completion))
        new_priority = input("New Priority: ")
        if new_priority:
            project.update_priority(int(new_priority))
    else:
        print("Invalid project choice.")


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DATA_FILE)

    while True:
        print("\nMenu:")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").strip().lower()
            if save_choice.startswith('y'):
                save_projects(DATA_FILE, projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
