from django.contrib import admin
from portfolio_app.models import MyInfo, Site, Experience, Skill, Summary, Category, PortfolioImage, Portfolio, Contact, Testimonial

admin.site.register([Site, Experience, Skill, Summary, PortfolioImage, Portfolio, Contact, Testimonial])


# Register your models here.
@admin.register(MyInfo)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['first_name']
    list_filter = ['created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['created_at']
    prepopulated_fields = {"slug": ("name",)}
