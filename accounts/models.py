from django.db import models
from services.mixin import DateMixin,SlugMixin
from django.contrib.auth import get_user_model
from services.uploader import Uploader
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from services.generator import CodeGenerator
from django.utils.text import slugify
from services.slugify import slugify
# Create your models here.

User = get_user_model()

class Profile(DateMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = RichTextField(blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    activation_code = models.CharField(max_length=200, blank=True,null=True)
    slug = models.SlugField(unique=True, blank=True,null=True)

    def __str__(self):
        return self.user.email

    def save(self,*args, **kwargs):
        self.slug = CodeGenerator.create_slug_profile(size=10, model_=Profile)

        
        return super().save(*args, **kwargs)
    










class Company(DateMixin,SlugMixin):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=300)
    logo = models.ImageField(upload_to = Uploader.upload_logo_company)
    adress = RichTextField()
    description = RichTextField()
    mobile = PhoneNumberField()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


    def save(self,*args, **kwargs):
        self.code = CodeGenerator.create_slug_shortcode(size=10, model_=Company)

        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
