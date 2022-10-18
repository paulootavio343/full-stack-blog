from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from utils.images import resize_image


class SocialNetworks(models.Model):
    social_network_name = models.CharField(
        max_length=64, blank=False, unique=True, verbose_name='Name'
    )
    social_network_link = models.CharField(
        max_length=1024, blank=False, unique=True, verbose_name='Link'
    )

    def __str__(self):
        return self.social_network_name

    class Meta:
        verbose_name = 'Social Network'
        verbose_name_plural = 'Social Networks'


class Category(models.Model):
    category_name = models.CharField(
        max_length=64, unique=True, blank=False, verbose_name='Name'
    )
    category_slug = models.SlugField(
        max_length=128, blank=True, unique=True, verbose_name='Slug'
    )

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.category_slug:
            new_slug = slugify(self.category_name)
            self.category_slug = new_slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, verbose_name='User'
    )
    post_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=False, verbose_name='Category'
    )
    title = models.CharField(
        max_length=64, blank=False, verbose_name='Title'
    )
    excerpt = models.CharField(
        max_length=255, blank=False, verbose_name='Excerpt'
    )
    keywords = models.CharField(
        max_length=255, blank=False, verbose_name='Key words'
    )
    slug = models.SlugField(
        max_length=128, blank=True, verbose_name='Slug'
    )
    image = models.ImageField(
        blank=True, upload_to='post_img/%Y/%m/%d', verbose_name='Image'
    )
    image_description = models.TextField(
        blank=True, verbose_name='Image description'
    )
    content = models.TextField(
        blank=False, verbose_name='Content'
    )
    publication_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Publication date'
    )
    update_date = models.DateTimeField(
        auto_now=True, verbose_name='Update date'
    )
    published = models.BooleanField(
        default=False, verbose_name='Published'
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = slugify(self.title)
            self.slug = new_slug

        super().save(*args, **kwargs)

        if self.image:
            resize_image(self.image.name, 1280, 720)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
