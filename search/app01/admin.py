from django.contrib import admin
from .models import Article, ArticleType, Category


# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'article_type')


# admin.site.register(Article, ArticleAdmin)   传统的注册方法

@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
