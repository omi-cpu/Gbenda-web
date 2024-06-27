from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=250)

class BibleStudy(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='series_bs/')
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Replay(models.Model):
    day = models.IntegerField()
    title = models.CharField(max_length=250)
    audio = models.FileField()
    date = models.DateField()
    series = models.ForeignKey(BibleStudy, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
