from music21 import stream,clef,meter,note,chord


#####################################################scala random
s0 = stream.Stream()
s0.append(clef.TrebleClef())
s0.append(meter.TimeSignature('4/4'))
s0.append(note.Note("C5"))
s0.append(note.Rest())
s0.append(note.Note("D5"))
s0.append(note.Note("E5"))
s0.append(note.Note("F5"))
s0.append(note.Rest())
s0.append(note.Note("G5"))
s0.append(note.Note("D5"))
s0.append(note.Note("E5"))
s0.append(note.Note("F5"))
s0.append(note.Note("E5"))

#####################################################scala discendente
s1 = stream.Stream()
s1.append(clef.TrebleClef())
s1.append(meter.TimeSignature('4/4'))
s1 = stream.Stream()
s1.append(note.Note("B6"))
s1.append(note.Note("A6"))
s1.append(note.Note("G6"))
s1.append(note.Note("F6"))
s1.append(note.Note("E6"))
s1.append(note.Note("D6"))
s1.append(note.Note("C6"))
s1.append(note.Note("B5"))
s1.append(note.Note("A5"))
s1.append(note.Note("G5"))
s1.append(note.Note("F5"))
s1.append(note.Note("E5"))
s1.append(note.Note("D5"))
s1.append(note.Note("C5"))
s1.append(note.Note("B4"))
s1.append(note.Note("A4"))
s1.append(note.Note("G4"))
s1.append(note.Note("F4"))
s1.append(note.Note("E4"))
s1.append(note.Note("D4"))
s1.append(note.Note("C4"))
s1.append(note.Note("B3"))
s1.append(note.Note("A3"))
s1.append(note.Note("G3"))
s1.append(note.Note("F3"))
s1.append(note.Note("E3"))
s1.append(note.Note("D3"))
s1.append(note.Note("C3"))

# #####################################################scala ascendente
s2 = stream.Stream()
s2.append(clef.TrebleClef())
s2.append(meter.TimeSignature('4/4'))
s2.append(note.Note("C3"))
s2.append(note.Note("D3"))
s2.append(note.Note("E3"))
s2.append(note.Note("F3"))
s2.append(note.Note("G3"))
s2.append(note.Note("A3"))
s2.append(note.Note("B3"))
s2.append(note.Note("C4"))
s2.append(note.Note("D4"))
s2.append(note.Note("E4"))
s2.append(note.Note("F4"))
s2.append(note.Note("G4"))
s2.append(note.Note("A4"))
s2.append(note.Note("B4"))
s2.append(note.Note("C5"))
s2.append(note.Note("D5"))
s2.append(note.Note("E5"))
s2.append(note.Note("F5"))
s2.append(note.Note("G5"))
s2.append(note.Note("A5"))
s2.append(note.Note("B5"))
s2.append(note.Note("C6"))
s2.append(note.Note("D6"))
s2.append(note.Note("E6"))
s2.append(note.Note("F6"))
s2.append(note.Note("G6"))
s2.append(note.Note("A6"))
s2.append(note.Note("B6"))
s2.append(note.Note("C7"))
s2.append(note.Note("D7"))


# #####################################################scala cromatica ascendente
s3 = stream.Stream()
s3.append(clef.TrebleClef())
s3.append(meter.TimeSignature('4/4'))
s3.append(note.Note("C4"))
s3.append(note.Note("C#4"))
s3.append(note.Note("D4"))
s3.append(note.Note("D#4"))
s3.append(note.Note("E4"))
s3.append(note.Note("F4"))
s3.append(note.Note("F#4"))
s3.append(note.Note("G4"))
s3.append(note.Note("G#4"))
s3.append(note.Note("A4"))
s3.append(note.Note("A#4"))
s3.append(note.Note("B4"))
s3.append(note.Rest())
s3.append(note.Note("C5"))
s3.append(note.Note("C#5"))
s3.append(note.Note("D5"))
s3.append(note.Note("D#5"))
s3.append(note.Note("E5"))
s3.append(note.Note("F5"))
s3.append(note.Note("F#5"))
s3.append(note.Note("G5"))
s3.append(note.Note("G#5"))
s3.append(note.Note("A5"))
s3.append(note.Note("A#5"))
s3.append(note.Note("B5"))
s3.append(note.Rest())
s3.append(note.Note("C6"))
s3.append(note.Note("C#6"))
s3.append(note.Note("D6"))
s3.append(note.Note("D#6"))
s3.append(note.Note("E6"))
s3.append(note.Note("F6"))
s3.append(note.Note("F#6"))
s3.append(note.Note("G6"))
s3.append(note.Note("G#6"))
s3.append(note.Note("A6"))
s3.append(note.Note("A#6"))
s3.append(note.Note("B6"))

#####################################################Accordi
s4 = stream.Stream()
s4.append(chord.Chord(["C4","E4","G4"]))
s4.append(chord.Chord(["C4","E4","G4"]))
s4.append(chord.Chord(["C4","E4","G4"]))

s4.append(chord.Chord(["E4","G4","C5"]))
s4.append(chord.Chord(["E4","G4","C5"]))
s4.append(chord.Chord(["E4","G4","C5"]))

s4.append(chord.Chord(["G4","C5","E5"]))
s4.append(chord.Chord(["G4","C5","E5"]))
s4.append(chord.Chord(["G4","C5","E5"]))
s4.append(chord.Chord(["E4","G4","C5"]))
s4.append(chord.Chord(["C4","E4","G4"]))
s3.append(note.Rest())

s4.append(chord.Chord(["E4","C5","G5"]))
s4.append(chord.Chord(["E4","C5","G5"]))
s4.append(chord.Chord([62, 65, 69, 71]))
s4.append(chord.Chord(["E3","C4","G4"]))
s4.append(chord.Chord(["C4","G4","E-5"]))
s4.append(chord.Chord("E-4 G4 B-4"))
s4.append(chord.Chord([60, 65, 70, 71]))
s4.append(chord.Chord(["E3","C4","G4"]))
s4.append(chord.Chord(["E3","C4","G4"]))
s4.append(chord.Chord([60, 65, 70, 75]))
s4.append(chord.Chord(["E3","C4","G4"]))
s4.append(chord.Chord(["C4","G4","E-5"]))
s4.append(chord.Chord("F4 A4 C5"))
s4.append(chord.Chord("E-4 G4 B-4"))
s4.append(chord.Chord([60, 65, 70, 75]))
s4.append(chord.Chord(["E3","C4","G4"]))
s4.append(chord.Chord(["E3","C4","G4"]))
s4.append(chord.Chord(["C4","G4","E-5"]))
s4.append(chord.Chord("F4 A4 C5"))
s4.append(chord.Chord("E-4 G4 B-4"))
s4.append(chord.Chord([60, 65, 70, 75]))
s4.append(chord.Chord(["E3","C4","G4"]))
s4.append(chord.Chord(["C4","G4","E-5"]))
s4.append(chord.Chord("F4 A4 C5"))
s4.append(chord.Chord("E-4 G4 B-4"))
s4.append(chord.Chord([60, 65, 70, 75]))
s4.append(chord.Chord(["E3","C4","G4"]))
s4.append(chord.Chord(["C4","G4","E-5"]))
s4.append(chord.Chord("F4 A4 C5"))
s4.append(chord.Chord("E-4 G4 B-4"))
s4.append(chord.Chord([60, 65, 70, 75]))

