from yotube_request import YoutubeRequest
from flask import Flask, request, json

app = Flask(__name__)


@app.route('/search', methods=['GET', 'POST'])
def search():
    """
    Точка входа для получения данных из видео
    """

    args = request.args
    url_video = args.get('url_video')
    if url_video is None:
        data_video = {'server_status': 404, 'result': "Not found video..."}
    else:
        data_video = youtube_request.request_data(url_video)

    return json.dumps(data_video, indent=2), 201, {'Content-Type': 'application/json'}


if __name__ == "__main__":
    youtube_request = YoutubeRequest()
    app.run()


