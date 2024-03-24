import datetime


class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __repr__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def update_completion(self, new_completion):
        if 0 <= new_completion <= 100:
            self.completion = new_completion
            print("Completion percentage updated successfully.")
        else:
            print("Invalid completion percentage. It must be between 0 and 100.")

    def update_priority(self, new_priority):
        self.priority = new_priority
        print("Priority updated successfully.")

    def to_dict(self):
        return {
            "name": self.name,
            "start_date": self.start_date.strftime('%d/%m/%Y'),
            "priority": self.priority,
            "estimate": self.estimate,
            "completion": self.completion
        }

    @staticmethod
    def from_dict(data):
        return Project(data["name"], data["start_date"], data["priority"], data["estimate"], data["completion"])
