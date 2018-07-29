from sanic import Sanic
import sanic.response
import requests
import asyncpg
print("Imported")

app = Sanic("chator")
print("Setup App")

app.static("/favicon.ico", "./favicon.ico", name="favicon")
app.static("/", "./webpages/index.html")
app.static("/py-chator.js", "./webpages/py-chator.js")
app.static("/css/index.css", "./webpages/index.css")

print("Static links setup")


@app.route("/messages/get", methods=["GET"])
async def messages_handler(request):
    conn = await asyncpg.connect(host="postgres", user="postgres")
    messages = await conn.fetchrow(
        "SELECT * FROM messages"
    )
    print(messages)
    # Get the messages from the database
    return sanic.response.json("[]")


@app.route("/messages/post", methods=["POST"])
async def messages_post_handler(request):
    print(request.json)
    print(request.json["value"])
    return sanic.response.text("200")
    conn = await asyncpg.connect(host="postgres", user="postgres")
    await conn.execute("""
    INSERT INTO messages(message) VALUES($1)""", request.json)
    return sanic.response.text("You have posted")


if __name__ == "__main__":
    ip = requests.get("http://api.ipify.org")
    print(f"Running on {ip.text}")
    app.run(host="0.0.0.0", port=80, access_log=True)
