import wikipedia


def main():
    while True:
        # Prompt the user for input
        query = input("Enter a page title or search phrase (or blank to quit): ").strip()

        # Check if the user wants to quit
        if not query:
            print("Exiting...")
            break

        try:
            # Get the Wikipedia page
            page = wikipedia.page(query, auto_suggest=False)

            # Print page title, summary, and URL
            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            # Handle disambiguation pages
            print("Disambiguation page! Please specify a more specific query.")

        except wikipedia.exceptions.PageError as e:
            # Handle page not found
            print("Page not found. Please enter a valid page title or search phrase.")

        except Exception as e:
            # Handle other unexpected errors
            print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
