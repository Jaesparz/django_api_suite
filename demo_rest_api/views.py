from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import uuid

# Simulación de base de datos local en memoria
data_list = []

# Añadiendo algunos datos de ejemplo para probar el GET
data_list.append({'id': str(uuid.uuid4()), 'name': 'User01', 'email': 'user01@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User02', 'email': 'user02@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User03', 'email': 'user03@example.com', 'is_active': False}) # Ejemplo de item inactivo

class DemoRestApi(APIView):
     name = "Demo REST API"
    
     def get(self, request):

      # Filtra la lista para incluir solo los elementos donde 'is_active' es True
      active_items = [item for item in data_list if item.get('is_active', True)]
      return Response(active_items, status=status.HTTP_200_OK)

     def post(self, request):
      data = request.data

      # Validación mínima
      if 'name' not in data or 'email' not in data:
         return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

      data['id'] = str(uuid.uuid4())
      data['is_active'] = True
      data_list.append(data)

      return Response({'message': 'Dato guardado exitosamente.', 'data': data}, status=status.HTTP_201_CREATED)

class DemoRestApiItem(APIView):

     def put(self, request, id):

      data = request.data
   


      #ojo josue no olvidar: [ LO QUE QUIERO GUARDAR ] for [ LO QUE RECORRO ]

      item_index = next((index for index, item in enumerate(data_list) if item['id'] == id), None)

      if item_index is None:
            return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND) 

      if 'name' not in data or 'email' not in data:
         return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)  

        

      data['is_active'] = True
      data['id'] = id
      data_list[item_index] = data
      

      return Response({'message': 'Dato actualizado exitosamente.', 'data': data}, status=status.HTTP_200_OK) 

     def patch(self, request, id):
      data = request.data
      

      #ojo josue no olvidar: [ LO QUE QUIERO GUARDAR ] for [ LO QUE RECORRO ]

      item_index = next((index for index, item in enumerate(data_list) if item['id'] == id), None)

      if item_index is None:
            return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND) 

    

      #obtenemos el original para hacerle un update
      original_item = data_list[item_index]

      original_item.update(data)
      

      return Response({'message': 'Dato actualizado parcialmente.', 'data': original_item}, status=status.HTTP_200_OK)

     def delete(self, request, id):
       
       
       item_found = None
       for item in data_list:
            if item['id'] == id:
                item_found = item
                break
       if not item_found:
            return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

       item_found['is_active'] = False

       return Response({'message': 'Elemento eliminado lógicamente.'}, status=status.HTTP_200_OK)
