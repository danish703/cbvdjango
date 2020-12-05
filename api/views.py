from .serializers import BookSerializer
from book.models import  Book
from django.http import JsonResponse
from rest_framework.parsers import  JSONParser
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def booklist(request):
    if request.method=='GET':
        bl = Book.objects.all()
        s = BookSerializer(bl,many=True)
        return JsonResponse(s.data,safe=False)
    else:
        #data = JSONParser().parse(request)
        s = BookSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=201)
        return JsonResponse(s.data,status=400)