from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_spending(expenses: list[dict], out_file: Path = Path("spending.png")):
    df = pd.DataFrame(expenses)
    df["date"] = pd.to_datetime(df["date"])
    df_group = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
    df_group.index = df_group.index.to_timestamp()
    plt.figure(figsize=(8, 4))
    df_group.plot()
    plt.title("Monthly Spending")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig(out_file)
    plt.close()
