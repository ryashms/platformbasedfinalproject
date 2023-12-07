from django.contrib import admin
from django.urls import path, include
from personal.views import home_screen_view
from django.conf import settings
from django.conf.urls.static import static
from post.views import create_blog_view  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view),
    path('blog/', create_blog_view, name='blog_posts'),  

  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
