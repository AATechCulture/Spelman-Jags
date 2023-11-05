import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from '../Header';
import Schedule from '../Schedule';
import TradeRequests from '../TradeRequests';

function App() {
  return (
    <Router>
      <div>
        <Header />
        <Switch>
          <Route path="/trades" component={TradeRequests} />
          <Route path="/" component={Schedule} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
