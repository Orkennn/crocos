from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from geopy.distance import geodesic
from shapely.geometry import Point
import pandas as pd

from .models import Landmark

@require_http_methods(["GET"])
def get_location(request):
    try:
        # Получаем параметры широты и долготы из GET-запроса
        latitude = request.GET.get('latitude', '')
        longitude = request.GET.get('longitude', '')

        # Создаем географическую точку на основе полученных координат
        user_location = Point(float(longitude), float(latitude))

        # Получаем все достопримечательности из базы данных
        landmarks = Landmark.objects.all()

        # Вычисляем расстояние между пользовательским местоположением и каждой достопримечательностью
        distances = []
        for landmark in landmarks:
            landmark_location = Point(landmark.longitude, landmark.latitude)
            distance = geodesic((latitude, longitude), (landmark.latitude, landmark.longitude)).kilometers
            distances.append((landmark, distance))

        # Сортируем достопримечательности по расстоянию до пользователя
        sorted_landmarks = sorted(distances, key=lambda x: x[1])[:10]

        # Собираем данные о ближайших достопримечательностях
        landmarks_data = []
        for landmark, distance in sorted_landmarks:
            landmarks_data.append({
                'name': landmark.name,
                'latitude': landmark.latitude,
                'longitude': landmark.longitude,
                'distance': distance
            })

        # Возвращаем данные о местоположении и ближайших достопримечательностях в формате JSON
        location_data = {
            'latitude': latitude,
            'longitude': longitude,
            'nearest_landmarks': landmarks_data
        }
        return JsonResponse(location_data)

    except Exception as e:
        # Обработка ошибок
        return JsonResponse({'error': str(e)})
