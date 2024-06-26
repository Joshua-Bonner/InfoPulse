import { AuthClient } from './clients/AuthClient'

export default {
  login(username: string, password: string) {
    return AuthClient.post('/token', {
      grant_type: 'password',
      username,
      password,
      scope: 'openid profile',
      client_id: '',
      client_secret: ''
    })
  }
}
