import argparse
from collections import defaultdict
from pathlib import Path

import numpy as np

from . import logger


def main(images_path, output):

    logger.info("Creating image pairs from directory...")
    pairs = []
    match_pairs = []
    paths = [f for f in images_path.iterdir() if f.is_file()]
    images = []
    for i in paths:
        images.append(i.name)
    images.sort()
    #print(images)
    image_pairs = []
    for i in range(0, len(images), 2):
        image_pairs.append([images[i], images[i+1]])
    pairs = image_pairs.copy()
    #print(pairs)
    buffer = []
    for i, j in image_pairs:
        if buffer:
            i_b, j_b = buffer
            pairs.append([i_b, i])
            pairs.append([i_b, j])
            pairs.append([j_b, i])
            pairs.append([j_b, j])
        buffer = [i, j]

    logger.info(f"Created {len(pairs)} pairs.")
    with open(output, "w") as f:
        f.write("\n".join(" ".join([i, j]) for i, j in pairs))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_path", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    main(**args.__dict__)
