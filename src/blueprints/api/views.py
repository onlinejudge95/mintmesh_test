from bs4 import BeautifulSoup
from flask import Blueprint
from flask import current_app
from flask import jsonify
from lxml import etree
from requests import get


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/case_details")
def global_case_details():
    url = current_app.config.get("DATA_SOURCE_URL")
    try:
        response = get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml")

            node = soup.find("table", {"id": "main_table_countries_today"}).find("tbody")
        return jsonify({"url": url, "data": []}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@bp.route("/case_details/<string:country>")
def specific_country_case_details():
    pass
