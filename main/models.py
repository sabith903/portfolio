from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon_path = models.TextField(blank=True, help_text="SVG path data")

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='projects')
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    
class About(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='about/')
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):   
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Image(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    
    