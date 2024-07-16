from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)



@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):

    principal_assignments = Assignment.get_submitted_and_graded()
    principal_assignments_dump = AssignmentSchema().dump(principal_assignments, many=True)

    return APIResponse.respond(data=principal_assignments_dump)