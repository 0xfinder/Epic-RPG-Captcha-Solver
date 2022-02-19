# Epic-RPG-Captcha-Solver

## Overview

Fun little machine learning project to solve Epic RPG captchas, trained on about 4000 images.

## Installation

### Requirements

- CUDA (if using GPU)
- Python 3

### Set-up

- ```git clone https://github.com/0xfinder/Epic-RPG-Captcha-Solver.git```
- ```cd epic-rpg-captcha-solver```
- ```pip install -r requirements.txt```
- Get dataset from [Kaggle](https://www.kaggle.com/evriskon/epic-rpg-captcha)
- Extract to ```data``` in working directory
- Run `imageclassifier.py` in `src`
- Models will be saved in `models`, use it however you like

## Limitations

- There are currently 15 classes, all of which contain coloured and greyscale images. Not sure whether to separate them or not since the accuracy is pretty bad for greyscale images.
- Wolf skin also affects the accuracy a lot since the colours are similar to other item greyscale images. (Possible solution: convert all images to greyscale and train on that)
- Some classes have very little data to work on despite the collective size being 4000 images since the items that appear in the captcha depends on the user's area, items in higher areas appear less often.
- Sorting the images took a lot of time, better way to collect and sort data might be to sort them when scraping, using the model, or to artifically generate captchas to train the model on.


## Update

I made a captcha generator so you can opt to use that if you want, I won't really be maintaining this project as it was a side project and I've had my fair share of fun.