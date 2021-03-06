"""bbb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
#import views from root directory of project
from . import views
from django.conf import settings
app_name = 'bricks'
urlpatterns = [
    path('', views.index,name='index' ),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('property/<property_id>/', views.property, name='property'),
    path('home/', views.home, name='home'),
    path('payment/', views.payment, name='payment'),
    path('purchase/', views.purchase, name='purchase'),
    path('sell/', views.sell, name='sell'),
    path('buy/',views.buy,name='buy'),
    path('gift2/',views.gift2,name='gift2'),
    path('success/',views.success, name="success"),
    path('convert/', views.convert, name='convert'),
    path('actions/', views.actions, name='actions'),
    path('faq/', views.faq, name='faq'),
    path('prospectus/', views.prospectus, name='prospectus'),
    path('registration/',views.registration, name='registration'),
    path('legal/', views.legal, name='about'),
    path('savings/', views.regular_saving_scheme, name='regular_saving_scheme'),
    path('notices/', views.notices, name='notices'),
    path('gift/', views.gift, name='gift'),
    path('settings/', views.settings, name='settings'),
    path('structure/', views.structure, name='structure'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('tandc/', views.terms_and_conditions, name='terms_and_conditions'),
    path('properties/', views.IndexView.as_view(), name='properties'),
    path('payment/', views.payment, name='payment'),
	path('recieving/', views.receiving_bank, name='receiving_bank'),
	path('team/',views.team, name='team'),
	path('logintoo/',views.logintoo, name='logintoo'),
    path('charts/',views.charts,name='charts'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registertoo/', views.registertoo, name='registertoo'),
    path('registerthree/', views.registerthree, name='registerthree'),
    path('kyc/', views.kyc, name='kyc'),
    path('convert/',views.convert, name='convert')


    ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
