import os
import csv 
import pandas as pd

def read_valid_numbers_from_txt(filename="orders.txt", min_value=1, max_value=100):
    valid_numbers = []
    invalid_lines = []

    with open(filename, "r", encoding="utf-8") as file:
        for line_no, line in enumerate(file, start=1):
            raw = line.strip()

            if raw == "":
                continue  # ignore empty lines

            if not raw.isdigit():
                invalid_lines.append((line_no, raw, "not a positive integer"))
                continue

            number = int(raw)
            if not (min_value <= number <= max_value):
                invalid_lines.append((line_no, raw, f"out of range {min_value}-{max_value}"))
                continue

            valid_numbers.append(number)

    return valid_numbers, invalid_lines

def save_txt_report(numbers, invalids, filename="outputs/report.txt"):
    os.makedirs("outputs", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        file.write("ORDERS REPORT (TXT)\n")
        file.write("-------------------\n\n")

        file.write(f"Valid count: {len(numbers)}\n")
        file.write(f"Valid total: {sum(numbers)}\n")
        file.write(f"Valid average: {round(sum(numbers) / len(numbers), 2) if numbers else 0}\n\n")

        file.write("Valid numbers:\n")
        file.write(", ".join(map(str, numbers)) + "\n\n")

        file.write("Invalid lines:\n")
        if not invalids:
            file.write("None\n")
        else:
            for line_no, raw, reason in invalids:
                file.write(f"Line {line_no}: '{raw}' -> {reason}\n")
def save_valid_numbers_csv(numbers, filename="outputs/orders.csv", delimiter=";"):
    os.makedirs("outputs", exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["value"])  # header

        for n in numbers:
            writer.writerow([n])                


def main():
    numbers, invalids = read_valid_numbers_from_txt("orders.txt", min_value=1, max_value=100)

    print("VALID:", numbers)
    print("COUNT:", len(numbers))
    print("TOTAL:", sum(numbers))

    print("\nINVALID LINES:")
    if not invalids:
        print("None")
    else:
        for line_no, raw, reason in invalids:
            print(f"Line {line_no}: '{raw}' -> {reason}")
    
    save_txt_report(numbers, invalids)
    print("\nSaved: outputs/report.txt")
        
    save_valid_numbers_csv(numbers)
    print("Saved: outputs/orders.csv")
    
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
  