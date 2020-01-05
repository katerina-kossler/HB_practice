class About extends React.Component {
    render(){
        return (
        <div>
            <p>I am weird and collect my friends!
            <br />
            <a href="/cards">Click here</a> to view my very normal, not creepy cards!</p>
            Hey look, it's me! <br />
            <img src="/static/img/balloonicorn.jpg" />
        </div>
        );
    }
}

ReactDOM.render(<About />, document.getElementById('about'));