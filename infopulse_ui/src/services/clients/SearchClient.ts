import axios from 'axios'

export const SearchClient = axios.create({
  baseURL: 'http://localhost:8000/search',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json'
  },
  timeout: 10000
})
