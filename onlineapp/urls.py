
from django.conf.urls import url,include

from django.views.decorators.csrf import csrf_exempt
from . import views
urlpatterns=[


url(r'^$', views.index, name="homepage"),
url(r'^cards/$', views.Getcards.as_view(), name="get_all_cards"),
url(r'^mycards/$', views.GetMyCards.as_view(), name="get_my_cards"),
url(r'^addcard/$', views.InsertCard.as_view(), name="add_card"),
url(r'^tags/$', views.GetTags.as_view(), name="get_all_tags"),
url(r'^getcard/(?P<pk>\d+)/$', views.Get_card.as_view(), name="get_card_id"),
url(r'^editcard/(?P<pk>\d+)/$',  csrf_exempt(views.Edit_card.as_view()), name="edit_card_id"),
url(r'^delcard/(?P<pk>\d+)/$', views.Delete_card.as_view(), name="delete_card_id"),
url(r'^searchcard/$', views.Search_card.as_view(), name="search_card"),
url(r'^register/$', views.Register, name="register"),


]