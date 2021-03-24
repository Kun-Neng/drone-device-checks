import time

import dronekit

link = {
    'udp': '127.0.0.1:14550',
    'tcp': 'tcp:127.0.0.1:5760',
    'com': 'com5',
    'ttyACM': '/dev/ttyACM0',
    'ttyTHS': '/dev/ttyTHS1'
}


class DroneModel:
    def __init__(self):
        try:
            self.vehicle = dronekit.connect(link['ttyTHS'], wait_ready=True, baud=57600)
        except dronekit.APIException:
            print('Timeout!')

    def getLocation(self, attribute=None):
        if attribute:
            return self.vehicle.location.global_relative_frame.__getattribute__(attribute)
        else:
            return self.vehicle.location.global_relative_frame

    def getAttitude(self, attribute=None):
        if attribute:
            return self.vehicle.attitude.__getattribute__(attribute)
        else:
            return self.vehicle.attitude

    def test_GPS_and_attitude(self):
        lat = float(self.getLocation('lat'))
        lon = float(self.getLocation('lon'))
        alt = float(self.getLocation('alt'))
        roll = float(self.getAttitude('roll'))
        pitch = float(self.getAttitude('pitch'))
        yaw = float(self.getAttitude('yaw'))
        print('lat: %.6f\tlon: %.6f\talt: %.2f' % (lat, lon, alt))
        print('roll: %f\tpitch: %f\tyaw: %f' % (roll, pitch, yaw))

    def close(self):
        self.vehicle.close()


if __name__ == '__main__':
    droneModel = DroneModel()
    try:
        while True:
            droneModel.test_GPS_and_attitude()
            time.sleep(1)
    except KeyboardInterrupt:
        droneModel.close()
