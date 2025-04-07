from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path("",views.home,name="home"),
    path("",include("first_app.urls")),
    path("<int:id>/",include("first_app.urls"),name="product_detail"),



    # this should be always at last
    path("__reload__/",include("django_browser_reload.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
