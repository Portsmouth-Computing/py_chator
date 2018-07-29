from sanic import Sanic
import sanic.response

app = Sanic("chator")

app.static("/favicon.ico", "./favicon.ico", name="favicon")


@app.route("/")
async def main_handler(request):
    return sanic.response.text("Hi")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, access_log=True)
