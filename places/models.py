from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    place_image = models.ImageField(upload_to='place_image/')
    
    def __str__(self) -> str:
        return self.name
    
class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

class PlaceOwner(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return f'{self.place.name} by {self.owner.full_name}'
    
class PlaceComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.TextField()
    stars_given = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    
    def __str__(self) -> str:
        return f'{self.user.username} gave {self.stars_given} to {self.place.name}'