from django.shortcuts import render, get_object_or_404  # برای مدیریت خطای ادرس اشتباه 404 رو فرامیخونم
from django.http import JsonResponse  #  برای جیسون برگردوندن
from .models import Article, Category # مدل ارتیکل رو ایوپرت می کنم تا به وسیله اون اطلاعات رو از دیتابیس بگیرم و توی ویو نایش بدم

def home(request):

    me = {
        # 'articles': Article.objects.all().filter(request).order_by('published'), فیلتر ه میکنه و مبنای مرتب شدن رو هم میده
        'articles': Article.objects.all(),
        'categories': Category.objects.all().filter(status=True),
    }
    return render(request, 'home.html', me)
#    return HttpResponse("Hello World")

def api(request):
    return JsonResponse({'title':"سلام دنیا" , 'id':11 , 'slug': 'ooo'})

def show(request):
    show = Article.objects.all().order_by('-id')[:2]  #   و دو تای اخر رو نشون میده بر حسب ای دی نزولی نمایش میده
    # Article.created.filter(status='p')
    # فیلتر میکنه
    return render(request, 'show.html', {'show':show})

def detail(request, slug):
    detail = {
        'article':get_object_or_404(Article, slug=slug), # , status='P' ثلا اگر اینو به فیلتر اضافه کنم فقط published ها رو نشون میده
        'categories': Category.objects.all().filter(status=True),
    }
    return render(request, 'detail.html', detail)

def category(request, slug): # این تابع برای category هستش
    context = {
        'category': get_object_or_404(Category, slug=slug) # کتگوری های یک ارتیکل رو میگیره
    }
    return render(request, 'category.html', context)

