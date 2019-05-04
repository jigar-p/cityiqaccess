# URLs for the city of San Diego
uaa = 'https://auth.aa.cityiq.io'
metadata_api = 'https://sandiego.cityiq.io/api/v2/metadata/assets'
event_service_api = 'https://sandiego.cityiq.io/api/v2/event/assets'
media_service_api = 'https://sandiego.cityiq.io/api/v2/media/ondemand/assets'
websocket_api = 'wss://sandiego.cityiq.io/api/v2/websocket/events'
parking_api = 'https://sandiego.cityiq.io/api/v2/event/locations'
parking_asset_api = 'https://sandiego.cityiq.io/api/v2/event/assets/'

# BBOX (Bounding Box)
sd_bbox = '32.5348:-117.2824,33.1142:-116.9058'
default_bbox = '32.5348:-117.2824,33.1142:-116.9058'  # default bbox is set to San Diego
sddt_bbox = '32.718987:-117.174244,32.707356:-117.154850'

# San Diego Zones
default_zone = 'SD-IE-TRAFFIC'
traffic_zone = 'SD-IE-TRAFFIC'
parking_zone = 'SD-IE-PARKING'
pedestrian_zone = 'SD-IE-PEDESTRIAN'
environmental_zone = 'SD-IE-ENVIRONMENTAL'
video_zone = 'SD-IE-VIDEO'
image_zone = 'SD-IE-IMAGE'

# Others
GET = "GET"
TEMPERATURE = "TEMPERATURE"
PRESSURE = "PRESSURE"
HUMIDITY = "HUMIDITY"
PKIN = "PKIN"  # Parking In
PKOUT = "PKOUT"  # Parking Out
PEDEVT = "PEDEVT"  # Pedestrian Movement
TFEVT = "TFEVT"  # Vehicle Movement
PKZONE = "PARKING_ZONE"
