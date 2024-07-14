import { defineStore } from 'pinia'
import { ref, computed, watchEffect } from 'vue'
import type { Ref } from 'vue'
import router from '@/router'
import type { UserToken, UserSearchPref } from '@/types/user'
import UserService from '@/services/UserService'

export const useUserStore = defineStore('user', () => {
  const userToken = ref(JSON.parse(localStorage.getItem('user') || '{}')) as Ref<UserToken>
  const curentUserName = computed(() => userToken.value.username)
  const userSearchPref = ref<UserSearchPref | null>(null)

  watchEffect(async () => {
    if (curentUserName.value) {
      const res = await UserService.fetchUserSearchPrefs(curentUserName.value)
      userSearchPref.value = res.data
    }
  })

  function setUserToken(newUser: UserToken) {
    userToken.value = newUser
  }

  function logout() {
    userToken.value = {} as UserToken
    localStorage.removeItem('user_token')
    router.push('/login')
  }

  return {
    userToken,
    userSearchPref,
    curentUserName,
    setUserToken,
    logout
  }
})
