from django.urls import path
from portfolio_app.views import IndexPage
urlpatterns = [
    path('' ,IndexPage.as_view())
]
