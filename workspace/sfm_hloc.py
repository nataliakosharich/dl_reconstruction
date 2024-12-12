
import tqdm, tqdm.notebook
tqdm.tqdm = tqdm.notebook.tqdm  # notebook-friendly progress bars
from pathlib import Path

from hloc import (
    extract_features, 
    match_features,
    match_dense,
    reconstruction, 
    visualization, 
    pairs_from_order,
)

images = Path('rec_data/def1/159532_159712_fix/images/')

outputs = Path('rec_data/def1/159532_159712_fix/outputs/') 
sfm_pairs = outputs / "pairs-order.txt"
sfm_dir = outputs / "loftr"

dense_conf = match_dense.confs["loftr"]

pairs_from_order.main(images, sfm_pairs)

feature_path, match_path = match_dense.main(
    dense_conf, sfm_pairs, images, outputs
)

model = reconstruction.main(sfm_dir, images, sfm_pairs, feature_path, match_path)

input("Press Enter to continue...")
