from django.shortcuts import render
from .models import product
from .serializers import productserializer,uniqueSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
# import json
# import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@api_view(['GET','POST'])
def apiOverview(request):
    api_urls={
        "product list":'prod_list/',
        "product by id":'prod_detail/',
        "add new product":'prod_create/',
        "product categories":"prod_categories/",
        "product by category":'prod_category/'
            }
    return JsonResponse(api_urls)

def product_list(request):
    pro=product.objects.all()
    serializer=productserializer(pro,many=True)
    res={'type':'Success','message':'Product fetched successfully','data':serializer.data}
    json_data=JSONRenderer().render(res)
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def product_details(request):
    if request.method=='POST':
        id=request.POST.get('id')
        if product.objects.filter(id =id):
            pro=product.objects.get(id= id)
            serializer=productserializer(pro)
            print(serializer.data['image'])
            res={'type':'Success','message':'Product fetched successfully','data':serializer.data}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            res={'type':'failed','message':'product id not found'} 
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def product_create(request):
    if request.method=='POST':

        name=request.POST.get('name')
        image=request.FILES.get('image')
        category=request.POST.get('category')
        description=request.POST.get('description')
        price=request.POST.get('price')
        # print(name,image,category,description,price)
        pythondata={"name":name,"image":image,"category":category,"description":description,"price":price}
        
        # data=request.POST
        # image=request.FILES
        # print(image)
        # json_data=json.dumps(data)
        # # stream = io.BytesIO(json_data)
        # # pythondata=JSONParser().parse(stream)
        # pythondata=json.loads(json_data)
        # print(pythondata)

        serializer=productserializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()
            res={'type':'Success','message':'Product created successfully'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
           json_data=JSONRenderer().render(serializer.errors) 
           return HttpResponse(json_data, content_type='application/json')


def product_categories(request):
    if request.method=='GET':
        fields = ('id','category',)
        pro = product.objects.values('id','category')
        data = uniqueSerializer(pro, many=True, fields = fields).data
        res={'type':'Success','message':'Category fetched successfully','data':data}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def product_category(request):
    if request.method=='POST':
        cate=request.POST.get('category')
        if product.objects.filter(category =cate):
            pro=product.objects.filter(category =cate)
            serializer=productserializer(pro,many=True)
            res={'type':'Success','message':'Product by category fetched successfully','data':serializer.data}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            res={'type':'failed','message':'product category not found'} 
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json') 