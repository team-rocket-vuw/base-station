import React from 'react';

import Map from './map.jsx';
import SimulationContainer from './simulationContainer.jsx';
import WeatherContainer from './weatherContainer.jsx';
import ControlsContainer from './controlsContainer.jsx';

var ContentContainer = React.createClass({
  getInitialState: function() {
    return({})
  },

  getLaunchOpsContent: function() {
    var currentLat;
    var currentLng;

    if (this.state.location) {
      currentLat = this.state.location.current.lat
      currentLng = this.state.location.current.lng
    } else {
      currentLat = "Not set"
      currentLng = "Not set"
    }

    return(
      <div className="launch-ops-container">
        <ControlsContainer data={this.props.data} />
        <div className="launch-data-container">
          <div className="location-data">
            <h3>Rocket</h3>
            <ul className="location-data-list">
              <li>lat: {this.props.data.location.target.lat}</li>
              <li>long: {this.props.data.location.target.lng}</li>
            </ul>
            <h3>Current</h3>
            <ul className="location-data-list">
              <li>lat: {currentLat}</li>
              <li>long: {currentLng}</li>
            </ul>
          </div>
        </div>
      </div>
    );
  },

  getLocationContent: function() {
    return(
      <div className="location-container">
        <Map markers={this.props.data.markers} onCurrentLocationSet={this.onCurrentLocationSet} />
      </div>
    );
  },

  onCurrentLocationSet: function(location) {
    this.setState({
      location: {
        current: {
          lat: location.lat,
          lng: location.lng
        }
      }
    });
  },

  getSimulationContent: function() {
    return(
      <div className="react-content">
        <SimulationContainer onSimulationsComplete={this.onSimulationsComplete} />
      </div>
    );
  },

  onSimulationsComplete: function(data) {
    this.setState({
      simulation_data: {
        data: data
      }
    });
  },

  getWeatherContent: function() {
    return(
      <div className="react-content">
        <WeatherContainer weatherData={this.state.weatherData} location={this.state.location} onWeatherDataSet={this.onWeatherDataSet} />
      </div>
    )
  },

  onWeatherDataSet: function(data) {
    this.setState({
      weatherData: data
    });
  },

  render: function() {
    switch(this.props.selectedSection) {
      case "launchOps":
        return(
          <div className="react-content">
            {this.getLocationContent()}
            {this.getLaunchOpsContent()}
          </div>
        );
        break;
      case "simulations":
        return(
          this.getSimulationContent()
        );
        break;
      case "weather":
        return(
          this.getWeatherContent()
        );
        break;
    }
  }
});

export default ContentContainer;
