import pkg_resources
import random
from IPython.display import Audio, display, Javascript

def play_finish_sound_notebook(sound_name=None):
    """
    Plays a specified finish sound or a random finish sound from the package's resources using IPython.display.Audio in Colab.
    Automatically plays the sound using JavaScript.

    Args:
        sound_name (str): Optional. Name of the specific sound file (with extension) to play.
    """
    # List all files in the 'sounds' directory
    sound_files = pkg_resources.resource_listdir("finish_sound", "sounds")

    # Filter out only .mp3 files
    mp3_files = [file for file in sound_files if file.endswith(".mp3")]

    # Determine the sound file to play
    if sound_name and sound_name in mp3_files:
        selected_sound = sound_name
    else:
        if sound_name:
            print(f"Specified sound '{sound_name}' not found. Playing a random sound instead.")
        selected_sound = random.choice(mp3_files)

    # Get the full path to the selected sound file
    sound_file = pkg_resources.resource_filename("finish_sound", f"sounds/{selected_sound}")

    # Create the audio object
    audio = Audio(sound_file)

    # Display the audio player and play it automatically using JavaScript
    display(audio)
    display(Javascript('document.querySelector("audio").play()'))




def play_finish_sound():
    """
    Plays a random finish sound from the package's resources.
    """
    # List all files in the 'sounds' directory
    sound_files = pkg_resources.resource_listdir("finish_sound", "sounds")
    
    # Filter out only .mp3 files
    mp3_files = [file for file in sound_files if file.endswith(".mp3")]
    
    # Select a random file from the list
    random_sound = random.choice(mp3_files)
    
    # Get the full path to the randomly selected sound file
    sound_file = pkg_resources.resource_filename(
        "finish_sound", f"sounds/{random_sound}"
    )
    
    # print(f"Code finished. Playing sound: {random_sound}")
    playsound(sound_file)
