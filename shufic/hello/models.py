from django.db import models

class Video(models.Model):
    class Meta():
        db_table = "Video_table"

    Video_url = models.URLField()
    Video_name = models.CharField(max_length=200)
    Video_properties = models.TextField()
    Video_date = models.DateField(auto_now_add=True)
    Video_likos = models.IntegerField(default=0)

    def __str__(self):
        return self.Video_name


class Comments(models.Model):
    class Meta():
        db_table = "Comments_table"

    Comments_text = models.TextField()
    Comments_Video = models.ForeignKey(Video, on_delete=models.CASCADE)
    Comments_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Comments_text

# Create your models here.

