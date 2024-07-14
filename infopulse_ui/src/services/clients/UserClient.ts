import axios from 'axios'

export const UserClient = axios.create({
  baseURL: 'http://localhost:8000/user',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json'
  },
  timeout: 10000
})
