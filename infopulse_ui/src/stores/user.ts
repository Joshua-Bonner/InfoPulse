import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { Ref } from 'vue'
import router from '@/router'
interface User {
  token: string
  token_type: string
  username: string
}

export const useUserStore = defineStore('user', () => {
  const user = ref(JSON.parse(localStorage.getItem('user') || '{}')) as Ref<User>
  const curentUserName = computed(() => user.value.username)

  function setUser(newUser: User) {
    user.value = newUser
  }

  function logout() {
    user.value = {} as User
    localStorage.removeItem('user')
    router.push('/login')
  }

  return {
    user,
    curentUserName,
    setUser,
    logout
  }
})
