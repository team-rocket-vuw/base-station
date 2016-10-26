import os
from jnius import autoclass

JAR_FILE = "/data/openrocket.jar"
os.environ['CLASSPATH'] = os.getcwd() + JAR_FILE

class OpenRocketSimulations:
    ENTRY_CLASS = 'TeamRocket'
    ROCKET_FILE = 'data/teamrocket.ork'

    def __init__(self):
        TeamRocket = autoclass(self.ENTRY_CLASS)
        self.simulation_file = TeamRocket(self.ROCKET_FILE)

    def run_simulations(self):
        return self.simulation_file.runSimulations()
