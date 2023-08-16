import csv
import re
import pandas as pd
from unidecode import unidecode

DATE = "8-11"
INPUT_FILE = f"input/{DATE}-emails.csv"
OUTPUT_FILE = f"output/{DATE}-email-upload.csv"
IS_STUDENT = False
DEPARTMENT = "Giao Ly"


def main():
    # Set the header for the CSV
    with open(OUTPUT_FILE, "w") as f:
        writer = csv.writer(f)
        headers = ["Username", "First name", "Last name", "Display name",
                   "Job title", "Department", "Office number", "Office phone",
                   "Mobile phone", "Fax", "Alternate email", "Address",
                   "City", "State or province", "Zip or postal code", "Country or region"]
        writer.writerow(headers)

    # Loop through input file and write to output file
    with open(INPUT_FILE, encoding="utf-8-sig") as template:
        reader = csv.DictReader(template)
        for entry in reader:
            first = format_name(entry["First Name"])
            middle_initials = format_middle_name(entry["Middle Name (N/A if you don't have one)"])
            last = format_name(entry["Last Name"])
            status = entry["Have you volunteered in Giao Ly before?"]
            username = format_username(first, middle_initials, last, IS_STUDENT)

            if status == "no-i-m-new":
                with open(OUTPUT_FILE, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow([username, first, last, f"{first} {last}",
                                     "", DEPARTMENT, "", "",
                                     "", "", "", "",
                                     "", "", "", ""])
                    print(f"Name: {first} {last}\nUsername: {username}\n")

    # Remove duplicates
    df = pd.read_csv(OUTPUT_FILE)
    df = df.drop_duplicates(subset="Username")
    df.to_csv(OUTPUT_FILE, index=False)


def normalize_string(text):
    """
    Takes a string and strips everything but the letters a - z
    :param string text: text
    :return string: text with everything stripped except for the letters a - z
    """
    return re.sub(r"[^A-Za-z]", "", text.lower())


def format_name(name):
    """
    Takes a string and formats it by removing accents and anything except for
    letters, hyphens, and spaces, and returns it with the first letter capitalized
    Example: nguyên -> Nguyen
    :param string name: name
    :return string: name with first letter capitalized, and everything removed
    except for letters, hyphens, and spaces
    """
    normalized = unidecode(name)
    name = re.sub(r"[^\w\s-]", "", normalized)
    return name.title().strip()


def format_middle_name(name):
    """
    Takes a middle name and returns just the first initials of each word
    Example: Joseph Gordon-Levitt -> jgl
    :param string name: name
    :return string: first initials of each word (separated by spaces or hyphens) in name
    """
    if name.lower() == "n/a":
        return ""

    words = filter(None, re.split(r"[-\s]", name))
    initials = [normalize_string(word[0]) for word in words]
    return "".join(initials)


def format_username(first, middle, last, is_student):
    """
    Formats the username for the email
    Example: Viet Thanh Nguyen -> viet.t.nguyen@school.vmpwa.org
    :param string first: first name
    :param string middle: middle initials
    :param string last: last name
    :param boolean is_student: whether person is or is not a student
    :return:
    """
    first = normalize_string(first).lower()
    last = normalize_string(last).lower()
    middle = middle.lower()

    username = f"{first}.{middle}.{last}" if middle else f"{first}.{last}"
    domain = "school" if not is_student else "student"
    return f"{username}@{domain}.vmpwa.org"


if __name__ == "__main__":
    main()
