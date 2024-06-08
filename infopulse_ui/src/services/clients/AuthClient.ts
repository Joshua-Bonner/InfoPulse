import axios from 'axios'

export const AuthClient = axios.create({
  baseURL: 'http://localhost:8000/auth',
  withCredentials: false,
  headers: {
    Accept: 'application/x-www-form-urlencoded',
    'Content-type': 'application/x-www-form-urlencoded',
  },
  timeout: 10000,
})