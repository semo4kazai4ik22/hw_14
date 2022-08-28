import json
from utils import get_data_netflix, search_by_title, search_by_year, group_by_rating, search_by_listed_in, search_cast
from flask import Flask, request, render_template
import sys

sys.setrecursionlimit(2000)

app = Flask(__name__, template_folder="templates")


@app.get("/movie/<title>")
def search_by_title_view(title):
    result = search_by_title(title=title)
    print(result)
    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/movie/<year_from>/<year_to>")
def search_by_year_view(year_from, year_to):
    result = search_by_year(year_from=year_from, year_to=year_to)
    print(result)
    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/rating/children")
def rating_for_children():
    result = group_by_rating("G")
    print(result)
    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/rating/family")
def rating_for_family():
    family_list = ["G", "PG", "PG-13"]
    result = []
    for n in family_list:
        result.append(group_by_rating(n))
    print(result)
    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/rating/adult")
def rating_for_adult():
    adult_list = ["R", "NC-17"]
    result = []
    for n in adult_list:
        result.append(group_by_rating(n))
    print(result)
    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/genre/<genre>")
def search_by_listed_in_view(genre):
    result = search_by_listed_in(genre)
    print(result)
    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


@app.get("/cast/<cast_1>-<cast_2>")
def search_cast_view(cast_1, cast_2):
    result = search_cast(cast_1, cast_2)
    print(result)
    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"
    )


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
