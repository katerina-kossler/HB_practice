class Homepage extends React.Component {
	render(){
		return (
        <div>
            <p>Welcome to my weird trading card game, my dear tradable friends!
            <br />
            <a href="/cards">Click here</a> to view my very normal, not creepy cards!</p>
            <img src="/static/img/balloonicorn.jpg" />
            <p>And you can <a href="/about">click here</a> to learn about very sensible me!</p>
        </div>
        );
	}
}

ReactDOM.render(<Homepage />, document.getElementById('app'));