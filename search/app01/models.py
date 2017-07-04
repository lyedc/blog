from django.db import models


# Create your models here.

class Category(models.Model):
    """分类表"""
    caption = models.CharField(max_length=16)

    def __str__(self):
        return self.caption


class ArticleType(models.Model):
    """文章类型表"""
    caption = models.CharField(max_length=16)

    def __str__(self):
        return self.caption


class Article(models.Model):
    """具体的内容表"""
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
    # 两个外键
    category = models.ForeignKey(Category)
    article_type = models.ForeignKey(ArticleType)

    def __str__(self):
        return self.title

        # type_choice = (
        #     (1,'Python'),
        #     (2,'OpenStack'),
        #     (3,'Linux'),
        # )
        # article_type_id = models.IntegerField(choices=type_choice)
