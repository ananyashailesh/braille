import braille

# Test text to braille
print("Text to Braille:", braille.textToBraille("hello"))

# Test text to speech
braille.textToSpeech("hello world")

# Test image to text (use one of the images in your images/ folder)
print("Image to Text:", braille.imageToText("images/a.png"))

# Test image to braille
print("Image to Braille:", braille.imageToBraille("images/a.png"))