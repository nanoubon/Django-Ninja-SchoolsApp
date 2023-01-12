from ninja import Schema

class PresonInSchema(Schema):
    fname :str
    lname : str
    position_id : int 
    student_class_id : int 

class PresonOutSchema(Schema):
     id : int
     fname :str
     lname : str
     position_id : int
     student_class_id : int

class PositionSchema(Schema):
     title : str
     
class Student_classSchema(Schema):
     title : str
     
class NotFondSchema(Schema):
    message : str
