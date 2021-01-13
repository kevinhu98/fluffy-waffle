require('dotenv').config()
const mongoose = require('mongoose')
const url = process.env.REACT_APP_MONGODB_URI

mongoose.connect(url, { useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify: false, useCreateIndex: true })
const movieSchema = new mongoose.Schema({
    id: String,
    title: String,
    release_date: Date,
    poster_path: String,
    overview: String,
    genres: Array
  })

const Movie = mongoose.model('Movie', movieSchema)

Movie.find({}).then(result => {
    result.forEach(movie => {
      console.log(movie)
    })
    mongoose.connection.close()
  })

