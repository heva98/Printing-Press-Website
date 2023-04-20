from django.views.generic import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class GalleryPageView(TemplateView):
    template_name = 'gallery.html'

class DigitalprintingPageView(TemplateView):
    template_name = 'digitalprinting.html'

class OffsetprintingPageView(TemplateView):
    template_name = 'offsetprinting.html'

class ContactPageView(TemplateView):
    template_name = 'contact-us.html'

class OfficesuppliesPageView(TemplateView):
    template_name = 'officesupplies.html'

class PromotionalmaterialsPageView(TemplateView):
    template_name = 'promotionalmaterials.html'
