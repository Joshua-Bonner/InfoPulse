import { defineStore } from 'pinia'
import type { Ref } from 'vue'
import { ref } from 'vue'
import AuthService from '@/services/AuthService'
import { useUserStore } from './user'
import router from '@/router'

export const useAuthStore = defineStore('auth', () => {
  const returnUrl: Ref<string | null> = ref(null)

  async function login(username: string, password: string) {
    try {
      const userStore = useUserStore()
      const response = await AuthService.login(username, password)
      userStore.setUserToken(response.data)
      localStorage.setItem('user_token', JSON.stringify(response.data))
      router.push(returnUrl.value || '/dashboard')
    } catch (error: any) {
      if (error.response.status === 401) {
        alert('Invalid credentials')
      } else {
        alert('An error occurred')
      }
    }
  }

  return {
    returnUrl,
    login
  }
})
