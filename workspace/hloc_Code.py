
import tqdm, tqdm.notebook
tqdm.tqdm = tqdm.notebook.tqdm  # notebook-friendly progress bars
from pathlib import Path

from hloc import extract_features, match_features, reconstruction, visualization, pairs_from_order
from hloc.visualization import plot_images, read_image
from hloc.utils import viz_3d

images = Path('rec_data/def1/159532_159712_fix/images/')
outputs = Path('rec_data/def1/159532_159712_fix/outputs/')
 
sfm_pairs = outputs / 'pairs-sfm.txt'
loc_pairs = outputs / 'pairs-loc.txt'
sfm_dir = outputs / 'sfm'
features = outputs / 'features.h5'
matches = outputs / 'matches.h5'

feature_conf = extract_features.confs['sift']
matcher_conf = match_features.confs['disk+lightglue']

references = [str(p.relative_to(images)) for p in (images).iterdir()]

extract_features.main(feature_conf, images, image_list=references, feature_path=features)
pairs_from_order.main(images, sfm_pairs)
match_features.main(matcher_conf, sfm_pairs, features=features, matches=matches);



model = reconstruction.main(sfm_dir, images, sfm_pairs, features, matches, image_list=references)

input("Press Enter to continue...")
