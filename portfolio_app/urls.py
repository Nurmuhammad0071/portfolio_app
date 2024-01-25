from django.urls import path
from portfolio_app.views import IndexPage, portfolio

urlpatterns = [
    path('', IndexPage.as_view(),  name="home"),
    path('portfolio/<int:id>', portfolio, name="portfolio")
]

