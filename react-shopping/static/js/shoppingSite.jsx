class App extends React.Component {
  constructor() {
    super();

    this.state = {
      melons: {}
      shoppingCart: {}
    };

    this.renderAllMelonsPage = this.renderAllMelonsPage.bind(this);
  }

  componentDidMount() {
    $.get('/api/melons', (res) => {
      this.setState({ melons: res });
    });
  }

  addMelonToCart(melon) {
    this.setState((prevState) => {
      const newShoppingCart = Object.assign({}, prevState.shoppingCart);

      if (newShoppingCart[melon.melon_code]) {
        newShoppingCart[melon.melon_code] += 1;
      } else {
        newShoppingCart[melon.melon_code] = 1;
      }

      return {
        shoppingCart: newShoppingCart
      }
    });
  }

  renderHomePage() {
    return (
      <HomePage>
        <h1>Ubermelon.</h1>
        <p className="lead"> Melons on demand. </p>
      </HomePage>
    );
  }

  renderAllMelonsPage() {
    const melonCards = [];

    for (const melon of Object.values(this.state.melons)) {
      const melonCard = (
        <MelonCard
          key={melon.melon_code}
          code={melon.melon_code}
          name={melon.name}
          imgUrl={melon.image_url}
          price={melon.price}
        />
      );

      melonCards.push(melonCard);
    }

    return (
      <AllMelonsPage>
        {melonCards}
      </AllMelonsPage>
    );
  }

  renderShoppingCart() {
    return (
      <ShoppingCartPage>
        <table className="table">
          <thead>
            <tr>
              <th>Melon</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
          </tbody>
        </table>
        <p className="lead">Total: ${(0).toFixed(2)}</p>
      </ShoppingCartPage>
    );
  }

  render() {
    return (
      <ReactRouterDOM.BrowserRouter>
        <Navbar
          logo="/static/img/watermelon.png"
          brand="Ubermelon"
        >
          <ReactRouterDOM.NavLink
            to="/shop"
            activeClassName="navlink-active"
            className="nav-link"
          >
            Shop for Melons
          </ReactRouterDOM.NavLink>
          <ReactRouterDOM.NavLink
            to="/cart"
            activeClassName="navlink-active"
            className="nav-link"
          >
            Shopping Cart
          </ReactRouterDOM.NavLink>
        </Navbar>

        <div className="container-fluid">
          <ReactRouterDOM.Route
            exact
            path="/"
            render={this.renderHomePage}
          />
          <ReactRouterDOM.Route
            exact
            path="/shop"
            render={this.renderAllMelonsPage}
          />
          <ReactRouterDOM.Route
            exact
            path="/cart"
            render={this.renderShoppingCart}
          />
        </div>
      </ReactRouterDOM.BrowserRouter>
    );
  }
}

ReactDOM.render(<App />, document.querySelector('#root'));
