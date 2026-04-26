import pandas as pd
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "Studentdata.csv")

SUBJECTS = ["Tamil", "English", "Maths", "Physics", "Chemistry", "Biology"]

def load():
    df = pd.read_csv(CSV_PATH)
    return df

def save(df):
    df.to_csv(CSV_PATH, index=False)