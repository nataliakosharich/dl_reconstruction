# dl_reconstruction
Collection of colmap and deep learning featuring/matching integrations.
## Bash scripts
Run scripts from inside of the rep folder.
- **bash_build** to build docker image (will be named dl_docker)
- **bash_start** to run container from image
- **bash_enter** to enter running container
## Workspace
Workspace folder is mounted in /app/workspace in container, all files are shared. Datasets with images and scripts go there.
## HLoc scripts
Rep folder contains hloc folder. This folder is mounted in hloc library folder in container, so modified or new scripts can be added and used from container.
