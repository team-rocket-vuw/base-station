import os
JAR_FILE = "/openrocket.jar"
os.environ['CLASSPATH'] = os.getcwd() + JAR_FILE
from jnius import autoclass

class OpenRocketSimulations:
    ENTRY_CLASS = 'TeamRocket'
    ROCKET_FILE = 'teamrocket.ork'

    def __init__(self):
        TeamRocket = autoclass(self.ENTRY_CLASS)
        self.simulation_file = TeamRocket(self.ROCKET_FILE)

    def run_simulations(self):
        return self.simulation_file.runSimulations()
