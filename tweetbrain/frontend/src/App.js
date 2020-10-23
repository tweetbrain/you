import React from 'react';
import './App.css';
import Navigation from './components/Navigation/Navigation.js'
import Logo from './components/Logo/Logo.js'
import ImageLinkForm from './components/ImageLinkForm/ImageLinkForm.js'
import Song from './components/Song/Song.js'


class App extends React.Component{
  constructor() {
    super();
    this.state = {
      value: '',
      full_title: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    fetch("song.json") //fetches json object
        .then(response => response.json()) //returns a promise that needs to be turned into a javascript object
        //data from api
        .then(response => {
            console.log(response[0].full_title);
            this.setState({
                full_title: response[0].full_title
            })
        });
  } 


  handleChange(event) {
    this.setState({value: event.target.value});
    console.log(this.state.value)
  }

  handleSubmit(event) {
    alert('Twitter handle was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <div className="App">
        <Navigation/>
        <Logo/>
        <ImageLinkForm value={this.state.value} handleChange={this.handleChange} handleSubmit={this.handleSubmit}/>
        <Song full_title={this.state.full_title}/>
      </div>
    )
  }

  
}

export default App;
