from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
#  برای اینکه کتگوری رو توی لیست دیس پلی نشون بدم باید فیلد رو به رشته تبدیل کنم چون لیست دیس پلی نمیتونه many to many باشه
    list_display = ('title', 'slug', 'status', 'created', 'category_to_string')  #  این اطلاعات رو توی پنل نشون میده
    list_filter = ('status', 'published')  #  بر حسب این دو تا فیلتر میکنه
    search_fields = ('title', 'slug')  #  عبارتی رو که جستجو می کنم رو میره توی title and slug چستجو می کنه
    prepopulated_fields = {'slug': ('title',)}  #  اسلاگ به صورت خودکار بر حسب تایتل ایجاد ممیشه
    ordering = ('status', 'published')  #  مبنا های مرتب سازی رکورد ها رو کشخص می کنه


    def category_to_string(self, obj):
        # return "category"
        # کتگوری هایی رو نشون میده که منتشر شده باشن
        return ", ".join([category.title for category in obj.category_status()])  #  تمام عناصر لیست رو با یک کاما و یک فضای خالی به هم وصل میکنه
    category_to_string.short_description = 'دسته بندی' #  توی پنل بجای نام پیش فرض از عبارت دسته بندی استفاده میشه

admin.site.register(Article, ArticleAdmin)

class CategoyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'position')  #  این اطلاعات رو توی پنل نشون میده
    list_filter = (['status'])  #  مقدار لیست فیلتر باید لیست باشه یا تاپل
    search_fields = ('title', 'slug')  #  عبارتی رو که جستجو می کنم رو میره توی title and slug چستجو می کنه
    prepopulated_fields = {'slug': ('title',)}  #  اسلاگ به صورت خودکار بر حسب تایتل ایجاد ممیشه

admin.site.register(Category, CategoyAdmin)

