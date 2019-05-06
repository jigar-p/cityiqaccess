## CityIQ Access
CityIQ Access is a package that allows you to access smart street sensors (to track traffic, pedestrian, temperature, humidity, pressure, and more) installed by Current (powered by GE). Check to make sure if your city has these sensors installed at [https://developer.currentbyge.com/cityiq.](CityIQ)

## Getting Started

### Accessing Environment Data

```python
from cityiq import CityIQ

sandiego = CityIQ()

#E street between 7th and 8th Ave (San Diego Downtown)
bbox = '32.714858:-117.158431,32.714562:-117.157248' 

# JSON formated dictionary
temperature_data = sandiego.get_temperature_metadata_by_bbox(bbox)
```

NOTE: There are more ways to derive temperature other than bbox, check the documentation for more information.

### Accessing Parking Data

```python
from cityiq import CityIQ

sandiego = CityIQ()

# E street between 7th and 8th Ave (San Diego Downtown)
bbox = '32.714858:-117.158431,32.714562:-117.157248' 
start_time = 1557187235000
end_time = 1557190835000

# JSON formated dictionary
open_spots = get_open_parking_spots_by_bbox(start_time, end_time, bbox)

```
NOTE: There are more ways to derive open/occupied parking data other than bbox, check the documentation for more information.




