## label.py

**Reference:** [Detect people with a RaspberryPi, a thermal camera, Platypush and Tensorflow](https://blog.platypush.tech/article/Detect-people-with-a-RaspberryPi-a-thermal-camera-Platypush-and-a-pinch-of-machine-learning)

Once the images have been copied, and the directories for the labels created, run the label.py script provided in the repository to interactively label the images:
```
UTILS_DIR=~/projects/imgdetect-utils
cd "$UTILS_DIR"
python utils/label.py -d "$IMGDIR" --scale-factor 10
```
