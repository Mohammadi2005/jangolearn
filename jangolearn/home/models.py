from django.db import models
from django.utils import timezone

class Article(models.Model):
    STATUS_CHOICES = (
        ('D', 'Draft'),  #  اگر دف انتخاب بشه دی نشون میده
        ('P', 'Published'),  #  اگر پابلیش انتخاب بشه پی نشون میده
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)  #  ادرس
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnails")
    published = models.DateTimeField(default=timezone.now)  #  زمان انتشار
    created = models.DateTimeField(auto_now_add=True)  #  زمان ساخت
    updated = models.DateTimeField(auto_now=True)  #  زمان ابدیت
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='D')

    def __str__(self):  #  این باعث میشه تایتل بهمون نمایش داده بشه
        return self.title
