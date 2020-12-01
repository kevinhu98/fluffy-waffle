import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

const mongoose = require('mongoose')

const url = `mongodb+srv://kevin:${password}@cluster0.8xh0x.mongodb.net/<note-app>?retryWrites=true&w=majority`

mongoose.connect(url, { useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify: false, useCreateIndex: true })

const movieSchema = new mongoose.Schema({
  //id: String,
  title: String,
  releaseDate: Date,
  imageUrl: String,
  popularity: Number,
  description: String,
  genre: String
})

const Movie = mongoose.model('Movie', movieSchema)

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);


