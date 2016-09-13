#!/usr/local/bin/python3

import sys
from GUI import status_tab, controls_tab, map_tab
from PyQt5.QtWidgets import *


class BaseStationGUI(QMainWindow):
    """
    Main class for the Graphical aspect of the base station.

    Creates the GUI window and then delegates the creation of the individual GUI tabs.

    Created 13 September 2016
    By Marcel van Workum

    Modified 13 September 2016
    By Marcel van Workum
    """

    APP_NAME = "TR - Base Station"
    APP_WIDTH = 1280
    APP_HEIGHT = 720
    STATUS_BAR_BASE_MSG = "Rocket Status: "

    def __init__(self):
        """
        Initialises the gui and tabs
        """
        super().__init__()

        self.running = False

        self.status_tab = QWidget()
        self.controls_tab = QWidget()
        self.map_tab = QWidget()

        self.init_tabs()
        self.init_gui()

    def init_tabs(self):
        """
        Initialises the individual tabs and delegates their layout to the respective classes
        """
        tab_widget = QTabWidget(self)
        tab_widget.setFixedSize(self.APP_WIDTH, self.APP_HEIGHT)
        tab_widget.addTab(self.status_tab, "Rocket Status")
        tab_widget.addTab(self.controls_tab, "Rocket Controls")
        tab_widget.addTab(self.map_tab, "Rocket Location")
        tab_widget.setCurrentIndex(2)

        # Delegate creation of tabs to helper classes
        status_tab.StatusTab()
        controls_tab.ControlsTab()
        map_tab.MapTab(self)

    def init_gui(self):
        """
        Initialises the GUI window, and then shows it
        """
        self.statusBar().showMessage(self.STATUS_BAR_BASE_MSG + "Initialising")
        self.setFixedSize(self.APP_WIDTH, self.APP_HEIGHT)
        self.center_gui_window()
        self.setWindowTitle(self.APP_NAME)
        self.show()

    def center_gui_window(self):
        """
        Helper method to center the QUI window in the screen
        """
        window_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

    def closeEvent(self, event):
        """
        Helper method to create confirmation dialog when window close event is detected, as well as
        setting the running variable to false thus halting any external threads dependent upon it.
        """
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure you want to quit?",
                                     QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()

            self.running = False
        else:
            event.ignore()


if __name__ == '__main__':
    """
    Main method that begins the execution of the program
    """
    running = True
    app = QApplication(sys.argv)
    gui = BaseStationGUI()

    sys.exit(app.exec())
