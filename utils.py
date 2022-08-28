import sqlite3


def get_data_netflix(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()

        return result


def search_by_title(title):
    sql = f"""
          SELECT * 
          FROM netflix 
          WHERE type = 'Movie' AND title='{title}'
          ORDER BY release_year DESC
          LIMIT 1 """

    result = get_data_netflix(sql)
    for item in result:
        return dict(item)


def search_by_year(year_from, year_to):
    sql = f"""
          SELECT title, release_year
          FROM netflix
          WHERE type = 'Movie' AND release_year BETWEEN '{year_from}' AND '{year_to}'
          ORDER BY release_year DESC
          LIMIT 100 """

    result = get_data_netflix(sql)

    response = []

    for item in result:
        response.append(dict(item))

    return response


def group_by_rating(rating):
    sql = f"""
          SELECT title, rating, description
          FROM netflix
          WHERE rating='{rating}'
          ORDER BY rating
          LIMIT 300
          """

    result = get_data_netflix(sql)

    rating_list = ["G", "PG", "PG-13", "R", "NC-17"]

    search_result = []

    for item in result:
        item = dict(item)
        if item["rating"] in rating_list:
            search_result.append(item)
        continue

    return search_result


def search_by_listed_in(listed_in):
    sql = f"""
          SELECT title, description, listed_in, release_year
          FROM netflix
          WHERE listed_in LIKE '%{listed_in}%'
          ORDER BY release_year DESC
          LIMIT 10
          """

    result = get_data_netflix(sql)

    list_listed_in = []

    for item in result:
        item = dict(item)
        if listed_in in item["listed_in"]:
            # for_new_item = {}
            # for_new_item.update(item["title"])
            # for_new_item.update(item["description"])
            list_listed_in.append(item)
        continue

    return list_listed_in


def search_cast(cast_1, cast_2):
    sql = f'''
    SELECT "cast"
    FROM netflix
    WHERE "cast" LIKE '%{cast_1}%' AND "cast" LIKE '%{cast_2}%'
    '''

    result = []

    names_dict = {}

    for item in get_data_netflix(sql):
        names = set(dict(item).get('cast').split(",")) - set ([cast_1, cast_2])

        for name in names:
            names_dict[str(name).strip()] = names_dict.get(str(name).strip(), 0) + 1

    for key, value in names_dict.items():
        if value >= 2:
            result.append(key)

    return result


def do_step_6(type_, year, genre):
    sql = f'''
    SELECT title, description, listed_in
    FROM netflix
    WHERE type = "{type_}" AND listed_in LIKE '%{genre}%' AND release_year = "{year}"
    '''

    result = []

    for item in get_data_netflix(sql):
        result.append(dict(item))

    return result


# print(do_step_6("Movie", 2020, "Dramas"))