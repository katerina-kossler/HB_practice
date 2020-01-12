class Homepage extends React.Component {
  render(){
    return (
      <div>
        <img src="/static/img/balloonicorn.jpg" />

        <p>This is a great site for viewing trading cards.</p>

        <a href="/cards-jquery">
          Click here to view the trading cards page in JQuery.
        </a>
        <br/>
        <a href="/cards">
          Click here to view the trading cards page in React.
        </a>


      </div>

    );
  }
}

ReactDOM.render(<Homepage />, document.getElementById('app'));
