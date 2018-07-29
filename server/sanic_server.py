from sanic import Sanic
import sanic.response
import requests
print("Imported")

app = Sanic("chator")
print("Setup App")

app.static("/favicon.ico", "./favicon.ico", name="favicon")
app.static("/html", "./webpages/index.html")
app.static("/py-chator.js", "./webpages/py-chator.js")
app.static("/css/index.css", "./webpages/index.css")

@app.route("/")
async def main_handler(request):
    return sanic.response.text("Hi")

"""
@app.route("/html")
async def html_handler(request):
    return sanic.response.html("")
"""

if __name__ == "__main__":
    ip = requests.get("http://api.ipify.org")
    print(f"Running on {ip.text}")
    app.run(host="0.0.0.0", port=80, access_log=True)
