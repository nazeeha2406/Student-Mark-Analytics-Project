from modules.load_data import load, save, SUBJECTS
import pandas as pd

def validate_mark(subject):
    while True:
        try:
            mark = int(input(f"{subject:<12}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("  Mark must be between 0 and 100. Try again.")
        except ValueError:
            print("  Invalid input. Enter a number.")

def add_student():
    df = load()
    c = 'y'

    while c == 'y':
        print()

        # Name input
        name = input("Student Name  : ").strip().upper()

        # Register No with duplicate check
        while True:
            regno = input("Register No   : ").strip().lower()
            if regno in df["Register No"].str.lower().values:
                print("  Register Number already exists. Enter a different one.")
            else:
                break

        # Mark inputs with validation
        marks = [validate_mark(s) for s in SUBJECTS]

        # Build new row
        new_row = pd.DataFrame([[name, regno] + marks],columns=["Name", "Register No"] + SUBJECTS)
        df = pd.concat([df, new_row], ignore_index=True)
        save(df)

        print("  Student record added successfully.")
        print()
        c = input("Add another student? (y/n): ").strip().lower()

    print()
    print("Returning to main menu...")