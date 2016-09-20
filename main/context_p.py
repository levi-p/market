from main.models import Product,Category,Comment


def conte(request):
    cat=Category.objects.all()
    


    c=Product.objects.filter(seller=request.user.id)
    d=Comment.objects.all()
    

    comment_list=[x for x in d if str(request.user.id) in x.products.participants if str(request.user) not in x.read]
    

    return {'cat':cat,'c':c,'d':d,'comment_list':comment_list,}
