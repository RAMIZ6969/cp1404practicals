import wikipedia
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="wikipedia")


def main():
    """Prompt the user for a page title or search phrase, then display page details."""
    print("Welcome to Wikipedia search!")

    title = input("Enter page title (or leave blank to exit): ").strip()
    while title:
        try:
            page = wikipedia.page(title)
            print(f"\nTitle: {page.title}")
            print(f"Summary: {page.summary[:300]}...")
            print(f"URL: {page.url}\n")
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print(f"Page titled '{title}' does not exist. Try another title.")
        except Exception as e:
            print(f"An error occurred: {e}")

        title = input("Enter page title (or leave blank to exit): ").strip()

    print("Thank you. Goodbye!")


if __name__ == "__main__":
    main()
