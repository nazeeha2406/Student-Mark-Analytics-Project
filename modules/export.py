from modules.load_data import load, SUBJECTS
import os

EXPORT_PATH = os.path.join(os.path.dirname(__file__), "..", "data")

def export_toppers():
    df = load()
    df["Total"] = df[SUBJECTS].sum(axis=1)
    top10 = df.sort_values("Total", ascending=False).head(10)
    top10 = top10.drop(columns=["Total"])
    path = os.path.join(EXPORT_PATH, "top10_students.csv")
    top10.to_csv(path, index=False)
    print()
    print(f"  Top 10 students exported to: data/top10_students.csv")
    print()
    rank = 1
    df_sorted = df.sort_values("Total", ascending=False).head(10)
    for _, row in df_sorted.iterrows():
        print(f"  Rank {rank:>2} : {row['Name']:<25} Total: {int(row['Total'])}")
        rank += 1

def export_failed_students():
    df = load()
    failed = df[df[SUBJECTS].apply(lambda row: any(row < 35), axis=1)]
    path = os.path.join(EXPORT_PATH, "failed_students.csv")
    failed.to_csv(path, index=False)
    print()
    print(f"  Failed students exported to: data/failed_students.csv")
    print(f"  Total failed: {len(failed)}")

def export_subject_summary():
    df = load()
    print()
    print(f"{'Subject':<12} {'Average':>10} {'Max':>6} {'Min':>6} {'Centum':>8} {'Failed':>8}")
    print("-" * 55)
    for sub in SUBJECTS:
        avg = df[sub].mean()
        maxx = df[sub].max()
        minn = df[sub].min()
        centum = (df[sub] == 100).sum()
        failed = (df[sub] < 35).sum()
        print(f"{sub:<12} {avg:>10.2f} {maxx:>6} {minn:>6} {centum:>8} {failed:>8}")