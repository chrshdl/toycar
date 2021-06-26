#! /usr/bin/env python
import rospy
import rospkg
import serial

from sensors.msg import gps


def decode(lat, lng):
  if len(lat) == 0 or len(lng) == 0:
    return float(), float()
  lat = '{:.7f}'.format(float(lat[:2]) + float(lat[2:])*1.0/60.0)
  lng = '{:.7f}'.format(float(lng[:3]) + float(lng[3:])*1.0/60.0)
  return float(lat), float(lng)


def publisher():
  port = rospy.get_param('~port', '/dev/ttyTHS1')
  ser = serial.Serial(port=port, baudrate=9600, timeout=0.5)
  rospy.loginfo('Connected to port ' + port)
  
  pub = rospy.Publisher('gps', gps, queue_size=10)
  rate = rospy.Rate(1)
  position = gps()

  while not rospy.is_shutdown():
    
    line = ser.readline().decode('utf-8', 'ignore')
    
    if line != '':
      data = line.split(',')

      if data[0][3:] == 'GGA':
        time = int(float(data[1]))
        fix = int(data[6])
        satellites = int(data[7])
        lat, lng = decode(data[2], data[4])
    
        position.time = time
        position.latitude = lat
        position.longitude = lng
        position.fix = fix
        position.satellites = satellites

        pub.publish(position)
        rate.sleep()

if __name__ == '__main__':
  rospy.init_node('gps_publisher')
  publisher()
