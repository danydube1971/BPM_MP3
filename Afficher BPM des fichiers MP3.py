# Analyse le BPM des fichiers MP3 situés dans le dossier courant de ce script. Enregistre le résultat dans un fichier texte.
# Faut installer "librosa" avec pip3 install librosa et "audioread" pip3 install audioread

import os
import audioread
import librosa

results = []
total_files = len([f for f in os.listdir() if f.endswith(".mp3")])
count = 0

for filename in os.listdir():
    if filename.endswith(".mp3"):
        count += 1
        print(f'Traitement de {count}/{total_files} : {filename}')
        with audioread.audio_open(filename) as audiofile:
            sr = audiofile.samplerate
            y, _ = librosa.load(filename, sr=sr)
            tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
            tempo = int(tempo)
            results.append((tempo, filename))

results.sort()
with open("BPM.txt","w") as f:
    for tempo, filename in results:
        f.write(f'{tempo} - {filename}.\n')

print("Les résultats ont été enregistrés dans 'BPM.txt'.")


