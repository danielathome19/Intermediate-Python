import httpx
import asyncio

async def fetch_api(client, endpoint: str) -> dict:
    print(f"--> Requesting {endpoint}...")
    response = await client.get(
        f"https://jsonplaceholder.typicode.com{endpoint}"
    )
    print(f"<-- Received {endpoint}")
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            fetch_api(client, '/users/1'),
            fetch_api(client, '/users/1/posts'),
            fetch_api(client, '/users/1/todos')
        )

    print(f"User: {results[0]['name']}"
          f" | Posts: {len(results[1])}"
          f" | Todos: {len(results[2])}")

if __name__ == "__main__":
    asyncio.run(main())
