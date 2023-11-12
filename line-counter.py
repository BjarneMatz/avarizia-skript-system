import os

path = os.getcwd()

lines = 0
file_count = 0

# Ordner durchsuchen
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".sk"):
            file_count += 1
            # Datei öffnen
            with open(os.path.join(root, file), "r") as f:
                # Zeilen zählen
                for line in f:
                    lines += 1

print(f"Dateien: {file_count} - Zeilen: {lines}")