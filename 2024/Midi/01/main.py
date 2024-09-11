# coding: utf-8

from mido import Message, MidiFile, MidiTrack
from midi2audio import FluidSynth

"""
Midi -> mp3/wav
    1, Download soundfont
        FluidR3_GM.sf2
    2, Install
        $python3 -m pip install mido python-rtmidi midi2audio
        $brew install fluidsynth
"""

SOUND_FONT = "../FluidR3_GM/FluidR3_GM.sf2"
FILE_MIDI  = "result.mid"
FILE_MP3   = "result.mp3"

#==========
# Main

def main():
    print("main!!")

    # Track
    track = MidiTrack()
    track.append(Message("program_change", program=0))
    notes = [
        ("note_on", 64, 0), ("note_off", 64, 240),  # E4
        ("note_on", 67, 0), ("note_off", 67, 240),  # G4
        ("note_on", 69, 0), ("note_off", 69, 240),  # A4
        ("note_on", 72, 0), ("note_off", 72, 240),  # C5
        ("note_on", 67, 0), ("note_off", 67, 240),  # G4
        ("note_on", 69, 0), ("note_off", 69, 240),  # A4
        ("note_on", 64, 0), ("note_off", 64, 240),  # E4
        ("note_on", 62, 0), ("note_off", 62, 240),  # D4
    ]
    for note in notes:
        track.append(Message(note[0], note=note[1], time=note[2]))

    # Midi
    mid = MidiFile()
    mid.tracks.append(track)

    # Save
    mid.save(FILE_MIDI)

    # Midi to mp3
    fs = FluidSynth(SOUND_FONT)
    fs.midi_to_audio(FILE_MIDI, FILE_MP3)


if __name__ == "__main__":
    main()
