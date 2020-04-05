from django.conf.urls import url, include
from rtb import views
from rtb.views import UserRegistrationView

app_name = 'rtb'

urlpatterns = [

# Boba
	url(r'^$', views.index, name='index'),
	url(r'^boba/$', views.boba, name='boba'),
	url(r'^boba/(?P<boba_slug>[\w\-]+)/$', views.boba, name='boba'),
	url(r'^boba/(?P<boba_slug>[\w\-]+)/reviews$', views.boba_reviews, name='boba_reviews'),
	url(r'^boba/(?P<boba_slug>[\w\-]+)/add_review$', views.add_boba_review, name='boba_add_review'),

# Cafes
	url(r'^cafes/$', views.cafes, name='cafes'),
	url(r'^cafes/(?P<cafe_slug>[\w\-]+)/$', views.cafes, name='cafes'),
	url(r'^cafes/(?P<cafe_slug>[\w\-]+)/boba/$', views.cafes_boba, name='cafes_stocks'),

# Generic site URLs
	url(r'^search/(?P<query_string>[\w|\W]+)/$', views.search, name='search'),
	url(r'^sitemap/$', views.sitemap, name='sitemap'),
	url(r'^about/$', views.about, name='about'),
	url(r'^privacy/$', views.privacy, name='privacy'),

# Accounts
	url(r'accounts/register/$', UserRegistrationView.as_view(), name='registration_register'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^accounts/reviews/$', views.user_reviews, name='reviews'),
	url(r'^accounts/details/$', views.user_details, name='user_details'),
	
]