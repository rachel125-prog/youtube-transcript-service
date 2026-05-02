from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import random
import requests

app = Flask(__name__)

PROXIES = [
    "http://yjbzrplk:jtn727u3wf3f@31.59.20.176:6754",
    "http://yjbzrplk:jtn727u3wf3f@198.23.239.134:6540",
    "http://yjbzrplk:jtn727u3wf3f@45.38.107.97:6014",
    "http://yjbzrplk:jtn727u3wf3f@107.172.163.27:6543",
    "http://yjbzrplk:jtn727u3wf3f@198.105.121.200:6462",
    "http://yjbzrplk:jtn727u3wf3f@216.10.27.159:6837",
    "http://yjbzrplk:jtn727u3wf3f@142.111.67.146:5611",
    "http://yjbzrplk:jtn727u3wf3f@191.96.254.138:6185",
    "http://yjbzrplk:jtn727u3wf3f@31.58.9.4:6077",
    "http://yjbzrplk:jtn727u3wf3f@23.229.19.94:8689",
]

@app.route('/')
def home():
    return jsonify({'status': 'YouTube Transcript Service is running'})

@app.route('/transcript')
def get_transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({'error': 'video_id required'}), 400
    
    proxy_url = random.choice(PROXIES)
    session = requests.Session()
    session.proxies = {"http": proxy_url, "https": proxy_url}
    
    try:
        ytt_api = YouTubeTranscriptApi(http_client=session)
        transcript = ytt_api.fetch(video_id)
        text = ' '.join([t.text for t in transcript])
        return jsonify({'transcript': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
