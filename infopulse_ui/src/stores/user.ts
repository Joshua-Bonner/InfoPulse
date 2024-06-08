import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Ref } from 'vue'

interface User {
  token: string
  token_type: string
  username: string
}

export const useUserStore = defineStore('user', () => {
  const user = ref(JSON.parse(localStorage.getItem('user') || '{}')) as Ref<User>

  function setUser(newUser: User) {
    user.value = newUser
  }

  return {
    user,
    setUser
  }
})
