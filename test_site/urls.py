from django.contrib import admin
from django.urls import include, path
from django.conf import settings


urlpatterns = [
    # Users.
    path("", include("users.urls")),
    # Admin.
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns