import coqui_tts
#pip install TTS

from coqui_tts import Synthesizer
# Load a pre-trained model
model = Synthesizer.from_pretrained("tts_models/coqui_tts/cleanup")
# Synthesize speech
text = "Hello, world!"
audio = model.synthesize(text)
# Save audio to file
with open("output.wav", "wb") as f:
    f.write(audio)