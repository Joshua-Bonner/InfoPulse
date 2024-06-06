import axios from 'axios'

export const AuthClient = axios.create({
  baseURL: 'http://localhost:8000/auth',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json',
  },
  timeout: 10000,
})