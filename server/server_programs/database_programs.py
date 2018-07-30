import asyncpg
host = "postgres"
user = "postgres"

conn = await asyncpg.connect(host=host, user=user)


async def fetch_from_database():
    messages = await conn.fetch(
        "SELECT * FROM messages ORDER BY id DESC LIMIT 50"
    )

    return messages


async def fetch_formattor(messages):
    formatted_list = []
    for message in messages:
        formatted_list.append({"id": message["id"], "message": message["messages"]})

    return formatted_list


async def insert_into_database(message):
    await conn.execute("""
    INSERT INTO messages(message) VALUES($1)""",
                       message)
