from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile', validators=[
                              FileExtensionValidator(['png', 'jpg'])])
    category = models.CharField(max_length=255, default='Content Creator')



    def __str__(self):
        return self.user.username
