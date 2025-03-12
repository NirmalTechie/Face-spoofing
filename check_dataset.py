import os

data_path = r"C:\Users\nirma\OneDrive\Desktop\PROJECTS\college project\face-detection\Face-spoofing\CelebA_Spoof"

if os.path.exists(data_path):
    print("Dataset loaded successfully!")
else:
    print("Dataset not found. Check your file paths.")
