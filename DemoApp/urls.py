from django.conf.urls import patterns,include,url
from DemoApp.views import list


urlpatterns = patterns('',
    url(r'^food/$', 'DemoApp.views.list', name='food-list'),
    url(r'^search/$', 'DemoApp.views.search', name='search'),
    # url(r'recipeDetails/$', 'DemoApp.views.recipeDetails', name='recipe'),
    url(r'^recipeDetails/(?P<num>\d+)/$', 'DemoApp.views.recipeDetails', name='food-detail'),

    url(r'^login/', 'DemoApp.views.login1'),
    url(r'^auth/', 'DemoApp.views.auth_and_login'),
    url(r'^signup_in/', 'DemoApp.views.sign_up_in'),
    url(r'^signup/', 'DemoApp.views.sign_up'),
    url(r'^$', 'DemoApp.views.secured'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

)
