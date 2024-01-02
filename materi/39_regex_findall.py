import re

text = "Halo, nama saya John. John adalah John yang hebat."

# Mencari semua kemunculan "John" dalam teks
matches = re.findall(r'John', text)
print("Semua kemunculan:", matches)
