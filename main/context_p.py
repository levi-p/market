from main.models import Product,Category


def conte(request):
    cat=Category.objects.all()

    return {'cat':cat,}
