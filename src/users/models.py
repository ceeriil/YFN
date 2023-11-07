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

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'following')

class ProfileDetails(models.Model):
    location = models.CharField(max_length=500)
    github = models.URLField(max_length=1000)
    linkedin = models.URLField(max_length=1000)
    website = models.URLField(max_length=500)
    eemail = models.URLField(max_length=100)
    biography = models.CharField(max_length=150)
    about = models.CharField(max_length=200, default='Whats up? I am a developer with 3 years of experience')

    def _str_(self):
        return '%s' %(self.ename)
    class Meta:
        db_table = 'ProfileDetails'
