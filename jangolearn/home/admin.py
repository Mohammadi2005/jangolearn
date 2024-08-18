from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created')  #  این اطلاعات رو توی پنل نشون میده
    list_filter = ('status', 'published')  #  بر حسب این دو تا فیلتر میکنه
    search_fields = ('title', 'slug')  #  عبارتی رو که جستجو می کنم رو میره توی title and slug چستجو می کنه
    prepopulated_fields = {'slug': ('title',)}  #  اسلاگ به صورت خودکار بر حسب تایتل ایجاد ممیشه
    ordering = ('status', 'published')  #  مبنا های مرتب سازی رکورد ها رو کشخص می کنه

admin.site.register(Article, ArticleAdmin)
