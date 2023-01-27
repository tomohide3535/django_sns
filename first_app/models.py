from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit

    
class Stasion(models.Model):
    first_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name
    
class Foodshop(models.Model):
    shop_name = models.CharField(max_length=30)
    sta_name = models.CharField(default=999, max_length=100, null=True, verbose_name='駅名')
    photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
    post_photo = ImageSpecField(source='photo',processors=[ResizeToFit(1080, 1080)],format='JPEG',options={'quality':60})
    
    def __str__(self):
        return self.shop_name

class Post(models.Model):
	author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
	text = models.TextField(verbose_name='本文')
	station = models.CharField(max_length=30)
	photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
	post_photo = ImageSpecField(source='photo',processors=[ResizeToFit(1080, 1080)],format='JPEG',options={'quality':60})
	created_at = models.DateTimeField(auto_now_add=True, blank=True)


	def get_like(self):
		likes = Like.objects.filter(post=self)
		return [like.user for like in likes]


class Like(models.Model):
	user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('user', 'post')