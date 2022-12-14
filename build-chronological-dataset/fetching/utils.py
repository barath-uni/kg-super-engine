"""Assortment of useful utility functions 
"""

import os
import ujson as json

import logging
logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

def jsonl_generator(fname):
    """ Returns generator for jsonl file """
    for line in open(fname, 'r'):
        line = line.strip()
        if len(line) < 3:
            d = {}
        elif line[len(line) - 1] == ',':
            d = json.loads(line[:len(line) - 1])
        else:
            d = json.loads(line)
        yield d

def get_batch_files(fdir):
    """ Returns paths to files in fdir """
    filenames = os.listdir(fdir)
    filenames = [os.path.join(fdir, f) for f in filenames]
    logging.debug(f"Fetched {len(filenames)} files from {fdir}")
    return filenames

