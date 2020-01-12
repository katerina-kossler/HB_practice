class TradingCard extends React.Component {
  render() {
    return (
      <div className="card">
        <p>Name: {this.props.name}</p>
        <img src={this.props.imgUrl} />
        <p>Skill: {this.props.skill} </p>
      </div>
    );
  }
}
class TradingCardForm extends React.Component {
  constructor() {
    super()

    this.state = {
      name: '',
      skill: ''
    };

    this.handleNameChange = this.handleNameChange.bind(this);
    this.handleSkillChange = this.handleSkillChange.bind(this);
    this.addNewCard = this.addNewCard.bind(this);
  }

  addNewCard() {
    const newCard = this.state
    $.post('/add-card', newCard, this.updateCards)
  }

  updateCards() {
    $.get('/cards.json', this.props.handleNewCardAdded);
  }

  handleNameChange(e) {
    this.setState({ name: e.target.value });
  }

  handleSkillChange(e) {
    this.setState({ skill: e.target.value });
  }

  render() {
    return (
      <form>
        <label for="name">Name:</label>
        <input
          id="name"
          type="text"
          value={this.state.name}
          onChange={this.handleNameChange}
        />

        <label for="skill">Skill:</label>
        <input
          id="skill"
          type="text"
          value={this.state.skill}
          onChange={this.handleSkillChange}
        />

        <button onClick={this.addNewCard}>Add</button>
      </form>
    );
  }
}

class TradingCardContainer extends React.Component {
  constructor() {
    super();

    this.state = { cards: [] };
    this.updateCards = this.updateCards.bind(this);
  }

  getCardData() {
    $.get('/cards.json',this.updateCards);
  }

  componentDidMount() {
    this.getCardData();
  }
  
  updateCards(response) {
    const cards = response.cards;
    this.setState({ cards: cards});
  }
  
  render() {
    const tradingCards = [];

    for (const currentCard of this.state.cards) {
      tradingCards.push(
        <TradingCard
          key={currentCard.name}
          name={currentCard.name}
          skill={currentCard.skill}
          imgUrl={currentCard.imgUrl}
        />
      );
    }

    return (
      <div>
        <TradingCardForm handleNewCardAdded={this.updateCards}/>
        <div>{tradingCards}</div>
      </div>
    );
  }
}

ReactDOM.render(
  <TradingCardContainer />,
  document.getElementById('container')
);
