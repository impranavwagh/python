from PIL import Image

# open the images
sunglass = Image.open("Sunglass.png")
photo = Image.open("dog.jpg")

# resize the sunglass image
sunglass = sunglass.resize((200, 120))

# paste the sunglass image on the photo
photo.paste(sunglass, (450, 130), sunglass)

# save and show the result
photo.save("result.jpg")
photo.show()
