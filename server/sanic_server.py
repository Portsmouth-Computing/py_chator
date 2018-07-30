from sanic import Sanic
import sanic.response
import requests
import asyncpg
from server_programs import database_programs
import asyncio
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
    messages = await conn.fetchrow(
        "SELECT * FROM messages"
    )
    print(messages)
    # Get the messages from the database
    return sanic.response.json("[]")


@app.route("/messages/post", methods=["POST"])
async def messages_post_handler(request):
    await database_programs.insert_into_database(conn, request.json["value"])

    messages = await database_programs.fetch_from_database(conn)
    formatted_list = await database_programs.fetch_formattor(messages)

    return sanic.response.json(formatted_list)


async def init_app():
    global conn
    ip = requests.get("http://api.ipify.org")
    print(f"Running on {ip.text}")
    conn = await asyncpg.connect(host="postgres", user="postgres")
    print("Connected to database")
    app.run(host="0.0.0.0", port=80, access_log=True)

if __name__ == "__main__":
    asyncio.run(init_app())
