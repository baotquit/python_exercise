from django.conf.urls import url
from django.contrib import admin

from library.views import home_view, SiteCreateCategory, SiteCreateBook

urlpatterns = [
    url(r'^$', home_view),
    url(r'^admin/', admin.site.urls),
    url(r'^create-category/', SiteCreateCategory.as_view(), name='create_category'),
    url(r'^create-book/', SiteCreateBook.as_view(), name='create_book'),
]
