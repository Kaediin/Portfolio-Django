from django.db import models

# Create your models here.
class Tile(models.Model):

    def __init__(self, project, img, softwares, description, buttons, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.project = project
        self.img = img
        self.softwares = softwares
        self.description = description
        self.buttons = buttons



class ButtonLink(models.Model):

    def __init__(self, imgPath, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.imgPath = imgPath
        self.url = url


