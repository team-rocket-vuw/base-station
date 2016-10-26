import React from 'react';
import $ from "jquery";


var WeatherContainer = React.createClass({
  getInitialState: function() {
    return({
      latValue: "",
      lngValue: ""
    });
  },

  getWeatherData: function() {
    $.ajax({
      type: "POST",
      dataType: 'json',
      url: `weather?lat=${this.state.latValue}&lng=${this.state.lngValue}&APPID=dfcb3e37ff82ecb487b5c45648cdef5b`,
      success: function(data) {
        this.setState({
          weatherData: data,
        });
      }.bind(this)
    });
  },

  handleChange: function(type, event) {
    if(type == "latValue") {
      this.setState({ "latValue": event.target.value });
    } else if(type == "lngValue") {
      this.setState({ "lngValue": event.target.value });
    }
  },

  renderFormattedWeatherData: function() {
    if (this.state.weatherData) {
      var data = this.state.weatherData["main"];
      return(
        <div>
          <h3>Weather Station Coordinates</h3>
          <ul>
            <li>Latitude: {this.state.weatherData["coord"]["lat"]}</li>
            <li>Longitude: {this.state.weatherData["coord"]["lon"]}</li>
          </ul>

          <h3>Weather conditions</h3>
          <ul>
            <li>Temperature: {Math.round(data["temp"] - 273.15)}</li>
            <li>Pressure: {data["pressure"]}</li>
            <li>Humidity: {data["humidity"]}</li>
            <li>Minimum Temperature: {data["temp_min"]}</li>
            <li>Maximum Temperature: {data["temp_max"]}</li>
            <li>Sea Level: {data["sea_level"]}</li>
            <li>Ground Level: {data["grnd_level"]}</li>
          </ul>

          <h3>Wind Conditions</h3>
          <ul>
            <li>Speed: {this.state.weatherData["wind"]["speed"]}</li>
            <li>Angle: {this.state.weatherData["wind"]["deg"]}</li>
          </ul>
        </div>
      );
    } else {
      return
    }
  },

  render: function() {
    return(
      <div className="weather-container">
        <input type="text" placeholder="Latitude" value={this.state.latValue} onChange={(e) => this.handleChange("latValue", e)} />
        <input type="text" placeholder="Longitude" value={this.state.lngValue} onChange={(e) => this.handleChange("lngValue", e)} />
        <button className="toggle-button" onClick={this.getWeatherData}>Get Weather Data</button>
        {this.renderFormattedWeatherData()}
      </div>
    );
  }
});

export default WeatherContainer
