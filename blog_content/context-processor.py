from .models import SocialNetworks, Category


def navbar(request):
    social_networks = SocialNetworks.objects.all().order_by('-id')
    categories = Category.objects.all().order_by('-id')

    return {'social_networks': social_networks, 'categories': categories}
