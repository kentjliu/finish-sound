# finish-sound

`finish-sound` is a simple, silly Python package that plays a sound when your code finishes executing. 
Specifically, it will be one of four random voices saying `"Your code is finished running!"`

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
