from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

from apps.vendor.models import Vendor

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']
    
    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)


    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title
   

 

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        # When image height is greater than its width
        if img.height > img.width:
            # make square by cutting off equal amounts top and bottom
            left = 0
            right = img.width
            top = (img.height - img.width)/2
            bottom = (img.height + img.width)/2
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width >300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

        # When image width is greater than its height
        elif img.width > img.height:
            # make square by cutting off equal amounts left and right
            left = (img.width - img.height)/2
            right = (img.width + img.height)/2
            top = 0
            bottom = img.height
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width >300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=150)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    





     