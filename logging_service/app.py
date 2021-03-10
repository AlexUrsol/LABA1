

from flask import Flask
import json
app = Flask(__name__)

messages_dict = {}


@app.route('/', methods=['GET', 'POST'])
def facade_s():
    if request.method == 'POST':
        return get_processed_post_request()
    else:
        return get_processed_get_request()


def get_processed_post_request():
    data=request.data
    print('RECEIVED request: ', request)
    messages_dict.update({data["uuid"]: data["msg"]})
    print('SAVED to self.messages_dict')
    status = post_logging_response.status
    return app.response_class(status=status)


def get_processed_get_request(
):
    print('Return messages:', messages_dict.values())
    return json.dumps([msg for msg in messages_dict.values()])

@app.route('/messages')
def messages():
    return 'Not implemented endpoint.'


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8001, debug=True)

