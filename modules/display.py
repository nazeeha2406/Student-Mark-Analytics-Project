from modules.load_data import load, SUBJECTS

def print_student(row):
    print()
    print(f"Student Name : {row['Name']}")
    print(f"Register No  : {row['Register No']}")
    print()
    print("%12s %10s %8s %10s %12s %10s" % ("Tamil", "English", "Maths", "Physics", "Chemistry", "Biology"))
    print("%12s %10s %8s %10s %12s %10s" % (
        row["Tamil"], row["English"], row["Maths"],
        row["Physics"], row["Chemistry"], row["Biology"]
    ))
    print()

    tot = sum(row[s] for s in SUBJECTS)
    avg = tot / 6
    result = "PASS" if all(row[s] >= 35 for s in SUBJECTS) else "FAIL"
    eng_cutoff = row["Maths"] + ((row["Physics"] + row["Chemistry"]) / 2)
    medi_cutoff = ((row["Physics"] + row["Chemistry"]) / 2) + row["Biology"]

    print("%8s %10s %8s %14s %14s" % ("Total", "Average", "Result", "Eng.Cutoff", "Medi.Cutoff"))
    print("%8d %10.2f %8s %14.1f %14.1f" % (tot, avg, result, eng_cutoff, medi_cutoff))
    print()
    print("=" * 65)

def show_all():
    df = load()
    print()
    print(f"Total Students: {len(df)}")
    print("=" * 65)
    for _, row in df.iterrows():
        print_student(row)

def search_by_regno():
    df = load()
    regno = input("Enter Register No: ").strip().lower()
    print()
    match = df[df["Register No"].str.lower() == regno]
    if match.empty:
        print("Register Number not found.")
    else:
        print_student(match.iloc[0])