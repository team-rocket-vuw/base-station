import React from 'react';
import $ from "jquery";

var ControlsContainer = React.createClass({
  getInitialState: function() {
    return({
      displayStartButton: false,
      displaySkipButton: false,
      displayBeginButton: false
    });
  },

  sendCommand: function(command) {
    if(command == "start") {
      $.ajax({
        url: '/start_command',
        success: function(data) {
          this.setState({
            startCommandResponse: data
          });
        }.bind(this)
      });
    } else if(command == "skip") {
      $.ajax({
        url: '/skip_command',
        success: function(data) {
          this.setState({
            skipCommandResponse: data
          });
        }.bind(this)
      });
    } else if(command == "begin") {
      $.ajax({
        url: '/begin_command',
        success: function(data) {
          this.setState({
            beginCommandResponse: data
          });
        }.bind(this)
      });
    }
  },

  renderStateDisplay: function() {
    var rocketState = this.props.data.responseData.rocket_state

    var rfmStateClass = "loading";
    var rfmStateContent = "";
    switch(rocketState.init_info.RFM) {
      case "True":
        rfmStateClass = "loaded";
        rfmStateContent = "✔";
      break;
      case "False":
        rfmStateClass = "fail";
        rfmStateClass = "✖"
      break;
    }

    var dmStateClass = "loading";
    var dmStateContent = "";
    switch(rocketState.init_info.DM) {
      case "True":
        dmStateClass = "loaded";
        dmStateContent = "✔";
      break;
      case "False":
        dmStateClass = "fail";
        dmStateContent = "✖";
      break;
    }

    var gpsStateClass = "loading";
    var gpsStateContent = "";
    switch(rocketState.gps_info.STATE) {
      case "waiting":
        gpsStateClass = "waiting";
        gpsStateContent = "•";
      break;
      case "skipped":
        gpsStateClass = "fail";
        gpsStateContent = "✖";
      break;
      case "ready":
        gpsStateClass = "loaded";
        gpsStateContent = "✔";
      break;
    }

    return(
      <div className="state-display">
        <h3>Rocket Initialisation Info</h3>
        <div>
          <div className={rfmStateClass}>{rfmStateContent}</div><span className="rfm-state">Radio Module: {rocketState.init_info.RFM}</span>
        </div>
        <div>
          <div className={dmStateClass}>{dmStateContent}</div><span>Data Module: {rocketState.init_info.DM}</span>
        </div>

        <h3>GPS State</h3>
        <div className={gpsStateClass} /><span>Status: {rocketState.gps_info.STATE}</span>
        <div>Visible Satellites: {parseInt(rocketState.gps_info.VIS)}</div>
      </div>
    );
  },

  renderButtons: function() {
    var buttons = [];

    if (this.state.displaySkipButton) {
      buttons.push(<button className="control-button" onClick={() => this.sendCommand("start")}>Send Start Command</button>);
    }
    if (this.state.displaySkipButton) {
      buttons.push(<button className="control-button" onClick={() => this.sendCommand("skip")}>Send Skip Command</button>);
    }
    if (this.state.displaySkipButton) {
      buttons.push(<button className="control-button" onClick={() => this.sendCommand("begin")}>Send Begin Command</button>);
    }

    return buttons;
  },

  render: function() {
    return(
      <div className="controls-container">
        {this.renderStateDisplay()}
        {this.renderButtons()}
      </div>
    );
  }
});

export default ControlsContainer
