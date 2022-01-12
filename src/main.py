from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root() -> str:
    return 'Salut à tous !'

if __name__ == "__main__":
    application.run()