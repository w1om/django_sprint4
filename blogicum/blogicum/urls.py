# blogicum/blogicum/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/", include("users.urls")),
    path("", include("blog.urls")),
    path("pages/", include("pages.urls")),
]

# Обработчики ошибок 404 и 500
handler404 = "pages.views.page_not_found"
handler500 = "pages.views.server_error"

# Раздача медиафайлов в режиме разработки (для картинок)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
