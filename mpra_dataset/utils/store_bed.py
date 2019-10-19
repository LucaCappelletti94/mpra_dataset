import pandas as pd
import os

__all__ = ["store_bed"]


def store_bed(bed: pd.DataFrame, path: str):
    """Store given dataframe as bed file."""
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    bed.to_csv(path, index=False, sep="\t", header=False)
