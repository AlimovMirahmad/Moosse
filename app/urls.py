from django.urls import path
from .views import home_view, blog_view, about_view, contact_view, blog_view_detail, index_view_detail

urlpatterns = [
    path('', home_view),
    path('blog/', blog_view),
    path('blog/<int:id>/', blog_view_detail),
    path('index/<int:id>/', index_view_detail),
    path('about/', about_view),
    path('contact/', contact_view)
]
