import random
import pkg_resources
import pygame

def play_finish_sound():
    """
    Plays a random finish sound from the package's resources using pygame.
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
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load the sound and play it
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    
    # Keep the program running until the sound is finished playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Check every 100ms

