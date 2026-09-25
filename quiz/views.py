import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render


def game(request):
    json_file = Path(settings.BASE_DIR) / "quiz_flag.json"

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    flags = []

    for item in data:
        flag = {
            "id": item["pk"],
            "country_name": item["fields"]["country_name"],
            "capital_name": item["fields"]["capital_name"],
            "continent": item["fields"]["continent"],
            "url_flag": item["fields"]["url_flag"],
        }

        flags.append(flag)

    return render(request, "quiz/game.html", {
        "flags": flags
    })