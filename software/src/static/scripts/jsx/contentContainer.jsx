import React from 'react';

import Map from './map.jsx';
import SimulationContainer from './simulationContainer.jsx';

var ContentContainer = React.createClass({
  getInitialState: function() {
    return({})
  },

  getStatusContent: function() {
    return(
      <div className="react-content">
        <h2>{this.props.data.status}</h2>

        <h3>Gyro data</h3>
        <ul>
          <li>x: {this.props.data.gyro.x}</li>
          <li>y: {this.props.data.gyro.y}</li>
          <li>z: {this.props.data.gyro.z}</li>
        </ul>

        <h3>Location</h3>
        <ul>
          <li>Target</li>
          <li>lat: {this.props.data.location.target.lat}</li>
          <li>long: {this.props.data.location.target.lng}</li>
        </ul>
      </div>
    );
  },

  getLocationContent: function() {
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
      <div className="react-content">
        <Map markers={this.props.data.markers} onCurrentLocationSet={this.onCurrentLocationSet} />

        <div className="location-data-container">
          <h2>Location Data</h2>

          <div className="current-location">
            <h3>Current</h3>
            <ul className="location-data-list">
              <li>lat: {currentLat}</li>
              <li>long: {currentLng}</li>
            </ul>
          </div>

          <div className="rocket-location">
            <h3>Rocket</h3>
            <ul className="location-data-list">
              <li>lat: {this.props.data.location.target.lat}</li>
              <li>long: {this.props.data.location.target.lng}</li>
            </ul>
          </div>
        </div>
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

  render: function() {
    switch(this.props.selectedSection) {
      case "status":
        return(
          this.getStatusContent()
        );
        break;
      case "location":
        return (
          this.getLocationContent()
        );
        break;
      case "simulations":
        return(
          this.getSimulationContent()
        );
        break;
      default:
        return(
          <div className="react-content">
            <p>Currently selected section: {this.props.selectedSection}</p>
          </div>
        );
        break;
    }
  }
});

export default ContentContainer;
