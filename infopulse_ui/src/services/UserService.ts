import { UserClient } from './clients/UserClient'
import type { UserSearchPref } from '@/types/user'

export default {
  fetchCurrentUser(token: string) {
    return UserClient.get('/current_user' + token)
  },
  createUser(data: any) {
    return UserClient.post('/', data)
  },
  updateUser(id: number, data: any) {
    return UserClient.put('/' + id, data)
  },
  deleteUser(id: number) {
    return UserClient.delete('/' + id)
  },
  fetchUserSearchPrefs(name: string) {
    return UserClient.get('/search_prefs/' + name)
  },
  updateUserSearchPrefs(id: Number, data: UserSearchPref) {
    return UserClient.put('/search_prefs/' + id, data)
  }
}
