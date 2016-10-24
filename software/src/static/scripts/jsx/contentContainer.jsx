import React from 'react';

import Map from './map.jsx';

var ContentContainer = React.createClass({
  render: function() {
    switch(this.props.selectedSection) {
      case "status":
        return(
          <div className="react-content">
            <p>Currently selected section: {this.props.selectedSection}</p>
            <h2>{this.props.data.status}</h2>

            <h3>Gyro data</h3>
            <ul>
              <li>x: {this.props.data.gyro.x}</li>
              <li>y: {this.props.data.gyro.y}</li>
              <li>z: {this.props.data.gyro.z}</li>
            </ul>

            <h3>Location</h3>
            <ul>
              <li>Current</li>
              <li>lat: {this.props.data.location.current.lat}</li>
              <li>long: {this.props.data.location.current.long}</li>
            </ul>

            <ul>
              <li>Target</li>
              <li>lat: {this.props.data.location.target.lat}</li>
              <li>long: {this.props.data.location.target.long}</li>
            </ul>
          </div>
        );
      case "location":
        return (
          <div className="react-content">
            <Map markers={this.props.data.markers} />
            <p>Currently selected section: {this.props.selectedSection}</p>
          </div>
        );
      default:
        return(
          <div className="react-content">
            <p>Currently selected section: {this.props.selectedSection}</p>
          </div>
        );
    }
  }
});

export default ContentContainer;
