
from django.contrib import admin
from django.urls import include, path
from movies.views import HelloWorld
from movies.views import Connection

# urls
urlpatterns = [
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/env/', HelloWorld.as_view()),
    path('api/v1/db/', Connection.as_view()),
    path('admin/', admin.site.urls),
]
