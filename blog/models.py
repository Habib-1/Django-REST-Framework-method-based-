from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title=models.CharField(max_length=100)
    blog_content=models.TextField()

    def __str__(self):
        return self.blog_title

class Comments(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    comment=models.TextField()

    def __str__(self):
        return self.comment
