MPRA dataset
======================
|travis|

Simple python package to build sequence (and in the future also epigenomic) data for MPRA.

How do I get this?
--------------------------------------------
In the future this package will be available on pip. Currently you need to clone and install the repository itself.

.. code:: bash

    git clone https://github.com/LucaCappelletti94/mpra_dataset.git
    cd mpra_dataset
    pip install .

You also need to install `bedtools <https://bedtools.readthedocs.io/en/latest/>`_. On macOS it is available on `brew <https://brew.sh/>`_, while on Debian/Ubuntu you can get it on apt.

For macOS:

.. code:: bash

    brew install bedtools

For Debian/Ubuntu:

.. code:: bash

    sudo apt install bedtools


Usage example
------------------------------------------------
To build the `default dataset <https://github.com/LucaCappelletti94/mpra_dataset/tree/master/dataset>`_ available within this repository, you just have to run:

.. code:: python

    from mpra_dataset import pipeline
    pipeline("dataset")

Once the dataset is rendered, you will find under the "encoded_sequences" directory the one-hot encoded nucleotides, and under "activity_ratios" the activity scores from the given raw files.


.. |travis| image:: https://travis-ci.com/LucaCappelletti94/mpra_dataset.svg?token=RksTFS6Qqghd4eDPtnKg&branch=master
    :target: https://travis-ci.com/LucaCappelletti94/mpra_dataset


Additional informations
------------------------------------------------
The liver enhancers MPRA activity ratios data comes from `the ncbi website <https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE83894&format=file&file=GSE83894%5FActivityRatios%2Etsv%2Egz>`_.