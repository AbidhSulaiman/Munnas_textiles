from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/dp', blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=[('male','Male'),('female','Female')],blank=True, null=True)
    mobile_number1 = models.CharField(max_length=15, blank=True, null=True)
    mobile_number2 = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def avatar(self):
        if self.profile_image:
            avatar = self.profile_image.url
        else:
            avatar = None
        return avatar  
        
    class Meta:
        verbose_name_plural = "Profiles"
        
    def __str__(self):
        return f'{self.first_name} {self.last_name} -- profile'

class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='address')
    type = models.CharField(max_length=50, choices=[('home','Home'),('work','Work')],blank=True, null=True, default='home')
    address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.profile.first_name or "Unknown"} {self.profile.last_name or ""} -- Address'

