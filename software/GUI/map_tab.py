import os
import datetime
import random
from threading import Thread
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

from util import map_downloader


class MapTab:
    """
    The Map Tab contains all the information about the rockets current location, and utilises the
    map downloader to grab the rockets location and visualise it as a Google Map.

    Created 13 September 2016
    By Marcel van Workum

    Modified 13 September 2016
    By Marcel van Workum
    """

    DEFAULT_FILE_NAME = "default_map.png"
    FILE_NAME = "rocket_location.png"
    TARGET_LAT_LABEL = "Rocket's Latitude: "
    TARGET_LONG_LABEL = "Rocket's Longitude: "
    CURRENT_LAT_LABEL = "Current Latitude: "
    CURRENT_LONG_LABEL = "Current Longitude: "
    TIME_LABEL = "Time Updated: "
    FETCH_LABEL = "Fetch Rocket Location"
    FETCH_BUTTON_WIDTH = 250

    def __init__(self, window):
        self.window = window
        self.horizontal_layout = QHBoxLayout()

        # initialise the tab's labels
        self.current_lat_label = QLabel(window)
        self.current_long_label = QLabel(window)
        self.target_lat_label = QLabel(window)
        self.target_long_label = QLabel(window)
        self.time_updated_label = QLabel(window)
        self.map_label = QLabel(window)

        # initialise the fetch button
        self.fetch_map_button = QPushButton(self.FETCH_LABEL, window)
        self.initialise_fetch_button()

        # sets the label text and map image
        self.set_label_text()
        self.set_map_image()

        # finally set the tab layout
        self.set_layout(window)

    def initialise_fetch_button(self):
        """
        Initialises the fetch button by setting it's width and connecting the `fetch_map_button_pressed` function
        """
        self.fetch_map_button.setFixedWidth(self.FETCH_BUTTON_WIDTH)
        self.fetch_map_button.clicked.connect(lambda: self.fetch_map_button_pressed())

    def set_label_text(self, target_lat="...", target_long="...", current_lat="...", current_long="...", time="..."):
        """
        Sets the labels of the tab, either taking in values or setting them to the default
        """
        self.current_lat_label.setText(self.CURRENT_LAT_LABEL + current_lat)
        self.current_long_label.setText(self.CURRENT_LONG_LABEL + current_long)
        self.target_lat_label.setText(self.TARGET_LAT_LABEL + target_lat)
        self.target_long_label.setText(self.TARGET_LONG_LABEL + target_long)
        self.time_updated_label.setText(self.TIME_LABEL + time)
        self.fetch_map_button.setText(self.FETCH_LABEL)

    def set_map_image(self):
        """
        Checks to see if the map image exists, and if it does set the map image to that.
         Otherwise set the image to the default map image.
        """
        if os.path.isfile(self.FILE_NAME):
            map_image = QPixmap(self.FILE_NAME)
        else:
            map_image = QPixmap(self.DEFAULT_FILE_NAME)

        self.map_label.setPixmap(map_image)

    def set_layout(self, window):
        """
        Sets the layout of the tab using a horizontal and vertical layout box
        """
        vertical_layout = QVBoxLayout()

        # Add the display & control widgets to the vertical layout
        vertical_layout.addWidget(self.fetch_map_button, alignment=Qt.AlignTop)
        vertical_layout.addWidget(self.current_lat_label, alignment=Qt.AlignTop)
        vertical_layout.addWidget(self.current_long_label, alignment=Qt.AlignTop)
        vertical_layout.addWidget(self.target_lat_label, alignment=Qt.AlignTop)
        vertical_layout.addWidget(self.target_long_label, alignment=Qt.AlignTop)
        vertical_layout.addWidget(self.time_updated_label, alignment=Qt.AlignTop)

        # Add a stretch at the bottom of the vertical box to push widgets to the top
        vertical_layout.addStretch(1)

        # Add the map to the horizontal layout
        self.horizontal_layout.addWidget(self.map_label, alignment=Qt.AlignTop)

        # Add the vertical layout to the horizontal layout
        self.horizontal_layout.addLayout(vertical_layout)

        # Set the alignment to push elements to the left
        self.horizontal_layout.setAlignment(Qt.AlignLeft)

        # finally set the window layout
        window.map_tab.setLayout(self.horizontal_layout)

    def fetch_map_button_pressed(self):
        """
        Helper method to handle the creation of the fetcher thread
        """
        self.fetch_map_button.setText("Fetching Data....")

        try:
            thread = Thread(target=self.fetch_map_image)
            thread.start()
        except Exception:
            print("Failed to create map downloader thread.")

    def fetch_map_image(self):
        """
        Concurrent helper method which uses the MapDownloader class to download the Google Map for the rockets location.
        """
        # TODO actually get values from base station
        current_lat = -41.2880647 + (random.random() / 100)
        current_long = 174.7617035 + (random.random() / 100)

        target_lat = -41.2880647 + (random.random() / 100)
        target_long = 174.7617035 + (random.random() / 100)

        # construct a lat,long string to pass to the map downloader
        current_lat_long = (current_lat, current_long)
        target_lat_long = (target_lat, target_long)

        # Create the MapDownloader and download the map, saving the resulting map image to {FILE_NAME}
        downloader = map_downloader.MapDownloader(target_lat_long, current_lat_long, self.FILE_NAME)
        downloader.download_map()

        # Set the new image to be the tab's map image
        new_map_image = QPixmap(self.FILE_NAME)
        self.map_label.setPixmap(new_map_image)

        # set the tab's labels
        self.set_label_text(target_lat=str(target_lat), target_long=str(target_long),
                            current_lat=str(current_lat), current_long=str(current_long),
                            time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

