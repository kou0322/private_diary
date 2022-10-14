from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name="blog_index"),
    path('bloginquiry/', views.BlogInquiryView.as_view(), name="bloginquiry"),
]