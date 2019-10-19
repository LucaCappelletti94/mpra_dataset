from .utils import load_settings
import pandas as pd
import os
from ucsc_genomes_downloader import download_genome
from .prepare_sequence_data import prepare_sequence_data


__all__ = ["pipeline"]


def pipeline(target: str):
    """Render the pipeline in given target dataset.
        target:str, the dataset to render.
    """
    settings = load_settings(target)
    genome = settings["genome"]
    download_genome(genome, path=f"{target}")
    for file_name in settings["file_names"]:
        raw = pd.read_csv(f"{target}/raw/{file_name}.tsv.gz", sep="\t")
        prepare_sequence_data(raw, file_name, target, settings)
        
        path = f"{target}/activity_ratios/{file_name}.csv"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        raw[["WT"]].to_csv(path)