# api/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category, Order
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer

@api_view(['POST'])
def login(request):
    # Ваш код авторизации пользователя с использованием JWT
    pass

@api_view(['POST'])
def register(request):
    # Ваш код регистрации нового пользователя
    pass

@api_view(['GET'])
def get_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def buy_product(request, product_id):
    # Ваш код создания заказа по определенному продукту для пользователя
    pass

@api_view(['GET'])
def get_user_orders(request, user_id):
    orders = Order.objects.filter(user_id=user_id)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
