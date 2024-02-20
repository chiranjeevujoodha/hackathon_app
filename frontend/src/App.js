
import './App.css';
import axios from 'axios';
import React from 'react';

class App extends React.Component {
  state = {details: [], }

  componentDidMount() {

    let data;
    axios.get('http://localhost:8000')
    .then(res => {
      data = res.data;
      this.setState({
        details: data
      })
    })
    .catch(err => { })
  }



render() {
  return(
    <div>
      <header>Django data</header>
      <hr></hr>
      {this.state.details.map((output, id) => (
        <div key={id}>
          <p>{output.fname}</p>
        </div>
      ))}

    </div>
  );
}

} 

export default App;
