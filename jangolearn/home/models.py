from django.db import models
from django.utils import timezone
from extensions.utils import change_to_jalali
from django.utils.html import format_html # برای تبدیل فرمت به جنگو استفاده میشه

# my maneger
class ArticleManager(models.Manager):  #  ساخت منیجیر
    def published(self):  # ارتیکل های منتشر شده رو نشون میده
        return self.filter(status='P')




# my models
class Category(models.Model):
    # ForeignKey یعنی چند فرززند و یک پدر داشته باشه
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.SET_NULL, verbose_name='زیر دسته')
    #  توی ادمین هم کتگوری رو فراخوانی میکنم و و براش کلاس میزنم
    title = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="ادرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="موقعیت")

    class Meta:  # ین کلاس برای تنظیمات مدل هست
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = 'دسته بندی'
    # عبارت parent__id باعث میشه اول فقط پدر ها رو بر اساس ایدی شون مرتب کنه و بعد فرزندان رو
        ordering = ['parent__id', 'position'] # می خوام رکورد ها بر اساس پوزیشن و به صورت صعودی مرتب بشه

    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES = (
        ('D', 'پیش نویس'),  #  اگر دف انتخاب بشه دی نشون میده
        ('P', 'منتشر شده'),  #  اگر پابلیش انتخاب بشه پی نشون میده
    )
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="ادرس مقاله")  #  ادرس
##############################################################################
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")  #  برای دسته بندی استفاده میشه
    # عبارت related_name="article" باعث میشه بتونم از طریق category به مقالات دسترسی داشته باشم چون ManyToManyField هستش
##############################################################################
    description = models.TextField(verbose_name="محتوا")  #
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

    def jpublished(self):  # ین تابع تایم رو برای تغییرات به تابع میفرسته تا تاریخ به شمسی بشه
        return change_to_jalali(self.published)

    def category_status(self):  # اگر توی کتگوری گفته شده باشه نمایش داده شود انگاه status = True
        return self.category.filter(status=True)

    objects = ArticleManager()  # منیجر ArticleManeger به قابلیت های منیجر objects اضافه میشه

    def thumbnail_tag(self): # این تابع برای نمایش تصویر هستش
        # از تگ اچ تی ام ال استفاده می کنم و format_html رمت عکی رو به جنگو تبدیل می کنه
        return format_html(f"<img width = 100 height = 75 style = border-radius:6px src='{self.thumbnail.url}'>")
    thumbnail_tag.short_description = "تصویر"
