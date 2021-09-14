## label.py

Once the images have been copied, and the directories for the labels created, run the label.py script provided in the repository to interactively label the images:
```
UTILS_DIR=~/projects/imgdetect-utils
cd "$UTILS_DIR"
python utils/label.py -d "$IMGDIR" --scale-factor 10
```
