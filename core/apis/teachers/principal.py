from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeachersSchema
principal_teachers_resources = Blueprint('principal_teachers_resources', __name__)


@principal_teachers_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    teachers_list = Teacher.get_all_teachers()
    teachers_list_dump = TeachersSchema().dump(teachers_list, many=True)
   

    return APIResponse.respond(data=teachers_list_dump)