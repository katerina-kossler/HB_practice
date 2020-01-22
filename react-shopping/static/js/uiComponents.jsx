const HomePage = (props) => {
  return (
    <div
      id="home-banner"
      className="row"
    >
      <div className="col">
        {props.children}
      </div>
    </div>
  );
}

const PageContainer = (props) => {
  const { children, className, title, ...rest } = props;
  return(
    <ReactRouterDOM.BrowserRouter>
      <h1>{title}</h1>
      <div
        {...rest}
        className={`row ${className || ''}`}
      >
        {children}
      </div>
    </ReactRouterDOM.BrowserRouter>
  );
}

const AllMelonsPage = (props) => {
  const { children } = props;
  return (
    <PageContainer title="All Melons" id="shopping">
      <div className="col-12 col-md-9 d-flex flex-wrap">
        {children}
      </div>
    </PageContainer>
  );
}

const ShoppingCartPage = (props) => {
  const { children } = props;
  return (
    <PageContainer title="Shopping Cart" id="shoppingCart">
      <div className="col-6">
        {children}
      </div>
    </PageContainer>
  );
}

const Navbar = (props) => {
  const { logo, brand, children, className } = props;

  const navLinks = children.map((el, i) => {
    return <div key={i} className="nav-item">{el}</div>;
  });

  return (
    <nav className={`navbar ${className || ''}`}>
      <ReactRouterDOM.Link to="/" className="havbar-brand d-flex justify-content-center">
        <img src={logo} height="30" />
        <span>{brand}</span>
      </ReactRouterDOM.Link>

      <section className="d-flex justify-content-center">
        {navLinks}
      </section>
    </nav>
  );
}

function MelonCard(props) {
  const { code, name, imgUrl, price, handleAddToCart } = props;

  return (
    <div className="card melon-card">
      <ReactRouterDOM.Link to={`/shop/${code}`}>
        <img src={imgUrl} className="card-img-top" />
      </ReactRouterDOM.Link>
      <div className="card-body">
        <h5 className="card-title">
          <ReactRouterDOM.Link to={`/shop/${code}`}>{name}</ReactRouterDOM.Link>
        </h5>
      </div>
      <div className="card-body pt-0 container-fluid">
        <div className="row">
          <div className="col-12 col-lg-6">
            <span className="lead price d-inline-block">
              ${price.toFixed(2)}
            </span>
          </div>
          <div className="col-12 col-lg-6">
            <a
              className="btn btn-sm btn-success d-inline-block"
              onClick={handleAddToCart}
            >
              Add to cart
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

/* The components below are for Further Study */

const Checkbox = (props) => {
  const { id, onClick, checked, label, className } = props;

  return (
    <div className={`custom-control custom-checkbox ${className || ''}`}>
      <input
        type="checkbox"
        className="custom-control-input"
        id={id}
        onClick={onClick}
        checked={checked}
      />
      <label
        className="custom-control-label"
        for={id}
      >
        {label}
      </label>
    </div>
  );
}

const Select = (props) => {
  const { selectedValue } = props;

  const options = this.props.options((opt) => {
    return (
      <option
        value={opt.value}
        selected={selectedValue === opt.value}
      >
        {opt.label}
      </option>
    );
  });

  return (
    <select className="custom-select">
      {options}
    </select>
  );
}
