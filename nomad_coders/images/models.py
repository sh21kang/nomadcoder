from django.db import models
from nomad_coders.users import models as user_models
from taggit.managers import TaggableManager
# Create your models here.


class TimeStampedModel(models.Model):

    create_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    class Meta :
        abstract = True

    @property
    def like_count(self):
        return self.likes.all().count()


class Image(TimeStampedModel) :
    """ Image Model """
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE ,null=True, related_name='images')
    tags =TaggableManager()

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

    @property
    def like_count(self):
        return self.likes.all().count()

    @property
    def comment_count(self):
        return self.comments.all().count()

    class Meta:
        ordering = ['-create_at']

class Comment(TimeStampedModel):
    """ Comment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE ,null=True)
    image =  models.ForeignKey(Image, on_delete=models.CASCADE ,null=True, related_name='comments')

    def __str__(self):
        return self.message

class Like(TimeStampedModel):

    """ Like Model """
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE ,null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE ,null=True ,related_name='likes')

    def __str__(self):
        return 'User: {} Image Caption: {}'.format(self.creator.username, self.image.caption)

    



