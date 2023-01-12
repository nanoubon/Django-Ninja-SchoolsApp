from typing import List,Optional
from ninja import NinjaAPI
from school_app.models import Preson, Position, Student_class
from school_app.schema import PresonInSchema,PresonOutSchema,PositionSchema,Student_classSchema, NotFondSchema

api = NinjaAPI()

@api.get('/test')
def test(request):
    return "the system it ok"

#Get preson
@api.get('/schools',response=list[PresonOutSchema])
def preson(request):
    return Preson.objects.all()

@api.get('/schools/{preson_id}',response={200: PresonOutSchema,404: NotFondSchema})
def track(request, preson_id:int):
    try:
        preson = Preson.objects.get(pk=preson_id)
        return 200, preson
    except Preson.DoesNotExist as e:
        return 404, {'message': 'Preson does not exist'}

#Post preson
@api.post('/schools', response={201: PresonInSchema})
def input_preson(request, preson: PresonInSchema):
    preson = Preson.objects.create(**preson.dict())
    return preson

#Post position
@api.post('/schools/position', response={201: PositionSchema})
def input_position(request, position: PositionSchema):
    position = Position.objects.create(**position.dict())
    return position

#Post student_class
@api.post('/schools/student_class', response={201:Student_classSchema})
def input_Stu_class(request, student_class: Student_classSchema):
    student_classt = Student_class.objects.create(**student_class.dict())
    return student_class

#Put | update preson
@api.put('/schools/{preson_id}', response={200: PresonInSchema, 404: NotFondSchema})
def change_preson(request, preson_id: int, data: PresonInSchema):
    try :
        preson = Preson.objects.get(pk=preson_id)
        for attribute, value in data.dict().items():
            setattr(preson, attribute,value)
        preson.save()
        return 200, preson
    except Preson.DoesNotExist as e:
        return 404, {'message': 'Preson does not exist'}
    
#Delete preson
@api.delete('/schools/{preson_id}', response={200: None, 404: NotFondSchema})
def delete_preson(request, preson_id: int):
    try :
        preson = Preson.objects.get(pk=preson_id)
        preson.delete()
        return 200
    except Preson.DoesNotExist as e:
        return 404, {'message': 'Preson does not exist'}