from flask import Blueprint, render_template

bp = Blueprint("interface", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/<path:items>")
def item(items):
    nodes = items.split("/")
    return items