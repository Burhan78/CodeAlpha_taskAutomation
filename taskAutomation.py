
import re
import os
import shutil


# TASK 1: EMAIL ADDRESS EXTRACTOR

def email_extractor():

    inp_file = "inp.txt"
    opt_file = "ext_email.txt"

    try:
        # Check input file
        if not os.path.isfile(inp_file):
            raise FileNotFoundError("Input file not found!")

        # Read input file
        with open(inp_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Find email addresses
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        emails = re.findall(pattern, text)

        # Remove duplicate emails
        unique_emails = list(dict.fromkeys(emails))

        # Save emails into output file
        with open(opt_file, "w", encoding="utf-8") as file:

            for email in unique_emails:
                file.write(email + "\n")

        print("\n========== EMAIL EXTRACTOR ==========")

        if unique_emails:
            print(f"Total emails found: {len(unique_emails)}")

            for email in unique_emails:
                print(email)

            print(f"\nEmails saved in {opt_file}")

        else:
            print("No email addresses found!")

    except FileNotFoundError as e:
        print("Error:", e)

    except PermissionError:
        print("Permission denied!")

    except OSError as e:
        print("File operation error:", e)


# TASK 2: JPG FILE ORGANIZER

def jpg_organizer():

    src_folder = "Source"
    dst_folder = "Destination"

    try:
        # Check source folder
        if not os.path.exists(src_folder):
            raise FileNotFoundError("Source folder does not exist!")

        # Create destination folder
        os.makedirs(dst_folder, exist_ok=True)

        moved_files = 0

        # Read files from source folder
        for filename in os.listdir(src_folder):

            src_path = os.path.join(src_folder, filename)

            # Check JPG extension
            if os.path.isfile(src_path) and filename.lower().endswith(".jpg"):

                dst_path = os.path.join(dst_folder, filename)

                # Avoid overwriting existing files
                if os.path.exists(dst_path):
                    print(f"File already exists: {filename}")
                    continue

                # Move JPG file
                shutil.move(src_path, dst_path)

                print(f"Moved: {filename}")

                moved_files += 1

        print("\nAutomation completed successfully!")
        print(f"Total JPG files moved: {moved_files}")

    except FileNotFoundError as e:
        print("Error:", e)

    except PermissionError:
        print("Permission denied! Check folder permissions.")

    except OSError as e:
        print("File operation error:", e)

# MAIN MENU


while True:

    print("\n========== PYTHON AUTOMATION TOOLKIT ==========")

    print("1. Extract Email Addresses")
    print("2. Organize JPG Files")
    print("3. Exit")

    try:
        choice = int(input("\nEnter your choice (1-3): "))

        if choice == 1:
            email_extractor()

        elif choice == 2:
            jpg_organizer()

        elif choice == 3:
            print("\nThank you for using Python Automation Toolkit!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

    except ValueError:
        print("Invalid input! Please enter a number.")
