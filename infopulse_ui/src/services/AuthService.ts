import { AuthClient } from './clients/AuthClient'

export default {
  login(username: string, password: string) {
    return AuthClient.post('/token', {
      username,
      password
    })
  },
}