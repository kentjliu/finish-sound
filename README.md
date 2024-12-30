# finish-sound

**Current Release**: 0.2.0

`finish-sound` is a simple, silly Python package that plays a sound when your code finishes executing. 
By defualt, it will be one of four random voices saying `"Your code is finished running!"`

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

### Custom Sounds
You can now create your custom sound to play when your code finishes running using our `CustomSound` class and `play_custom_sound` method (built on top of Google's `gtts` package).

```
from finish_sound import *

sound = CustomSound()
sound.text = 'This is my custom sound!`

// some long task (eg. scraping websites)

play_custom_sound(sound)
```

You can also set the local accent of the voice. By default, it is an Australian accent.

```
sound.accent = 'co.za' # South African accent
```

Refer to the table below for options.

| Local Accent                 | Param                                    |
|-------------------------|-------------------------------------------------|
| English (Australia)    | `com.au`          |
| English (United Kingdom)       | `co.uk` |
| English (United States)    | `us`       |
| English (Canada)  | `ca` |
| English (India)     | `co.in`             |
| English (Ireland)      | `ie`          |
| English (South Africa)     | `co.za`               |
| English (Nigeria)      | `com.ng`   |


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
* Tweak the sound: pitch, volume, etc.
