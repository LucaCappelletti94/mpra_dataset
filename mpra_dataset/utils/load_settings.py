from json import load

__all__ = ["load_settings"]


def load_settings(target: str):
    """Load the settings file in given target dataset.
        target:str, the dataset.
    """
    with open(f"{target}/settings.json", "r") as f:
        return load(f)
