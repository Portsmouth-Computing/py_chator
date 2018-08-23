import requests
import json
import os.path
import logging
log = logging.getLogger(__name__)


async def bootstrap_version_check():
    bootstrap_version = requests.get("https://api.github.com/repos/twbs/bootstrap/releases")
    latest_json = bootstrap_version.json()[0]
    if os.path.isfile("./version.json") is False:
        log.warning("./version.json doesn't exist, creating.")
        with open("./versino.json", "w") as file:
            file.write(str({"version": "0.0"}))
        log.info("./version.json created.")
    if os.path.isfile("../webpages/bootstrap.min.js") is False:
        log.warning("../webpages/bootstrap.min.js doesn't exist, creating.")
        with open("../webpages/bootstrap.min.js", "w+") as file:
            file.write("")
        log.info("../webpages/bootstrap.min.js created.")
    with open("./version.json") as file:
        json_file = json.load(file)
    if latest_json["name"] != json_file["version"]:
        log.info("Updating bootstrap file")
        latest_bootstrap_js = requests.get("https://stackpath.bootstrapcdn.com/bootstrap/{}/js/bootstrap.min.js".format(latest_json["name"][1:]))
        with open("../webpages/bootstrap.min.js", "w") as file:
            file.write(str(latest_bootstrap_js))
        log.info("Updated bootstrap file")
    else:
        log.info("Bootstrap is on latest version")

