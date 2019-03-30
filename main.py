from Quick import QuickSocket, jsonify
from Quick import QuickClient

app = QuickSocket()

@app.router("/welcome")
def welcome(req):
    print(req.data)
    return jsonify({"ok": True})


def friend_request_handler(data):
    # process new friend request notification

def make_request():
    # request or the client side design

    client = QuickClient(host='127.0.0.1', port=2345)

    data = {'username': 'shayan'}
    resp = client.send(route='/register', json=data)
    print(resp.json())

    client.route(route='/notification/friendRequest',
                 handler=friend_request_notification)

    @client.route(route='/notification/newMessage')
    def new_message_handler(data):
        pass

    notif_client = client.blueprint('notification')
    @notif_client.route('/newPost')
    def new_post_handler(data):
        pass

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2345)
