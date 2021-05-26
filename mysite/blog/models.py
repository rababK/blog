from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=100,blank=False,help_text="Title")
    content = models.TextField (max_length=1000, blank=False, help_text="Content")
    pubDate=models.DateTimeField(auto_now_add=True,auto_created=True)
    signature=models.CharField(max_length=100,blank=False,help_text="Signature")

    def __str__(self):
        return self.title