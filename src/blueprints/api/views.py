from flask import Blueprint
from flask import jsonify


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/case_details")
def global_case_details():
    pass


@bp.route("/case_details/<string:country>")
def specific_country_case_details():
    pass
