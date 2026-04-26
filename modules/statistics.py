from modules.load_data import load, SUBJECTS

def get_subject():
    while True:
        sub = input("Enter Subject (Tamil/English/Maths/Physics/Chemistry/Biology): ").strip().title()
        if sub in SUBJECTS:
            return sub
        print(f"  Invalid subject. Choose from: {', '.join(SUBJECTS)}")

def pass_fail_count():
    df = load()
    total = len(df)
    passed = df[SUBJECTS].apply(lambda row: all(row >= 35), axis=1).sum()
    failed = total - passed
    print()
    print(f"  Total Students : {total}")
    print(f"  Pass           : {passed}")
    print(f"  Fail           : {failed}")

def centum_count():
    sub = get_subject()
    df = load()
    count = (df[sub] == 100).sum()
    print()
    print(f"  No. of Centum in {sub} : {count}")

def subject_average():
    sub = get_subject()
    df = load()
    avg = df[sub].mean()
    print()
    print(f"  Average mark in {sub} : {avg:.2f}")

def subject_maximum():
    sub = get_subject()
    df = load()
    maxx = df[sub].max()
    name = df.loc[df[sub] == maxx, "Name"].values[0]
    print()
    print(f"  Maximum mark in {sub} : {maxx}  ({name})")

def subject_minimum():
    sub = get_subject()
    df = load()
    minn = df[sub].min()
    name = df.loc[df[sub] == minn, "Name"].values[0]
    print()
    print(f"  Minimum mark in {sub} : {minn}  ({name})")

def fail_in_subject():
    sub = get_subject()
    df = load()
    failed = df[df[sub] < 35]
    count = len(failed)
    print()
    print(f"  No. of Students Failed in {sub} : {count}")
    if count > 0:
        print()
        for _, row in failed.iterrows():
            print(f"    {row['Register No']}  {row['Name']}  [{sub}: {row[sub]}]")