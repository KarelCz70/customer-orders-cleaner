import os
import pandas as pd

def main():
    os.makedirs("outputs", exist_ok=True)

    df = pd.read_csv("outputs/orders.csv", delimiter=";")

    summary = {
        "count": len(df),
        "total": int(df["value"].sum()),
        "average": round(df["value"].mean(), 2),
        "min": int(df["value"].min()),
        "max": int(df["value"].max()),
    }

    df_summary = pd.DataFrame(list(summary.items()), columns=["metric", "value"])
    df_summary.to_csv("outputs/summary.csv", index=False, sep=";")

    print("Saved: outputs/summary.csv")
    print(df_summary)

if __name__ == "__main__":
    main()

