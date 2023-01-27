from rest_framework.decorators import api_view
from rest_framework.response import Response
#lasttry
@api_view(['GET'])
def test_view(request):
    dict_ = {
        'text': 'Hello WOrld',
        'int': 11001,
        'float': 9.99,
        'bool': True,
        'empty': None,
        'list': [1, 2, 3],
        'dict': {
            'list': [
                {'int': 1000},
                {'int': 1000},
                {'int': 1000},
                {'int': 1000},

            ]
        }
    }
    return Response(data=dict_)
