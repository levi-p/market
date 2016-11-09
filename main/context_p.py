from main.models import Product,Category,Comment
from allPeople.models import Message


def conte(request):
    cat=Category.objects.all()
    


    c=Product.objects.filter(seller=request.user.id)
    d=Comment.objects.all()
    

    comment_list=[x for x in d if str(request.user.id) in x.products.participants if str(request.user) not in x.read]

#find a way to check if either the to or the from doesnt raise an exception

    try:
        message_list = [x for x in str(Message.objects.filter(From__first_name__id=str(request.user.id)))+str(Message.objects.all(To__first_name__id=str(request.user.id))) if str(request.user.id) not in x.readBy ]
    except:
        try:message_list = [x for x in str(Message.objects.filter(From__first_name__id=str(request.user.id))) if str(request.user.id) not in x.readBy ]
        except:message_list = [x for x in str(Message.objects.filter(To__first_name__id=str(request.user.id))) if str(request.user.id) not in x.readBy ]

    return {'cat':cat,'c':c,'d':d,'comment_list':comment_list,'message_list':message_list}
