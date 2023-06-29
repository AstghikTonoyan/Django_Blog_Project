from django.urls import path
from .views import home_page, contact_us, blog_detail, about_us
app_name = "blog"
urlpatterns = [
    path('',home_page, name = "home"),
    path('contact-us/',contact_us, name= "contact-us"),
    path('about-us/',about_us, name= "about-us"),
    path('blog-detail/<int:pk>/',blog_detail, name="blog-detail")
]
