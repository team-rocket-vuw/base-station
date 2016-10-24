import React from 'react';
import {
  withGoogleMap,
  GoogleMap,
  Marker,
} from "react-google-maps";

const GoogleMapComponent = withGoogleMap(props => (
  <GoogleMap
    ref={props.onMapLoad}
    defaultZoom={12}
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
  getInitialState: function() {
    return({
      currentMarkerSet: false
    });
  },

  componentDidMount: function() {
    navigator.geolocation.getCurrentPosition((position) => {
      var lat = position.coords.latitude;
      var lng = position.coords.longitude;

      this.setState({
        currentMarkerSet: true,
        currentMarker: {
          'position': {
            lat: lat,
            lng: lng
          },
          'label': 'C',
          'key': 'current',
        }
      });
    })
  },

  render: function() {
    var markers = this.props.markers;

    if (this.state.currentMarkerSet) {
      markers.push(this.state.currentMarker);
    }

    return (
      <div className="react-map">
        <GoogleMapComponent
          containerElement={<div id="containerElement" style={{ height: `100%`, width: `100%` }} />}
          mapElement={<div id="mapElement" style={{ height: `100%`, width: `100%` }} />}
          onMapLoad={_.noop}
          onMapClick={_.noop}
          onMarkerRightClick={_.noop}
          markers={markers}
        />
      </div>
    )
  }
});

export default Map;
