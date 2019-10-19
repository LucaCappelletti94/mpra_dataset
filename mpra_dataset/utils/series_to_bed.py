import pandas as pd
from .value_to_bed import value_to_bed


__all__ = ["series_to_bed"]


def series_to_bed(series: pd.Series, base_pairs: int) -> pd.DataFrame:
    """Return given series expanded into bed format.

    Parameters
    --------------
    series: pd.Series, series to expand into dataframe in bed format.
    base_pairs: int, window size for the nucleotides.

    Returns
    ----------------------
    Dataframe containing series encoded as bed values

    """
    df = series.apply(value_to_bed(base_pairs)).str.split(',', expand=True)
    df.columns = ["chr", "start", "end", "id"]
    return df
