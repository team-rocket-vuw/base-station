var Sections = React.createClass({
  onSectionClick: function(e) {
    let sections = ["status", "controls", "location", "weather", "simulations"];
    e.preventDefault();

    var targetId = e.currentTarget.dataset.id;

    if (sections.includes(targetId)) {
      this.props.handleSectionChange(targetId);
    }
  },

  render: function() {
    return (
      <ul className="sections">
        <li onClick={this.onSectionClick} data-id="status" className={this.props.selectedSection == "status" ? "selected" : " "}>Status</li>
        <li onClick={this.onSectionClick} data-id="controls" className={this.props.selectedSection == "controls" ? "selected" : " "}>Controls</li>
        <li onClick={this.onSectionClick} data-id="location" className={this.props.selectedSection == "location" ? "selected" : " "}>Location</li>
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

var SideBar = React.createClass({
  render: function() {
    return (
      <div className="react-sidebar">
        <Header />
        <Sections selectedSection={this.props.selectedSection} handleSectionChange={this.props.handleSectionChange}/>
      </div>
    )
  }
});

var ContentContainer = React.createClass({
  render: function() {
    return (
      <div className="react-content">
        <p>Currently selected section: {this.props.selectedSection}</p>
        <p>{this.props.data.foo}</p>
      </div>
    );
  }
});

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
