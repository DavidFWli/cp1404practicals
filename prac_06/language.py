from programming_language import ProgrammingLanguage

# Create ProgrammingLanguage objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print the objects to check the __str__ method
print(python)
print(ruby)
print(visual_basic)

# Create a list containing these objects
programming_languages = [python, ruby, visual_basic]

# Iterate over the list and print each object to verify the list works as expected
for language in programming_languages:
    print(language)