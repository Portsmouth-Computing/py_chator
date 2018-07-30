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


@app.listener('before_server_start')
async def setup_db_connection(app, loop):
    app.pool = await asyncpg.create_pool(host="postgres", user="postgres")
    print("Connected to database")


@app.route("/messages/get", methods=["GET"])
async def messages_handler(request):
    async with request.app.pool.aquire() as conn:
        messages = await database_programs.fetch_from_database(conn)
    formatted_list = await database_programs.fetch_formattor(messages)
    return sanic.response.json(formatted_list)


@app.route("/messages/post", methods=["POST"])
async def messages_post_handler(request):
    async with request.app.pool.aquire() as conn:
        await database_programs.insert_into_database(conn, request.json["value"])

    async with request.app.pool.aquire() as conn:
        messages = await database_programs.fetch_from_database(conn)
    formatted_list = await database_programs.fetch_formattor(messages)

    return sanic.response.json(formatted_list)


if __name__ == "__main__":
    ip = requests.get("http://api.ipify.org")
    print(f"Running on {ip.text}")
    app.run(host="0.0.0.0", port=80, access_log=True)
