# QuickSocket
A Bi-Directional Communication Protocol to provide routing as well as fast communication between the client and the server, highly influenced by Flask and WebSockets.

### Server Example

```python
from Quick import QuickSocket, jsonify

app = QuickSocket()

@app.router('/index')
def index_handler(req):
    print(req.data)
    return jsonify({'ok': True})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2345, debug=True)
```


### Client Example

```python
from Quick import QuickClient

client = QuickClient(host="127.0.0.1", port=2345)

@client.router('/notification/friendRequest')
def new_message_handler(req):
    # handle friend request notification from the server

def make_call():
    data = {'username': 'Shayan'}
    response = client.send(route='/register', json=data)
    print(response.json())

if __name__ == '__main__':
    make_call()
    run_forever()
```

## Notes
- The protocol is under development and the api is subjected to change in the future.
