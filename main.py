from flask import Flask, render_template, Response
from camera import VideoCamera
from time import sleep

app = Flask(__name__)


def gen(camera):
    while True:
        sleep(0.3)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
