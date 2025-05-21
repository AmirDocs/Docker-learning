import logging 
from flask import Flask, render_template, request, redirect, url_for
import redis
import geoip2.database

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

r = redis.Redis(host='redis', port=6379)

# Path to the GeoLite2 database
GEOIP_DB = 'GeoLite2-Country.mmdb'

@app.route('/')
def index():
    visit_count = r.incr('visit_count')  # Increment visit count in Redis

    # Get visitor's IP address
    ip_address = request.remote_addr
    country_name = ""  # Start with an empty string for the country

    # Get the country from the IP address
    try:
        with geoip2.database.Reader(GEOIP_DB) as reader:
            response = reader.country(ip_address)
            country_name = response.country.name  # Get the country name
    except Exception as e:
        print(f"Error getting country: {e}")

    return render_template('index.html', visit_count=visit_count, country=country_name)

@app.route('/reset')
def reset():
    r.set('visit_count', 0)  # Reset visit count in Redis
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
