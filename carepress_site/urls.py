from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact-us/', views.ContactPageView.as_view(), name='contact-us'),
    path('gallery/', views.GalleryPageView.as_view(), name='gallery'),
    path('digitalprinting/', views.DigitalprintingPageView.as_view(), name='digitalprinting'),
    path('offsetlprinting/', views.OffsetprintingPageView.as_view(), name='offsetprinting'),
    path('officesupplies/', views.OfficesuppliesPageView.as_view(), name='officesupplies'),
    path('promotionalmaterials/', views.PromotionalmaterialsPageView.as_view(), name='promotionalmaterials'),
]