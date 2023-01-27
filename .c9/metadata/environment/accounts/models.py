{"filter":false,"title":"models.py","tooltip":"/accounts/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":15,"column":42},"action":"insert","lines":["from django.db import models","from django.contrib.auth.models import AbstractUser","from imagekit.models import ImageSpecField, ProcessedImageField","from imagekit.processors import ResizeToFill","","class CustomUser(AbstractUser):","    description = models.TextField(verbose_name='プロフィール', null=True, blank=True)","    photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')","    thumbnail = ImageSpecField(source='photo',","                               processors=[ResizeToFill(256, 256)],","                               format='JPEG',","                               options={'quality': 60})","","","    class Meta:","        verbose_name_plural = 'CustomUser'"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":42},"end":{"row":15,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1674289384149,"hash":"752414212f8a7354067bb7ab7674212a2b408db5"}