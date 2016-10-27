import React from 'react';

var Sections = React.createClass({
  onSectionClick: function(e) {
    let sections = ["launchOps", "weather", "simulations"];
    e.preventDefault();

    var targetId = e.currentTarget.dataset.id;

    if (sections.includes(targetId)) {
      this.props.handleSectionChange(targetId);
    }
  },

  render: function() {
    return (
      <ul className="sections">
        <li onClick={this.onSectionClick} data-id="launchOps" className={this.props.selectedSection == "launchOps" ? "selected" : " "}>Launch Ops</li>
        <li onClick={this.onSectionClick} data-id="weather" className={this.props.selectedSection == "weather" ? "selected" : " "}>Weather</li>
        <li onClick={this.onSectionClick} data-id="simulations" className={this.props.selectedSection == "simulations" ? "selected" : " "}>Simulations</li>
      </ul>
    );
  }
});

var Header = React.createClass({
  render: function() {
    return (
      <div className="header">
        <img className="icon" src="/static/assets/icons/missile.png"/>
        <div className="title">
          <p>Teamrocket</p>
          <p>Basestation</p>
          <p className="version">V1.0</p>
        </div>
      </div>
    );
  }
});

var Sidebar = React.createClass({
  render: function() {
    return (
      <div className="react-sidebar">
        <Header />
        <Sections selectedSection={this.props.selectedSection} handleSectionChange={this.props.handleSectionChange}/>
      </div>
    )
  }
});

export default Sidebar;
