from django.contrib import admin
from .models import stu_2,Contact,Tag


class Taginlin(admin.TabularInline):
    model = Tag

# 上面的 Contact 是 Tag 的外部键，所以有外部参考的关系。
# 而在默认的页面显示中，将两者分离开来，无法体现出两者的从属关系。我们可以使用内联显示，让 Tag 附加在 Contact 的编辑页面上显示。


class ContactAdmin(admin.ModelAdmin):
    # fields = ('name','age','email')  #在管理页面添加值的时候 隐藏了部分字段 只显示这三个
    #fields和fieldsets好像有冲突 只能使用一个？
    inlines = [Taginlin]

    search_fields = ('name',) #添加搜索栏
    list_display = ('name','email','age') #我们也可以自定义该页面的显示，比如在列表中显示更多的栏目，只需要在 ContactAdmin 中增加 list_display 属性:

    fieldsets = (
        [
            'Main',{
            'fields':('name','email'),
        }],
        [
            'Advance',{
            'classes':('collapse',), #css
            'fields':('age',),
        }]
    )
    #上面的栏目分为了 Main 和 Advance 两部分。classes 说明它所在的部分的 CSS 格式。这里让 Advance 部分隐藏：


admin.site.register(Contact,ContactAdmin)
# admin.site.register([stu_2,Contact,Tag])
admin.site.register([stu_2])  #自定义表单的话 需要把该表单放到上面去注册  如果还在这注册会导致重复注册报错
#用内联显示的话 Tag 也不用注册了  因为 Contact是T ag 的外键 Contact注册时 inlines 会加载Tag（前提是有上面的类和调用）


'''还有很多功能呢 做个标记 回来继续看'''