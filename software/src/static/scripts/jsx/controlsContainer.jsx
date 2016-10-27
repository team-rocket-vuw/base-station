import React from 'react';
import $ from "jquery";

var ControlsContainer = React.createClass({
  getInitialState: function() {
    return({});
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

  render: function() {
    var rocketState = this.props.data.responseData.rocket_state
    return(
      <div className="controls-container">
        <p>{rocketState.init_info.RFM}</p>
        <button className="control-button" onClick={() => this.sendCommand("start")}>Send Start Command</button>
        <button className="control-button" onClick={() => this.sendCommand("skip")}>Send Skip Command</button>
        <button className="control-button" onClick={() => this.sendCommand("begin")}>Send Begin Command</button>
      </div>
    );
  }
});

export default ControlsContainer
