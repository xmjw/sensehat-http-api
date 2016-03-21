from flask import Flask
from flask import Response
from sense_hat import SenseHat
from icons import Icons
import json

app = Flask(__name__)
sense = SenseHat()
icons = Icons()

# My sense is upside down for reasons of cable.
sense.set_rotation(180)

@app.route('/temperator', methods=['GET'])
def temperature():
  r = {'temperature': sense.get_temperature()}
  return Response(json.dumps(r), mimetype='application/json')


@app.route('/humidity', methods=['GET'])
def humidity():
  r = {'humidity': sense.get_humidity()}
  return Response(json.dumps(r), mimetype='application/json')

@app.route('/pressure', methods=['GET'])
def humidity():
  r = {'pressure': sense.get_pressure()}
  return Response(json.dumps(r), mimetype='application/json')

@app.route('/emotion' methods=['POST'])
def emotion():
  face = request.form['face']
  fg = request.form['foreground'].split(',')
  bg = [0,0,0]
  if face == 'smile'
    sense.set_pixels(icons.smile(fg,bg))
  elif face == 'neutral'
    sense.set_pixels(icons.neutral(fg,bg))
  elif face == 'wink'
    sense.set_pixels(icons.wink(fg,bg))
  elif face == 'angry'
    sense.set_pixels(icons.angry(fg,bg))
  elif face == 'dot'
    sense.set_pixels(icons.dot(fg,bg))
  return Response('',204) 

