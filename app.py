from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os
import redis
from utils.weather import get_weather_data

load_dotenv()

app = Flask(__name__)
redis_client = redis.from_url(os.getenv('REDIS_URL'))

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=[os.getenv('RATE_LIMIT')]
)


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    # 尝试从缓存获取
    cached_data = redis_client.get(city)
    if cached_data:
        return jsonify({"data": eval(cached_data), "source": "cache"})

    # 调用天气API
    data = get_weather_data(city)
    if 'error' in data:
        return jsonify(data), 500

    # 设置缓存（12小时）
    redis_client.setex(city, 43200, str(data))
    return jsonify({"data": data, "source": "api"})


if __name__ == '__main__':
    app.run(debug=True)