from math import floor, ceil

__all__ = ["value_to_bed"]

def value_to_bed(base_pairs:int):
    """Convert given value to bed format, expanding window to given base_pairs.
    
    Parameters
    ----------------------
    base_pairs:int, the window size to which expand windows of given values.

    Returns
    ----------------------
    Value formatted as bed file format.
    """
    def _value_to_bed(value:str)->str:
        chromosome, regions  = value.split("Mod_")[1].split("_")[0].split(":")
        start, end = regions.split("-")
        start = int(start)
        end = int(end)
        delta = base_pairs - (end-start)
        start = start-int(floor(delta/2))
        end = end+int(ceil(delta/2))
        return f"{chromosome},{start},{end},{chromosome}:{start}-{end}"
    return _value_to_bed