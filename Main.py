from modules import display, add_student, statistics, export

def print_menu():
    print()
    print("=" * 45)
    print("   STUDENT MARK REPORT SYSTEM".center(45))
    print("=" * 45)
    print("  1. Display All Students")
    print("  2. Search by Register No")
    print("  3. Add New Student")
    print("  4. Statistics")
    print("  5. Export Reports")
    print("  6. Exit")
    print("=" * 45)

def statistics_menu():
    print()
    print("-" * 40)
    print("  STATISTICS MENU")
    print("-" * 40)
    print("  1. Total Students, Pass & Fail Count")
    print("  2. No. of Centum in a Subject")
    print("  3. Average Mark in a Subject")
    print("  4. Maximum Mark in a Subject")
    print("  5. Minimum Mark in a Subject")
    print("  6. Students Failed in a Subject")
    print("  7. Back to Main Menu")
    print("-" * 40)

    while True:
        try:
            c = int(input("  Enter choice: "))
        except ValueError:
            print("  Invalid input.")
            continue

        if c == 1: statistics.pass_fail_count()
        elif c == 2: statistics.centum_count()
        elif c == 3: statistics.subject_average()
        elif c == 4: statistics.subject_maximum()
        elif c == 5: statistics.subject_minimum()
        elif c == 6: statistics.fail_in_subject()
        elif c == 7: break
        else: print("  Invalid choice.")

        print()
        again = input("  Back to Statistics Menu? (y/n): ").strip().lower()
        if again != 'y':
            break

def export_menu():
    print()
    print("-" * 40)
    print("  EXPORT MENU")
    print("-" * 40)
    print("  1. Export Top 10 Students")
    print("  2. Export Failed Students List")
    print("  3. Subject-wise Summary Report")
    print("  4. Back to Main Menu")
    print("-" * 40)

    while True:
        try:
            c = int(input("  Enter choice: "))
        except ValueError:
            print("  Invalid input.")
            continue

        if c == 1: export.export_toppers()
        elif c == 2: export.export_failed_students()
        elif c == 3: export.export_subject_summary()
        elif c == 4: break
        else: print("  Invalid choice.")

        print()
        again = input("  Back to Export Menu? (y/n): ").strip().lower()
        if again != 'y':
            break

def main():
    while True:
        print_menu()
        try:
            choice = int(input("  Enter choice: "))
        except ValueError:
            print("  Invalid input. Enter a number.")
            continue

        if choice == 1:
            display.show_all()
        elif choice == 2:
            display.search_by_regno()
        elif choice == 3:
            add_student.add_student()
        elif choice == 4:
            statistics_menu()
        elif choice == 5:
            export_menu()
        elif choice == 6:
            print()
            print("  Thank You. Goodbye!")
            print()
            break
        else:
            print("  Invalid choice. Try again.")

if __name__ == "__main__":
    main()