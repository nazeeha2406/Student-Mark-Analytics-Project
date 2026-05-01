import pandas as pd
import os

BUCKET_NAME = "student-mark-analytics"
FILE_KEY = "Studentdata.csv"
S3_PATH = f"s3://{BUCKET_NAME}/{FILE_KEY}"

SUBJECTS = ["Tamil", "English", "Maths", "Physics", "Chemistry", "Biology"]

def load():
    df = pd.read_csv(S3_PATH)
    return df

def save(df):
    df.to_csv(S3_PATH, index=False)
