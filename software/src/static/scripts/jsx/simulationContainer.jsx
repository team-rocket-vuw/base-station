import React from 'react';
import $ from "jquery";
import rd3 from 'rd3';

const LineChart = rd3.LineChart;

var SimulationLineChart = React.createClass({
  getInitialState: function() {
    var labels = [];
    var maxAltitudes = [];
    var maxVelocities = [];
    var maxAccelerations = [];

    var counter = 0;
    for(var launch in this.props.data) {
      labels.push(launch);
      maxAltitudes.push({x: counter, y: this.props.data[launch]["launchStatistics"]["maxAltitude"]});
      maxVelocities.push({x: counter, y: this.props.data[launch]["launchStatistics"]["maxVelocity"]});
      maxAccelerations.push({x: counter, y: this.props.data[launch]["launchStatistics"]["maxAcceleration"]});
      counter++;
    }

    var data = [
      {
        name: 'Max Altitude',
        values: maxAltitudes
      },
      {
        name: 'Max Velocity',
        values: maxVelocities
      },
      {
        name: 'Max Acceleration',
        values: maxAccelerations
      },
    ];

    return({
      data: data
    });
  },

  render: function() {
    return(
      <div className="simulation-chart">
        <LineChart
          legend={true}
          data={this.state.data}
          width='800px'
          height={400}
          viewBoxObject={{
            x: 0,
            y: 0,
            width: 500,
            height: 400
          }}
          title="Simulation Data Chart"
          yAxisLabel="Unit"
          xAxisLabel="Launch Number"
          domain={{x: [,46], y: [0,]}}
          gridHorizontal={true}
        />
      </div>
  )}
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
        <SimulationLineChart data={this.props.data} />
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
