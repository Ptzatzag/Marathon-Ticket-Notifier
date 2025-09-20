import requests
from bs4 import BeautifulSoup
import time

URL = "https://copenhagenmarathon.dk/en/"
EXPECTED_TEXT = "Copenhagen Marathon 2026 The race is sold out"

def check_for_changes():
    try:
        page = requests.get(URL)
        page.raise_for_status()
        soup = BeautifulSoup(page.content, "html.parser")

        head_line_tag = soup.find("h1", class_="h1 headline-1 text-align-center")

        if head_line_tag:
            current_text = " ".join(head_line_tag.get_text().split())

            if current_text != EXPECTED_TEXT:
                print("Ticket availability detected!")
                print(f"URL: {URL}")
                return True

    except requests.exceptions.RequestException as e:
        print(f"Error checking website: {e}")

    return False

if __name__ == "__main__":
    if check_for_changes():
        input("Press Enter to exit...") 
    else:
        input("No updates\nPress enter to exit...")
