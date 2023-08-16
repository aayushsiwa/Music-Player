# Music Player Application

This is a simple music player application built using Python's `tkinter` for the GUI and `pygame` for audio playback. The application allows users to play and manage their music files in a playlist-like interface.

## Features

- Play, pause, stop, and navigate through songs.
- Adjust volume using a slider control.
- Display song progress using a progress slider.
- Add individual songs or multiple songs to the playlist.
- Delete songs from the playlist or clear the entire playlist.

## Requirements

- Python 3.x
- `tkinter` library
- `pygame` library
- `mutagen` library
- `Pillow` library for image support

You can install all the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script using `python main.py`.
2. The application window will appear, showing the playlist and control buttons.
3. Use the "Add Songs" menu to add individual songs or multiple songs to the playlist.
4. Use the control buttons to navigate and manage the playlist:
   - Play/Pause: Play or pause the current song.
   - Stop: Stop the playback.
   - Next/Previous: Move to the next or previous song.
5. Adjust the volume using the volume slider.
6. The progress slider shows the current playback progress. Drag the slider to jump to a specific position within the song.
7. Use the "Remove Songs" menu to delete individual songs or clear the entire playlist.

## Note

- The script assumes that the audio files are located in the "audio" directory.
- Ensure that the image files referenced in the script (e.g., icons) are present in the "assets" directory.

## Authors

- [AayushSiwa](https://www.github.com/aayushsiwa)

## License

This project is licensed under the [MIT License](LICENSE).
