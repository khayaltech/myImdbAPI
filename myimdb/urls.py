from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('myimdb_watchlist.api.urls')),
    path('auth/', include('authentication.api.urls')),
    # path('api-auth/',include('rest_framework.urls'))
]
