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
    conn = await asyncpg.connect(host="postgres")
    messages = await conn.fetchrow(
        "SELECT * FROM messages"
    )
    print(messages)
    # Get the messages from the database
    return sanic.response.text("hi")


@app.route("/messages/post", methods=["POST"])
async def messages_post_handler(request):
    # Add the message to the database
    return sanic.response.text("You have posted")


if __name__ == "__main__":
    ip = requests.get("http://api.ipify.org")
    print(f"Running on {ip.text}")
    app.run(host="0.0.0.0", port=80, access_log=True)
