import pandas as pd
import csv


def save_to_csv(data, filename: str):
    """Saving news in CSV with separate columns
    """
    try:
        columns = ["title", "link", "date", "summary"]
        df = pd.DataFrame(data)

        for col in columns:
            if col not in df.columns:
                df[col] = ""

        df = df[columns]

        df.to_csv(filename, index=False, encoding="utf-8", sep=",", quoting=csv.QUOTE_ALL)
        print(f"[INFO] Data saved to {filename}")
    except Exception as e:
        print(f"[ERROR] Saving CSV failed: {e}")
