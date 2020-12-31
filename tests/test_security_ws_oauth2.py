from fastapi import Depends, FastAPI, Security, WebSocket
from fastapi.security import OAuth2, OAuth2PasswordRequestFormStrict
from fastapi.testclient import TestClient
from pydantic import BaseModel
from starlette.routing import websocket_session

app = FastAPI()

reusable_oauth2 = OAuth2(
    flows={
        "password": {
            "tokenUrl": "token",
            "scopes": {"read:users": "Read the users", "write:users": "Create users"},
        }
    }
)


class User(BaseModel):
    username: str


# Here we use string annotations to test them
def get_current_user(oauth_header: str = Security(reusable_oauth2)):
    user = User(username=oauth_header)
    return user


@app.websocket("/talk")
async def read_current_user(
    websocket: WebSocket, current_user: User = Depends(get_current_user)
):
    print(current_user)
    print(websocket.headers)
    await websocket.accept()
    await websocket.send_text(dict(current_user))
    await websocket.close()


client = TestClient(app)


def test_security_oauth2():
    with client.websocket_connect(
        "/talk", headers={"Authorization": "Bearer footokenbar"}
    ) as websocket:
        data = websocket.receive_text()
        assert data == {"username": "Bearer footokenbar"}


def test_security_oauth2_password_other_header():
    with client.websocket_connect(
        "/talk", headers={"Authorization": "Other footokenbar"}
    ) as websocket:
        data = websocket.receive_text()
        assert data == {"username": "Other footokenbar"}


def test_security_oauth2_password_bearer_no_header():
    with client.websocket_connect("/talk") as websocket:
        data = websocket.receive_text()
        assert data == {"username": "Other footokenbar"}
