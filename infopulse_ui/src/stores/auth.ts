import { defineStore } from 'pinia'
import type { Ref } from 'vue'
import { ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const returnUrl: Ref<string | null> = ref(null)

  async function login(username: string, password: string) {
    
  }

  function logout() {
    
  }

  return {
    user,
    returnUrl,
    login,
    logout,
  }
})