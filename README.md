# finish-sound

**Current Release**: 0.1.4

`finish-sound` is a simple, silly Python package that plays a sound when your code finishes executing. 
Specifically, it will be one of four random voices saying `"Your code is finished running!"`

## Demo
For your convenience, we have provided a Google Colab Notebook with which you can use to follow along:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kentjliu/finish-sound/blob/main/finish_sound_demo.ipynb)

## Installation

You can install the package via `pip`:
```
pip install finish-sound
```

## For Colab

Example usage

```
from finish_sound import play_finish_sound_notebook

...
// some long task (eg. training large diffusion model)

play_finish_sound_notebook()
```

## Local machine

Example usage

```
from finish_sound import play_finish_sound

...
// some long task (eg. loading llama model checkpoints)

play_finish_sound()
```

## Looking forward

* Plan to add more voices/sounds
* Add option to pick specific voice/sound from a set menu by passing in a string argument
* Tweak the sound: pitch, volume, etc.
