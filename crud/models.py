from django.db import models
from django.utils.text import slugify

class crudUser(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100, blank=False, unique=True, default='')
    time = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while crudUser.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
