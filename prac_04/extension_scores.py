"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    scores_file.close()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")

    # Initialize a dictionary to store scores for each subject
    scores_per_subject = {subject: [] for subject in subjects}

    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        for subject, score in zip(subjects, score_strings):
            # Convert the score to an integer and append it to the subject's list
            scores_per_subject[subject].append(int(score))

    # Print the results in a nicely formatted table
    print("Subject\tMax\tMin\tAverage")
    for subject in subjects:
        scores = scores_per_subject[subject]
        max_score = max(scores)
        min_score = min(scores)
        avg_score = sum(scores) / len(scores)

        print(f"{subject}\t{max_score}\t{min_score}\t{avg_score:.2f}")


main()
