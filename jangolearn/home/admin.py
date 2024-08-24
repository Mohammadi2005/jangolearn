from django.contrib import admin
from .models import Article, Category

def make_public(modeladmin, request, queryset): # برای تغییر به حالت منتشر شده
    rows_update = queryset.update(status='P') # تغییری که میخواییم انجام بشه رو باید اینجا اعمال کنیم
    if rows_update == 1:
        werb = "شد"
    else:
        werb = "شدند"
    modeladmin.message_user(request, f"{rows_update} مقاله منتشر {werb}")
# متن مورد نیاز برای اقدام رو توی ادمین پنل اینجا باید بنویسم
make_public.short_description = 'انتشار مقالات انتخاب شده'

def make_private(modeladmin, request, queryset):
    rowd_update = queryset.update(status='D')
    if rowd_update == 1:
        werb = "شد"
    else:
        werb = "شدند"
    modeladmin.message_user(request, f"{rowd_update} مقاله پیش نویس {werb}")
make_private.short_description = 'پیش نویس شدن مقالا انتخاب شده'

class ArticleAdmin(admin.ModelAdmin):
#  برای اینکه کتگوری رو توی لیست دیس پلی نشون بدم باید فیلد رو به رشته تبدیل کنم چون لیست دیس پلی نمیتونه many to many باشه
    list_display = ('title', 'thumbnail_tag', 'slug', 'status', 'created', 'category_to_string')  #  این اطلاعات رو توی پنل نشون میده
    list_filter = ('status', 'published')  #  بر حسب این دو تا فیلتر میکنه
    search_fields = ('title', 'slug')  #  عبارتی رو که جستجو می کنم رو میره توی title and slug چستجو می کنه
    prepopulated_fields = {'slug': ('title',)}  #  اسلاگ به صورت خودکار بر حسب تایتل ایجاد ممیشه
    ordering = ('status', 'published')  #  مبنا های مرتب سازی رکورد ها رو کشخص می کنه
    actions = [make_public, make_private] # اقداماتی که توی ادمین پنل نوشته رو تعیین میکنه


    def category_to_string(self, obj):
        # return "category"
        # کتگوری هایی رو نشون میده که منتشر شده باشن
        return ", ".join([category.title for category in obj.category_status()])  #  تمام عناصر لیست رو با یک کاما و یک فضای خالی به هم وصل میکنه
    category_to_string.short_description = 'دسته بندی' #  توی پنل بجای نام پیش فرض از عبارت دسته بندی استفاده میشه

admin.site.register(Article, ArticleAdmin)

class CategoyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'position', 'parent')  #  این اطلاعات رو توی پنل نشون میده
    list_filter = (['status'])  #  مقدار لیست فیلتر باید لیست باشه یا تاپل
    search_fields = ('title', 'slug')  #  عبارتی رو که جستجو می کنم رو میره توی title and slug چستجو می کنه
    prepopulated_fields = {'slug': ('title',)}  #  اسلاگ به صورت خودکار بر حسب تایتل ایجاد ممیشه

admin.site.register(Category, CategoyAdmin)

