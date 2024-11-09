 # resize image
        image = Image.open("logo.png")
        resized_image = image.resize((50, 50)) 
        self.icon_title = PhotoImage(resized_image)