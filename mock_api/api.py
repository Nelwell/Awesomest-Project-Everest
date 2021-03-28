"""
Mimicking the Uber API request & response structure for price estimates endpoint
https://developer.uber.com/docs/riders/references/api/v1.2/estimates-price-get
Endpoint:
GET /v1.2/estimates/price
Query Parameters:
start_latitude	float	Latitude component of start location.
start_longitude	float	Longitude component of start location.
end_latitude	float	Latitude component of end location.
end_longitude	float	Longitude component of end location.
seat_count(optional)	int	The number of seats required for uberPOOL. Default and maximum value is 2.
Example response 
{
  "prices": [
    {
      "localized_display_name": "POOL",
      "distance": 6.17,
      "display_name": "POOL",
      "product_id": "26546650-e557-4a7b-86e7-6a3942445247",
      "high_estimate": 15,
      "low_estimate": 13,
      "duration": 1080,
      "estimate": "$13-14",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "uberX",
      "distance": 6.17,
      "display_name": "uberX",
      "product_id": "a1111c8c-c720-46c3-8534-2fcdd730040d",
      "high_estimate": 17,
      "low_estimate": 13,
      "duration": 1080,
      "estimate": "$13-17",
      "currency_code": "USD"
    },
    {
      "localized_display_name": "uberXL",
      "distance": 6.17,
      "display_name": "uberXL",
      "product_id": "821415d8-3bd5-4e27-9604-194e4359a449",
      "high_estimate": 26,
      "low_estimate": 20,
      "duration": 1080,
      "estimate": "$20-26",
      "currency_code": "USD"
    }
  ]
}
"""

import math 
from flask import Flask 
from flask import request, abort, jsonify
import time
app = Flask(__name__)

@app.route('/v1.2/estimates/price')
def price_estimate():

    try:
        start_lat = float(request.args.get('start_latitude', ''))
        start_lon = float(request.args.get('start_longitude', ''))
        end_lat = float(request.args.get('end_latitude', ''))
        end_lon = float(request.args.get('end_longitude', ''))
    except ValueError:
        abort(401, 'Bad request - latitude and longitude must be numbers')
    try:
        trip_time = time.strptime(request.args.get('time', ''), '%H:%M:%S')
    except ValueError:
        trip_time = time.localtime()

    # TODO verify lat and long values are sensible numbers so longitudes -180 -> +180, latitudes -90 -> +90
    go = True
    go = validate_lat_lon(go, start_lat, start_lon)
    go = validate_lat_lon(go, end_lat, end_lon)

    if go:
      if start_lat and start_lon and end_lat and end_lon:
          # create mock response
          response = mock_estimates(start_lon, start_lat, end_lon, end_lat)
          return jsonify(response)
      else:
          abort(401, 'Bad request - include start and end locations')
    else:
      abort(401, 'Bad request - latitude must be equal to or between -90 and 90, longitudes must be equal to or between -180 and 180')


def validate_lat_lon(go, lat, lon):
  if lat < -90 or lat > 90:
    go = False
  elif lon < -180 or lon > 180:
    go = False
  
  return go


def mock_estimates(start_lat, start_long, end_lat, end_long):
    # about how far apart are the coordinates? 



    lat_diff = abs(start_lat - end_lat)
    long_diff = abs(start_long - end_long)
    # pythagoras! This isn't the actual distance because the world isn't flat and lat-long is not a regular grid.  
    distance_lat_long = math.sqrt( lat_diff**2 + long_diff**2 )

    # one degree differece of latitude is about 70 miles 
    # one degree difference in longitude, varies where you are in the world. Going with 70 to keep things simple or would need to do more math

    distance = round(distance_lat_long * 70, 2)   # in miles, to 2 decimal places 

    # sample prices taken from https://www.uber.com/us/en/price-estimate/
    pool_booking_fee = 2.20
    uberx_booking_fee = 2.20
    uberxl_booking_fee = 2.45
    select_booking_fee = 2.45
    uber_black_booking_fee = 0.00

    pool_price_per_mile = 1.29
    uberx_price_per_mile = 1.60
    uberxl_price_per_mile = 2.47
    select_price_per_mile = 2.81
    uber_black_price_per_mile = 3.81

    pool_minimum_fair = 7.65
    uberx_minimum_fair = 7.20
    uberxl_minimum_fair = 9.45
    select_minimum_fair = 11.45
    uber_black_minimum_fair = 15.00

    time_per_mile = 300   # seems to be seconds in the response, I'm making this up too
    duration = math.floor(distance * time_per_mile)

    low_price, high_price = get_fair_estimates(distance,pool_price_per_mile,pool_booking_fee,pool_minimum_fair)
    pool_price_json = create_json('POOL',distance,'26546650-e557-4a7b-86e7-6a3942445247',high_price,low_price,duration)

    low_price, high_price = get_fair_estimates(distance,uberx_price_per_mile,uberx_booking_fee,uberx_minimum_fair)
    uberx_price_json = create_json('uberX',distance,'a1111c8c-c720-46c3-8534-2fcdd730040d',high_price,low_price,duration)

    low_price, high_price = get_fair_estimates(distance,uberxl_price_per_mile,uberxl_booking_fee,uberxl_minimum_fair)
    uberx_price_json = create_json('uberXL',distance,'821415d8-3bd5-4e27-9604-194e4359a449',high_price,low_price,duration)

    low_price, high_price = get_fair_estimates(distance,select_price_per_mile,select_booking_fee,select_minimum_fair)
    select_price_json = create_json('SELECT',distance,'57c0ff4e-1493-4ef9-a4df-6b961525cf9',high_price,low_price,duration)

    low_price, high_price = get_fair_estimates(distance,uber_black_price_per_mile,uber_black_booking_fee,uber_black_minimum_fair)
    uber_black_price_json = create_json('BLACK',distance,'d4abaae7-f4d6-4152-91cc-77523e8165a4',high_price,low_price,duration)

    return [
        pool_price_json,
        uberx_price_json,
        uberxl_price_json,
        select_price_json,
        uber_black_price_json
    ]

    # suggestion - tweak estimate based on time of day, whatever else you might think Uber might use to adjust pricing


def get_fair_estimates(distance,price_per_mile,booking_fee,minimum_fair):
  low_price = math.floor(distance * pool_price_per_mile * 0.8)   # round down
  high_price = math.ceil(distance * pool_price_per_mile * 1.2)   # round up
  low_price = low_price + booking_fee
  high_price = high_price + booking_fee
  if low_price < minimum_fair:
    low_price = minimum_fair
  if high_price < minimum_fair:
    high_price = minimum_fair

  return low_price, high_price


def create_json(display_name,distance,product_id,high_price,low_price,duration):
  json = {
  "localized_display_name": name,
    "distance": distance,
    "display_name": name,
    "product_id": product_id,
    "high_estimate": high_price,
    "low_estimate": low_price,
    "duration": duration,
    "estimate": f"${low_price}-{high_price}",
    "currency_code": "USD"
  }

  return json
