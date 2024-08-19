from django.db import models
from django.utils import timezone
from extensions.utils import change_to_jalali


class Article(models.Model):
    STATUS_CHOICES = (
        ('D', 'پیش نویس'),  #  اگر دف انتخاب بشه دی نشون میده
        ('P', 'منتشر شده'),  #  اگر پابلیش انتخاب بشه پی نشون میده
    )
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="ادرس مقاله")  #  ادرس
    description = models.TextField(verbose_name="محتوا")
    thumbnail = models.ImageField(upload_to="thumbnails", verbose_name="تصویر مقاله")
    published = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار مقاله')  #  زمان انتشار
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت مقاله')  #  زمان ساخت
    updated = models.DateTimeField(auto_now=True, verbose_name='زمان ادیت مقاله')  #  زمان ابدیت
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='D', verbose_name="وضعیت")

    class Meta: # ین کلاس برای تنظیمات مدل هست
        verbose_name_plural = 'مقالات' # برای جا هایی که نام مدل رو باید به صورت جمع بنویسه
        verbose_name = 'مقاله' # این دو تا نامی که برای مدل توی ادمین پنل باید بزارم رو تعیین میکنه
    def __str__(self):  #  این باعث میشه تایتل بهمون نمایش داده بشه
        return self.title

    def jpublished(self):  #  ین تابع تایم رو برای تغییرات به تابع میفرسته
        return change_to_jalali(self.published)