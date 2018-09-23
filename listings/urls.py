from django.conf.urls import url
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.listing_search),
    # search_results
    url(r'^listing-search/$', views.listing_search),
    # url(r'^listing/(?P<client_pk>[0-9]{1..5})/$', views.listing),
    # url(r'^listing/<int:client_pk>/$', views.listing)
    
    # path('listing/<str:company_name>/<int:client_pk>/', views.listing),
    # path('listing/<str:company_name>/<int:client_pk>/<str:state>/', views.listing),
    path('listing/<str:company_name>/<int:client_pk>/<str:state>/<int:prod_1_naic>/', views.listing),

]
        # ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
