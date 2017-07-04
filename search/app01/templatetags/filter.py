from django import template
from django.utils.safestring import mark_safe  # 安全防护 让django 知道我们这个是安全的额

# 为什么这里的makesafe 没有起作用呢?
register = template.Library()  # 创建template 对象


@register.simple_tag
def filter_all(kwargs, k):
    """过滤全部的选项"""
    if k == 'category':  # 分类的全部
        category_id = kwargs['category_id']
        article_type_id = kwargs['article_type_id']
        if category_id == 0:  # 判断如果是分类全部的标签就把这个加上背景
            result = '<a class="active" href="/home/article-0-%s">全部</a>' % article_type_id
        else:
            result = '<a href="/home/article-0-%s">全部</a>' % article_type_id
        return result
    else:  # 文章类型的全部
        category_id = kwargs['category_id']
        article_type_id = kwargs['article_type_id']
        if article_type_id == 0:
            result = '<a class="active" href="/home/article-%s-0">全部</a>' % category_id
        else:
            result = '<a href="/home/article-%s-0">全部</a>' % category_id
        return result


@register.simple_tag
def filer(list, kwargs, k):
    result = None
    if k == 'category':
        for row in list:  # 分类的遍历
            if row[id] == kwargs['category_id']:
                result = ' < a class ="active" href="/home/article-%s-%s" >' \
                         ' %s< / a >' % (row[id], kwargs['article_type_list_id'], row['caption'])
            else:
                result = ' < a href="/home/article-%s-%s" >' \
                         ' %s< / a >' % (row[id], kwargs['article_type_list_id'], row['caption'])
        return result
    else:
        for row in list:  # 类型的遍历
            if row[id] == kwargs['article_type_list_id']:
                result = ' < a class ="active" href="/home/article-%s-%s" >' \
                         ' %s < / a >' % (kwargs['category_id'], row[id], row['caption'])
            else:
                result = ' < a href="/home/article-%s-%s" >' \
                         ' %s < / a >' % (kwargs['category_id'], row[id], row['caption'])
        return result
    pass

#     { %
#     for row in article_type_list %}
#     { % if row.id == kwargs.article_type_id %}
#     < a class ="active" href="/home/article-{{ kwargs.category_id }}-{{ row.id }}" > {{row.caption}} < / a >
#
#
# { % else %}
# < a
# href = "/home/article-{{ kwargs.category_id }}-{{ row.id }}" > {{row.caption}} < / a >
# { % endif %} { % endfor %}


# 分类的全部在前端的实现
# {% if kwargs.category_id == 0 %}
#        <a class="active" href="/home/article-0-{{ kwargs.article_type_id }}">全部</a>
#    {% else %}
#        <a href="/home/article-0-{{ kwargs.article_type_id }}">全部</a>
#    {% endif %}

# 文章类型的全部在前端的实现
# { % if kwargs.article_type_id == 0 %}
#   < aclass ="active" href="/home/article-{{ kwargs.category_id }}-0" > 全部 < / a >
# { % else %}
# < a href = "/home/article-{{ kwargs.category_id }}-0" > 全部 < / a >
# { % endif %}
