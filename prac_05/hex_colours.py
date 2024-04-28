COLOR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}


def get_color_code(color_name):
    # Convert the color name to lowercase for case-independent lookup
    color_name_lower = color_name.lower()

    # Check if the color name exists in the dictionary
    try:
        return COLOR_CODES[color_name_lower]

    except Exception as ex:
        print(ex)
        return None


# Main program loop
while True:
    # Get the user input for the color name
    color_name = input("Enter a color name (or leave blank to exit): ")

    # Check if the user entered a blank name to exit the loop
    if not color_name:
        break

    # Get the hexadecimal color code for the given name
    color_code = get_color_code(color_name)

    # Check if a valid color code was found
    if color_code:
        print(f"The hexadecimal code for {color_name} is {color_code}")
    else:
        print(f"Invalid color name: {color_name}")
