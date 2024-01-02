import re

text = "Halo, nama saya John. John adalah John yang hebat."

# Mengganti hanya 2 kemunculan pertama "John" dengan "Doe"
text_baru = re.sub(r'John', 'Doe', text, count=2)
print(text_baru)
