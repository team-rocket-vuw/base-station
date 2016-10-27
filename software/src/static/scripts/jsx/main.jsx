import React from 'react';
import ReactDOM from 'react-dom';
import $ from "jquery";
import _ from "lodash";

import Sidebar from './sidebar.jsx';
import ContentContainer from './contentContainer.jsx';

require('../../styles/scss/style.scss');

var TeamRocket = React.createClass({
  getInitialState: function() {
    return {
      selectedSection: 'status'
    };
  },

  handleSectionChange: function(selectedSection) {
    this.setState({
      selectedSection: selectedSection
    });
  },

  render: function() {
    return (
      <div className="react-container">
        <Sidebar selectedSection={this.state.selectedSection} handleSectionChange={this.handleSectionChange} />
        <ContentContainer data={this.props.data} selectedSection={this.state.selectedSection}/>
      </div>
    );
  }
});

var refreshTime = 100;

setInterval(function() {
  $.get("http://127.0.0.1:5000/data", function (response) {
    var responseData = JSON.parse(response);

    var lat = 0;
    var lng = 0;

    if(responseData.rocket_state.gps_info) {
      if(responseData.rocket_state.gps_info.LAT != "Uninitialised") {
        lat = responseData.rocket_state.gps_info.LAT
      }

      if(responseData.rocket_state.gps_info.LNG != "Uninitialised") {
        lng = responseData.rocket_state.gps_info.LNG
      }
    }

    var data = {
      responseData,
      location: {
        target: {
          lat: lat,
          lng: lng
        }
      },
      markers: [
        {
          position: {
            lat: lat,
            lng: lng
          },
          label: "R",
          key: "target"
        }
      ]
    }

    ReactDOM.render(
      <TeamRocket data={data} />,
      document.getElementById('react-hook')
    );
  });
}, refreshTime);
