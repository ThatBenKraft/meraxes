"""
Allows for use of the Create3 AudioNoteVector publisher to play midi tracks.
"""

import os
import time

import mido
import rclpy  # type: ignore
from builtin_interfaces.msg import Duration  # type: ignore
from geometry_msgs.msg import Twist  # type: ignore
from irobot_create_msgs.msg import AudioNote, AudioNoteVector  # type: ignore
from rclpy.node import Node  # type: ignore

__author__ = "Ben Kraft"
__copyright__ = "None"
__credits__ = "Ben Kraft"
__license__ = "MIT"
__version__ = "1.1"
__maintainer__ = "Ben Kraft"
__email__ = "benjamin.kraft@tufts.edu"
__status__ = "Prototype"

rclpy.init()


def main():
    """
    Runs main song actions.
    """
    current_directory = os.path.dirname(os.path.realpath(__file__))

    VICTORY_SONG = os.path.join(current_directory, "tracks", "Victory Robot Song.mid")
    # VICTORY_SONG = os.path.join(current_directory, "tracks", "Victory Robot Song.mid")
    # PIRATE_SONG = os.path.join(current_directory, "tracks", "new_pirate.mid")
    # WHOA = os.path.join(current_directory, "tracks", "Hark_the_Herald_Angels_Sing_Pentatonix.mid")

    time.sleep(2)

    midi = MidiPublisher(1, VICTORY_SONG)

    midi.track_readout(VICTORY_SONG)

    time.sleep(3)

    midi.play_track(VICTORY_SONG, 0)

    time.sleep(10)


class MidiPublisher(Node):
    """
    Allows for publication of midi events to audio channel.
    """

    def __init__(self, gap_duration: int = 1, *midi_filepaths: str) -> None:
        """
        Initializes midi publisher with specified gap duration and midi
        files.
        """
        # Runs default node initializations with created name
        super().__init__("midi_publisher")
        # Creates a publisher through which audio information can be sent
        self.publisher_ = self.create_publisher(AudioNoteVector, "cmd_audio", 10)
        # Creates a dictionary of filepaths and track vectors
        self.songs: dict[str, tuple[AudioNoteVector, ...]] = {}
        # Assigns gap duration
        self.GAP_DURATION = gap_duration
        # For each path specified:
        for filepath in midi_filepaths:
            # Adds to track bundle dictionary
            self.add_song(filepath)

    def add_song(self, midi_filepath: str) -> None:
        """
        Adds a midi file to publisher's accessible songs.
        """
        # Readies midi data from path
        midi_data = mido.MidiFile(midi_filepath)
        # print(midi_data, midi_data.ticks_per_beat)
        # Initiates a track list
        song: list[AudioNoteVector] = []
        # For each track in midi data:
        for midi_track in midi_data.tracks:
            # Converts midi track data into custom audio vector
            track = self._build_track(midi_track, midi_data.ticks_per_beat)
            # If there are any notes in the vector:
            if track.notes:
                # Add track vector to song
                song.append(track)
        # If song contains any vectors with notes:
        if song:
            # Adds track list to dictionary of songs
            self.songs[midi_filepath] = tuple(song)
        else:
            print(
                f"WARNING: {midi_filepath} contains no tracks with notes! Was not added to bundles."
            )

    def _build_track(self, midi_track: list, ticks_per_beat: int) -> AudioNoteVector:
        """
        Converts midi track into AudioNoteVector object. Optional flag for
        gap notes.
        """
        # Calculates nanoseconds per tick from default microseconds per beat
        nanoseconds_per_tick = int(500000 / ticks_per_beat * 1e3)
        previous_frequency = 0
        delta_time = 0.0
        # Creates note vector object for a track
        track = AudioNoteVector()
        track.header.stamp = rclpy.time.Time().to_msg()
        # For each message in track:
        for message in midi_track:
            # Adds message time to delta time
            delta_time += message.time
            # If tempo message:
            if message.type == "set_tempo":
                # Calculates nanoseconds per beat from microseconds per beat
                nanoseconds_per_tick = int(message.tempo / ticks_per_beat * 1e3)
            # If note event message:
            if message.type in ("note_on", "note_off"):
                # Defines duration of seperation note
                gap_duration = int(self.GAP_DURATION * (delta_time > self.GAP_DURATION))
                # Addes gap note to vector
                track.notes.append(
                    self.create_note(0, gap_duration * nanoseconds_per_tick)
                )
                # Addes previous note to vector
                track.notes.append(
                    self.create_note(
                        previous_frequency,
                        (delta_time - gap_duration) * nanoseconds_per_tick,
                    )
                )
                # Sets previous frequency to current by converting from midi note
                previous_frequency = int(
                    bool(message.velocity) * 440 * 2 ** ((message.note - 69) / 12)
                )
                # Resets delta time
                delta_time = 0.0

        # print(f"Track notes: {track.notes}")
        return track

    def create_note(self, frequency: int, nanosecond_runtime: int) -> AudioNote:
        """
        Utility function that creates note through AudioNote and Duration
        objects.
        """
        seconds, nanoseconds = divmod(nanosecond_runtime, 1e9)
        runtime = Duration()
        # print(f"seconds {int(seconds)} nanoseconds {int(nanoseconds)}")
        runtime.sec = int(seconds)
        runtime.nanosec = int(nanoseconds)
        note = AudioNote()
        note.frequency = int(frequency)
        # print(f"Frequency: {frequency}")
        note.max_runtime = runtime
        return note

    def play_track(self, midi_filepath: str, track_number: int = 0) -> None:
        """
        Plays midi sequence on robot. Optional track number specification.
        """

        # If filepath not in note vector list:
        if midi_filepath not in self.songs:
            raise ValueError("Sequence does not exist for specified filepath.")
        # Acquires vector bundle from list
        song = self.songs[midi_filepath]
        # If track number does not exist:
        if not (0 <= track_number < len(song)):
            raise ValueError("Track number does not exist for specified filepath.")
        # Publish the vector
        # print(song[track_number])
        self.publisher_.publish(song[track_number])

    def track_readout(self, midi_filepath: str):
        # If filepath not in note vector list:
        if midi_filepath not in self.songs:
            raise ValueError("Sequence does not exist for specified filepath.")

        song = self.songs[midi_filepath]

        for index, track in enumerate(song):
            print(f"Track {index}: {len(track.notes)} notes")


if __name__ == "__main__":
    main()
