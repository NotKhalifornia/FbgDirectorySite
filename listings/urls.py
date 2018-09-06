from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.listing_search),
    # search_results
    url(r'^listing-search/$', views.listing_search),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
