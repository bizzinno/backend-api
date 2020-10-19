from django.conf.urls import re_path
from django.urls import path
from api import views




urlpatterns = [

    # re_path(r'^authenticate/(?P<backend>[^/]+)/$',views.exchange_token,name='url_authenticate'),
    #url(r'^login/(?P[^/]+)/$',views.exchange_token,name='register_by_access_token')
    re_path(r'^home/',views.index,name='url_index'),

]