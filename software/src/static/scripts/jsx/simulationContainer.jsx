import React from 'react';
import $ from "jquery";

const LineChart = require("react-chartjs").Line;

var SimulationBarChart = React.createClass({
  render: function() {
    var labels = [];
    var maxAltitudes = [];
    var maxVelocities = [];

    for(var launch in this.props.data) {
      labels.push(launch);
      maxAltitudes.push(this.props.data[launch]["launchStatistics"]["maxAltitude"]);
      maxVelocities.push(this.props.data[launch]["launchStatistics"]["maxVelocity"]);
    }

    var data = {
      labels: labels,
      datasets: [
        {
          label: "Max Altitudes",
          fillColor: "transparent",
          strokeColor: "black",
          pointColor: "black",
          pointStrokeColor: "black",
          pointHighlightFill: "black",
          pointHighlightStroke: "black",
          yAxisID: "maxAltitudeAxis",
          data: maxAltitudes
        },
        {
          label: "Max Velocities",
          fillColor: "transparent",
          strokeColor: "red",
          pointColor: "red",
          pointStrokeColor: "red",
          pointHighlightFill: "red",
          pointHighlightStroke: "red",
          yAxisID: "maxVelocityAxis",
          data: maxVelocities
        },
      ]
    };

    var options = {
      scales: {
        yAxes: [{
          position: "left",
          "id": "maxAltitudeAxis"
        }, {
          position: "right",
          "id": "maxVelocityAxis"
        }]
      }
    }

    return <LineChart data={data} options={options} width="800" height="600" />
  }
});

var Launch = React.createClass({
  launchAngle: function() {
    return <h4 className="launch-angle">Launch Angle: {this.props.data["launchAngle"]} </h4>;
  },

  launchStatistics: function() {
    var statistics = [];
    for(var statistic in this.props.data["launchStatistics"]) {
      statistics.push(<p className="statistic">{statistic}: {this.props.data["launchStatistics"][statistic]}</p>);
    }

    return statistics
  },

  render: function() {
    return(
      <div className="launch-container">
        <h3 className="launch-name">{this.props.name}</h3>
        {this.launchAngle()}
        {this.launchStatistics()}
      </div>
    );
  }
});

var Simulation = React.createClass({
  formattedSimulationData: function() {
    var launches = [];

    for (var launch in this.props.data) {
      launches.push(<Launch name={launch} data={this.props.data[launch]} />);
    }
    return(
      <div className="launches-container">
        {launches}
      </div>
    )
  },

  render: function() {
    return(
      <div className="simulation">
        <h3 className="simulation-name">Simulation Name: {this.props.name}</h3>
        <SimulationBarChart data={this.props.data} />
        {this.formattedSimulationData()}
      </div>
    );
  }
});

var SimulationContainer = React.createClass({
  getInitialState: function() {
    return({
      loading: false,
      loaded: false
    });
  },

  runSimulations: function() {
    this.setState({
      loading: true
    });

    $.ajax({
      url: '/simulations',
      dataType: 'json',
      success: function(data) {
        this.setState({
          data: JSON.parse(data),
          loading: false,
          loaded: true
        });
      }.bind(this)
    });
  },

  render: function() {
    var loadButtonText = this.state.loading ? "Loading" : "Run Simulations";
    var simulations = [];

    if (this.state.loaded) {
      for (var simulation in this.state.data) {
        simulations.push(<Simulation name={simulation} data={this.state.data[simulation]} />);
      }
    }

    if (this.state.loaded) {
      return(
        <div className="simulations-content">
          <h1>Simulations</h1>
          {simulations}
        </div>
      );
    } else {
      return(
        <div className="simulations-content">
          <h1>Simulations</h1>
          <input type="button" value={loadButtonText} onClick={this.runSimulations} />
        </div>
      );
    }
  }
});

export default SimulationContainer
