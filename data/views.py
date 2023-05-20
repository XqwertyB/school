from django.shortcuts import render
# myapp/views.py
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FeedbackSerializer, NewsList, ArtList
from .telegram import send_telegram_message
from .models import News, Art



@api_view(['POST'])
def feedback_view(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        number = serializer.validated_data['number']
        message = serializer.validated_data['message']
        # Отправка сообщения в Telegram
        text = f'Yangi xabar:\n\nIsm: {name}\nNomer: {number}\nXabar: {message}'
        print(text)
        try:
            send_telegram_message(text)
        except Exception as ex:
            return Response({'error': str(ex)})
        return Response({'success': True}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsView(APIView):
    def get(self, request):
        try:
            news = News.objects.all()
            serializer = NewsList(news, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({"errors": str(ex)})


class ArtView(APIView):
    def get(self, request):
        try:
            art = Art.objects.all()
            serializer = ArtList(art, many=True)
            return Response(serializer.data)
        except Exception as ex:
            return Response({"errors": str(ex)})