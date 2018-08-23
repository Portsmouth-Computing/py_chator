import requests
import json
import os.path


async def bootstrap_version_check():
    bootstrap_version = requests.get("https://api.github.com/repos/twbs/bootstrap/releases")
    latest_json = bootstrap_version.json()[0]
    if os.path.isfile("./test.json") is False:
        with open("./test.json", "w") as file:
            file.write(str({"version": "0.0"}))
    if os.path.isfile("../webpages/bootstrap.min.js") is False:
        with open("../webpages/bootstrap.min.js", "w") as file:
            file.write("")
    with open("./test.json") as file:
        json_file = json.load(file)
    if latest_json["name"] != json_file["version"]:
        latest_bootstrap_js = requests.get("https://stackpath.bootstrapcdn.com/bootstrap/{}/js/bootstrap.min.js".format(latest_json["name"][1:]))
        with open("../webpages/bootstrap.min.js", "w") as file:
            file.write(str(latest_bootstrap_js))
        print("Fetched updated bootstrap")
    else:
        print("bootstrap is on latest version")

