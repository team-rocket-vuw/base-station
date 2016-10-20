import React from 'react';
import {
  withGoogleMap,
  GoogleMap,
  Marker,
} from "react-google-maps";

const GettingStartedGoogleMap = withGoogleMap(props => (
  <GoogleMap
    ref={props.onMapLoad}
    defaultZoom={13}
    defaultCenter={{ lat: props.markers[0].position.lat, lng:  props.markers[0].position.lng}}
    onClick={props.onMapClick}
  >
    {props.markers.map((marker, index) => (
      <Marker
        {...marker}
        onRightClick={() => props.onMarkerRightClick(index)}
      />
    ))}
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
          onMarkerRightClick={_.noop}
          markers={this.props.markers}
        />
      </div>
    )
  }
});

export default Map;
