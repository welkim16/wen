from django.contrib import admin
from django.urls import path,include
from srappBrither import urls as hey 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(hey))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
