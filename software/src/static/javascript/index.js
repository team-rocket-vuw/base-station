var TeamRocket = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Team Rocket</h1>
        <h3>{this.props.data.foo}</h3>
      </div>
    );
  }
});

var refreshTime = 50;

setInterval(function() {
  $.get("http://127.0.0.1:5000/data", function (response) {
    var data = JSON.parse(response);

    ReactDOM.render(
      <TeamRocket data={data} />,
      document.getElementById('container')
    );
  });
}, refreshTime);
