import requests
import json
import os.path
import logging
log = logging.getLogger(__name__)

VERSION_JSON_LOCATION = "./version.json"
BOOTSTRAP_JS_LOCATION = "./webpages/bootstrap.min.js"


async def bootstrap_version_check():
    bootstrap_version = requests.get("https://api.github.com/repos/twbs/bootstrap/releases")
    latest_json = bootstrap_version.json()[0]
    if os.path.isfile(VERSION_JSON_LOCATION) is False:
        log.warning(f"{VERSION_JSON_LOCATION} doesn't exist, creating.")
        with open(VERSION_JSON_LOCATION, "w") as file:
            json.dump({"version": "0.0"}, file)
        log.info(f"{VERSION_JSON_LOCATION} created.")
    if os.path.isfile(BOOTSTRAP_JS_LOCATION) is False:
        log.warning(f"{BOOTSTRAP_JS_LOCATION} doesn't exist, creating.")
        with open(BOOTSTRAP_JS_LOCATION, "w+") as file:
            json.dump({}, file)
        log.info(f"{BOOTSTRAP_JS_LOCATION} created.")
    with open(VERSION_JSON_LOCATION) as file:
        try:
            json_file = json.load(file)
        except json.decoder.JSONDecodeError as JDJSONDE:
            file.close()
            log.error(JDJSONDE, "Remaking file")
            with open(VERSION_JSON_LOCATION, "w+") as file:
                json.dump({"version": "0.0"}, file)
            json_file = json.load(file)
    if latest_json["name"] != json_file["version"]:
        log.info("Updating bootstrap file")
        log.info("Fetching version '{}' of bootstrap".format(latest_json["name"][1:]))
        latest_bootstrap_js = requests.get("https://stackpath.bootstrapcdn.com/bootstrap/{}/js/bootstrap.min.js".format(latest_json["name"][1:]))
        if latest_bootstrap_js.status_code == 200:
            with open(BOOTSTRAP_JS_LOCATION, "w") as file:
                json.dump(latest_bootstrap_js.json(), file)
            log.info("Updated bootstrap file")
            with open(VERSION_JSON_LOCATION, "w") as file:
                json.dump({"version": latest_json["name"]}, file)
            log.info("Updated version file")
        else:
            log.warning(f"Status code {latest_bootstrap_js.status_code}. Text: {latest_bootstrap_js.text}")
    else:
        log.info("Bootstrap is on latest version")

