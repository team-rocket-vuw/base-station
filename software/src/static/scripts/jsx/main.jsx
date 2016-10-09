import React from 'react';
import ReactDOM from 'react-dom';
import $ from "jquery";

import SideBar from './sidebar.jsx';
import ContentContainer from './contentContainer.jsx';

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
        <SideBar selectedSection={this.state.selectedSection} handleSectionChange={this.handleSectionChange} />
        <ContentContainer data={this.props.data} selectedSection={this.state.selectedSection}/>
      </div>
    );
  }
});

var refreshTime = 100;

setInterval(function() {
  $.get("http://127.0.0.1:5000/data", function (response) {
    var data = JSON.parse(response);

    ReactDOM.render(
      <TeamRocket data={data} />,
      document.getElementById('react-hook')
    );
  });
}, refreshTime);
