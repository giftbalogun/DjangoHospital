from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import handler404, handler500, handler400, handler403

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('care.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'care.views.handler404'
handler403 = 'care.views.handler403'
handler400 = 'care.views.handler400'
handler500 = 'care.views.handler500'
