from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction,connection
from django.db.models import Q, F, Value,Func,ExpressionWrapper,DecimalField
from django.db.models.aggregates import Count,Max,Min,Avg,Sum
from django.db.models.functions import Concat
from store.models import Product,Customer,Order,OrderItem,Collection
from tags.models import TaggedItem

def say_hello(request):
    # products = Product.objects.all()[:5]
    # product = Product.objects.filter(id=0).first()
    # products = Product.objects.filter(unit_price__lt=20)
    # products = Product.objects.filter(unit_price__range=(20,30))
    # products = Product.objects.filter(collection__id__range=(1,3))
    # products = Product.objects.filter(title__icontains='coffee')
    # products = Product.objects.filter(last_update__year=2021)
    # products = Product.objects.filter(unit_price__lt=20, title__icontains = 'coffee') # Logical And connection
    # products = Product.objects.filter(unit_price__lt=20).filter(title__istartswith = 'coffee')  # Logical And connection
    # products = Product.objects.filter(Q(unit_price__lt=20) & Q(title__iendswith = 'ed')) # logical AND connection using Q object
    # products = Product.objects.filter(Q(unit_price__lt=20) | Q(title__iendswith = 'ed'))
    # products = Product.objects.filter(inventory = F('unit_price'))
    # result = Product.objects.aggregate(Count('id'))
    # result = Product.objects.aggregate(count = Count('id'))
    # result = Product.objects.aggregate(count = Count('id'), min_price = Min('unit_price'))
    # result = Product.objects.filter(collection__id = 5).aggregate(count = Count('id'), min_price = Min('unit_price'))
    # new_product = Product.objects.annotate(is_new = Value(True))
    # new_product = Product.objects.annotate(is_new = F('id')+1)
    # full_name = Customer.objects.annotate(
    #     full_name = Func(F('first_name'), Value(' '), F('last_name'),function = 'CONCAT')
    # )
    # full_name = Customer.objects.annotate(
    #     full_name = Concat('first_name', Value(' '), 'last_name')
    # )
    # result = Customer.objects.annotate(
    #     orders_count = Count('order')
    # )
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # results = Product.objects.annotate(
    #     discounted_price = discounted_price
    # )
    # content_type = ContentType.objects.get_for_model(Customer)
    # tags = TaggedItem.objects.select_related('tag').filter(
    #     content_type = content_type,
    #     object_id = 6
    # )
    # tags = TaggedItem.objects.get_tags_for(Customer, 6)
    # Collection.objects.filter(id__gt = 10).delete()

    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    # queryset = Product.objects.raw('SELECT * FROM store_product')

    # try:
    #     cursor = connection.cursor()
    #     cursor.execute('SELECT * FROM store_customer')
    # finally:
    #     cursor.close()

    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * FROM store_customer')


    
    # return render(request, 'hello.html', {'name': 'Mosh','products':list(products)})
    # return render(request, 'hello.html', {'name': 'Mosh','product':product})
    # return render(request, 'hello.html', {'name':'Mosh','results':list(results)})
    # return render(request, 'hello.html', {'name':'Mosh','full_name':full_name})
    # return render(request, 'hello.html', {'name':'Mosh','tags':list(tags)})
    return render(request, 'hello.html',{'name':'mosh'})

