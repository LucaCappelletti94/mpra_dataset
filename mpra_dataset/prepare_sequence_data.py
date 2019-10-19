import subprocess
import pandas as pd
from typing import Dict
from fasta_one_hot_encoder import FastaOneHotEncoder
from .utils import store_bed, series_to_bed
import os

__all__ = ["prepare_sequence_data"]


def expand_sequences(path: str, target: str, genome: str, bed: str):
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)

    subprocess.run([
        "fastaFromBed",
        "-fi",
        f"{target}/{genome}.fa",
        "-bed",
        bed,
        "-fo",
        path
    ])


def encode_sequences(path: str, sequences: str):
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)

    FastaOneHotEncoder(
        nucleotides="acgtn",
        sparse=False
    ).transform_to_df(sequences).to_csv(path)


def prepare_sequence_data(raw: pd.DataFrame, file_name: str, target: str, settings: Dict):
    region = f"{target}/bed/{file_name}.bed"
    sequences = f"{target}/sequences/{file_name}.fa"
    encoded_sequences = f"{target}/encoded_sequences/{file_name}.fa"

    store_bed(
        series_to_bed(raw["Region"], settings["base_pairs"]),
        region
    )

    expand_sequences(sequences, target, settings["genome"], region)
    encode_sequences(encoded_sequences, sequences)
