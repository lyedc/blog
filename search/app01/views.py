from django.shortcuts import render
from .models import Article, ArticleType, Category


# Create your views here.

def index(request):
    """没有什么用处的"""
    article_type_list = ArticleType.objects.all()
    category_list = Category.objects.all()
    result = Article.objects.all()
    return render(request, 'article.html', locals())



def article(request, *args, **kwargs):
    # print(kwargs)  # {'category_id': '0', 'article_type_id': '0'}
    print("返回的数据是:", kwargs)
    article_type_list = ArticleType.objects.all()
    category_list = Category.objects.all()
    # result = Article.objects.all()# 不返回全部了 返回过滤出来的结果  1
    # result = Article.objects.filter(category_id=1,article_type_id=2)  2
    # 当是0的时候数据库中是没有值的 是不返回数据的  需要给够滤掉
    condition = {}
    for key, value in kwargs.items():
        kwargs[key] = int(value) # 把字符串转换成数字
        if value == "0":  # 注意这里是字符串0 不是数组  一定要转换成字符串来
            pass
        else:
            condition[key] = value  # 把0的时候给过滤掉
    result = Article.objects.filter(**condition) # 3
    print(result)
    return render(request, "article.html", locals())
