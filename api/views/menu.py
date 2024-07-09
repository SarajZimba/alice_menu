from rest_framework.views import APIView
from rest_framework.response import Response
from menu.models import Menu
from api.serializers.menu import MenuSerializerCreate, MenuSerializerList

class MenuListView(APIView):
    def get(self, request, *args, **kwargs):
        menus = Menu.objects.filter(status=True,is_deleted=False)
        try:
            serializer = MenuSerializerList(menus, many=True)
            data = serializer.data
            return Response(data, 200)

        except Exception as e:
            print(e)
            return Response("Something went wrong", 400)
        

class IsPromotional(APIView):
    def get(self, request, *args, **kwargs):
        menus = Menu.objects.filter(status=True, is_deleted=False, is_promotional=True)

        try:
            serializer = MenuSerializerList(menus, many=True)
            data = serializer.data
            return Response(data, 200)

        except Exception as e:
            print(e)
            return Response("Something went wrong", 400)
        
class IsTodaySpecial(APIView):
    def get(self, request, *args, **kwargs):
        menus = Menu.objects.filter(status=True, is_deleted=False, is_todayspecial=True)

        try:
            serializer = MenuSerializerList(menus, many=True)
            data = serializer.data
            return Response(data, 200)

        except Exception as e:
            print(e)
            return Response("Something went wrong", 400)



from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class MenuCreateAPIView(APIView):
    # parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request, *args, **kwargs):
        print(f"This is the {request.data}")
        datas = request.data  # Create a mutable copy of the request data
        try:
            for data in datas:
                # data = data.copy()
                type = data.get('type', None)
                title = data.get('itemName', None)
                description = data.get('description', None)
                price = float(data.get('price', 0.0))
                group = data.get('group', None)
                image = data.get('image', None)  # Get the image from the request data
                image_bytes = data.get('image_bytes', None)
                discount_exempt = data.get('discountExempt', False)


                # Prepare the data for the serializer
                menu_data = {
                    'item_name': title,
                    'description': description,
                    'price': price,
                    'group': group,
                    'thumbnail': image,  # Add the image to the menu data
                    'discount_exempt':discount_exempt,
                    'type':type,
                    'outlet': 'Alice',
                    'image_bytes':image_bytes
                }
                
                print(f"This is the menu data {menu_data} ")

                serializer = MenuSerializerCreate(data=menu_data)
                if serializer.is_valid():
                    menu = serializer.save()
            return Response("menu Created", status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ImageByteView(APIView):
    def get(self, request, *args, **kwargs):
        menu_name = kwargs.get('menu_name')
        menu = Menu.objects.filter(item_name = menu_name).first()
        dict = {}
        if menu:
            dict = {
                'image': menu.image_bytes 
            }
        return Response(dict, 200)
