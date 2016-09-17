import pyqrcode
import png


class QRCodeGenerator:
    GOOGLE_MAP_ROOT = "http://maps.google.com/maps?q=loc:"

    def __init__(self, current_location, target_location, file_name):
        self.current_location = current_location
        self.target_location = target_location
        self.file_name = file_name

    def generate_image(self):
        qr = pyqrcode.create(self.GOOGLE_MAP_ROOT + self.parse_location(self.target_location))
        qr.png(self.file_name, scale=5)

    def parse_location(self, location_tuple):
        return str(location_tuple[0]) + "," + str(location_tuple[1])
