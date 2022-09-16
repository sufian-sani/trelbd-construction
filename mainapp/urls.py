from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('ourmission/', ourmission, name='ourmission'),
    path('service/', service, name='service'),
    path('service-details/<int:id>/', servicedetails, name='service-details'),
    path('ourprojects/', ourproject, name='ourprojects'),
    path('ourprojectdetails/<int:id>/', ourprojectdetails, name='ourprojectdetails'),
    path('ourvision/', ourvision, name='ourvision'),
    path('ourreport/', ourreport, name='ourreport'),
    path('gallery/', gallery, name='gallery'),
    path('gallery-details/<int:id>/', gallerydetails, name='gallery-details'),
    path('boardofdirectors/', boardofdirectors, name='boardofdirectors'),
    path('boardofdirectors/<slug>/', boardofdirectorsdetails, name='boardofdirectorsdetails'),
    path('historymilestones/', historymilestones, name='historymilestones'),
    path('historymilestonesdetails/<slug>/', historymilestonesdetails, name='historymilestonesdetails'),
    path('boardmeetingsagm/', boardmeetingsagm, name='boardmeetingsagm'),
    path('boardmeetingsagm/<slug>/', boardmeetingsagmdetails, name='boardmeetingsagmdetails'),
    path('corporategovernance/', corporategovernance, name='corporategovernance'),
    path('reportstatements/', reportstatements, name='reportstatements'),
    path('event/', event, name='event'),
    path('event/<slug>/', eventdetails, name='eventdetails'),
    path('carrer/', carrer, name='carrer'),
    path('carrerdetails/<str:slug>', carrerdetails, name='carrerdetails'),
    path('news/', news, name='news'),
    path('news/newspage_details/<str:slug>', newsdetails, name='newspage_details'),
    path('expertteam/', expertteam, name='expertteam'),
    path('message-from-md/', messagefrommd, name='message-from-md'),
    path('contactus/', contactus, name='contactus'),
    path('expertteamdetails/<str:slug>', expertteamdetails, name='expertteamdetails'),
    path('corporate_social_responsibility/', corporatesocialresponsibility, name='corporatesocialresponsibility'),
    path('advertisements/', advertisements, name='advertisements'),
    path('product_details/<slug>/',product_details, name='product_details'),
    path('notice/',notice,name='notice'),
    path('corporategovernance/<slug>/',corporategovernancedetails,name='corporategovernancedetails'),
    path('company-value/',companyvalue, name='companyvalue'),
    path('about-us/',aboutus, name='aboutus'),
]