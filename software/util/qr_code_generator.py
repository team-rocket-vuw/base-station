import pyqrcode
import png


class QRCodeGenerator:
    """
    QRCode Generator service that takes a location and generates a QRCode png image
    with the Google maps url for that location

    Created 17 September 2016
    By Marcel van Workum

    Modified 19 September 2016
    By Marcel van Workum
    """
    GOOGLE_MAP_ROOT = "http://maps.google.com/maps?q=loc:"

    def __init__(self, location, file_name):
        """
        Instantiates the QRCodeGenerator and splits the location into a url friendly string
        """
        self.location = str(location[0] + "," + location[1])
        self.file_name = file_name

    def generate_image(self):
        """
        Create the QRCode and save it to a png image
        """
        qr = pyqrcode.create(self.GOOGLE_MAP_ROOT + self.location)
        qr.png(self.file_name, scale=5)

