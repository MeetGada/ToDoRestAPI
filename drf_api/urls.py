from django.contrib import admin
from django.urls import path, include
from api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # using include() to use the urls of the app, api
    path('api/todo/', include(urls)),
]
