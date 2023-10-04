from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test(request):
  if request.method == 'POST':
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    address = request.POST['address']
    place = request.POST['place']
    
    print(first_name, last_name, address, place)
    return HttpResponse('hai')
  

simple_detail=[
    {
        "id" : "1",
        "name":"Akshaya",
        "image":"fdghj.jpg"
    },

    {
        "id" : "2",
        'name': 'John Doe',
        'image': 'john.jpg',
    },
    {
         "id": "3",
         'name': 'Jane Smith',
        'image': 'jane.jpg',
    }

]

advanced_detail = [
    {
        'id':1,
        'f_name': 'akshaya',
        'l_name': 'p',
        'contact': '123-456-7890',
        'email': 'akshaya@example.com',
        'image': 'fgh.jpg',
    },
    {
        'id':2,
        'f_name': 'John',
        'l_name': 'Doe',
        'contact': '123-456-7890',
        'email': 'john.doe@example.com',
        'image': 'john.jpg',
    },
    {
        'id':3,
        'f_name': 'Jane',
        'l_name': 'Smith',
        'contact': '987-654-3210',
        'email': 'jane.smith@example.com',
        'image': 'jane.jpg',
    }
    ]

@csrf_exempt
def employee(request):
    return JsonResponse(simple_detail, safe=False)

@csrf_exempt
def employeedetails(request, id):
    employee = None
    for item in advanced_detail:
        if item['id'] == id:
            employee = item
            break
        
    if employee:
        return JsonResponse(employee)
    else:
        return HttpResponse('not found')
    
