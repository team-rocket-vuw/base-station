import React from 'react';
import {
  withGoogleMap,
  GoogleMap,
  Marker,
} from "react-google-maps";

const GettingStartedGoogleMap = withGoogleMap(props => (
  <GoogleMap
    ref={props.onMapLoad}
    defaultZoom={16}
    defaultCenter={{ lat: -25.363882, lng: 131.044922 }}
    onClick={props.onMapClick}
  >
  </GoogleMap>
));

var Map = React.createClass({
  render: function() {
    return (
      <div className="react-map">
        <GettingStartedGoogleMap
          containerElement={
            <div style={{ height: `100%`, width: `100%` }} />
          }
          mapElement={
            <div style={{ height: `100%`, width: `100%` }} />
          }
          onMapLoad={_.noop}
          onMapClick={_.noop}
          onMarkerRightClick={this.handleMarkerRightClick}
        />
      </div>
    )
  }
});

export default Map;
