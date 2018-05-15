from django.db import models
# rom django.core.urlresolvers import reversef

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=30)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse("pins:details", kwargs={"id": self.id})
    class Meta:
        ordering = ['name']

    def get_image(image_id):
        images = Image.objects.get(id = image_id)
        return images
    @classmethod
    def search_by_category(cls,search_term):
        searched = cls.objects.filter(category__name__icontains = search_term)
        return searched