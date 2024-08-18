from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse  #  برای جیسون برگردوندن
from .models import Article # مدل ارتیکل رو ایوپرت می کنم تا به وسیله اون اطلاعات رو از دیتابیس بگیرم و توی ویو نایش بدم

def home(request):
    me = {"name":"amir", "age":19, "job":"python"}
    return render(request, 'home.html', context=me)
#    return HttpResponse("Hello World")

def api(request):
    return JsonResponse({'title':"سلام دنیا" , 'id':11 , 'slug': 'ooo'})

def show(request):
    show = Article.objects.all().order_by('-id')[:2]  #   و دو تای اخر رو نشون میده بر حسب ای دی نزولی نمایش میده
    # Article.created.filter(status='p')
    # فیلتر میکنه
    return render(request, 'show.html', {'show':show})

def detail(request, slug):
    detail = Article.objects.get(slug=slug)
    return render(request, 'detail.html', {'detail':detail})
