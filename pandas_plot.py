import os
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # ensure output directory
    os.makedirs("outputs", exist_ok=True)

    # load cleaned data
    df = pd.read_csv("outputs/orders.csv", delimiter=";")

    # create histogram
    plt.figure(figsize=(8, 5))
    plt.hist(df["value"], bins=5)

    plt.title("Order Values Distribution")
    plt.xlabel("Value")
    plt.ylabel("Count")

    # save figure
    output_file = "outputs/value_distribution.png"
    plt.savefig(output_file)
    plt.close()

    print(f"Saved: {output_file}")


if __name__ == "__main__":
    main()
