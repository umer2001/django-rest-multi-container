
from django.contrib import admin
from django.urls import include, path
from movies.views import HelloWorld

# urls
urlpatterns = [
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/env/', HelloWorld.as_view()),
    path('admin/', admin.site.urls),
]
