

from flask import Flask, request
import json
app = Flask(__name__)

messages_dict = {}


@app.route('/logging', methods=['GET', 'POST'])
def facade_s():
    if request.method == 'POST':
        return get_processed_post_request()
    else:
        return get_processed_get_request()


def get_processed_post_request():
    data=request.json
    print('RECEIVED request: ', data)
    messages_dict.update({data["uuid"]: data["msg"]})
    print('SAVED to self.messages_dict')
    return "ok"


def get_processed_get_request(
):
    print('Return messages:', messages_dict.values())
    return ','.join([msg for msg in messages_dict.values()])


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8001, debug=True)

