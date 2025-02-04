from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    favorited_by = models.ManyToManyField(User, related_name= 'favourite_products', blank=True)

    def __str__(self):
        return f'{self.name} ({self.color})'
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.address_line1}, {self.city}, {self.country}'
    
class PastOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='past_orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField()
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order of {self.product.name} on {self.order_date}'

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    addresses = models.ManyToManyField(Address, related_name='user_profiles', blank=True)
    favorite_products = models.ManyToManyField(Product, related_name='favorited_by_profiles', blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

