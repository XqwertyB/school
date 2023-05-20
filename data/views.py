from django.shortcuts import render
# myapp/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FeedbackSerializer
from .telegram import send_telegram_message


@api_view(['POST'])
def feedback_view(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        message = serializer.validated_data['message']
        # Отправка сообщения в Telegram
        text = f'Новое сообщение обратной связи:\n\nИмя: {name}\nEmail: {email}\nСообщение: {message}'
        print(text)
        try:
            send_telegram_message(text)
        except Exception as ex:
            return Response({'error': str(ex)})
        return Response({'success': True}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


