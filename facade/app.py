import os
import uuid
import requests
from flask import Flask, request, abort


app = Flask(__name__)

messager_service_url = "http://localhost:8002"
logging_service_url = "http://localhost:8001"


@app.route('/', methods=['GET', 'POST'])
def facade_s():
    if request.method == 'POST':
        return get_processed_post_request()
    else:
        return get_processed_get_request()


def get_processed_post_request():
    print('send POST-like request to logging service')
    try:
        post_logging_request = {
            "uuid":str(uuid.uuid4()),
            "msg":request.json.get('msg')
    }
        post_logging_response = requests.post(
            "{msg}/logging-service".format(logging_service_url),
            post_logging_request
        )
        status = post_logging_response.status
        print('received status from logging:', status)
        return app.response_class(status=status)
    except Exception as ex:
        abort(400)


def get_processed_get_request():
    print('send GET-like request to logging service')
    get_logging_response = requests.get(
        "{msg}/".format(msg=logging_service_url)
    )
    print('received from logging:', get_logging_response)
    response_from_messages_service = requests.get(
        "{msg}/messages".format(msg=messager_service_url)
    )
    print('received from messages:', response_from_messages_service.content)
    print(get_logging_response.json())
    return  str(get_logging_response.messages), str(response_from_messages_service.text)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8000, debug=True)
