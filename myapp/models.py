from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile



class pictures(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='imagefile', null= True, blank=True)
    def save(self, *args, **kwargs):
        super(pictures, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height >100 or img.width>100:
            output_size = (128,128)
            im=img.resize(output_size)
            im.save(self.image.path)
            

        # if not self.id:
        #     self.image = self.compressImage(self.image)
        # super(pictures, self).save(*args, **kwargs)
    
    # def compressImage(self, image):
    #     imageTempoary = Image.open(image)
    #     outputIoStream = BytesIO()
    #     imageTempoaryResized = imageTempoary.resize((1020, 573))
    #     imageTempoary.save(outputIoStream, format='JPEG', quality=80)
    #     outputIoStream.seek(0)
    #     image = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" %image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    #     return image

