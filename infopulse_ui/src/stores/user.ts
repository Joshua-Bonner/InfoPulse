import { defineStore } from 'pinia'
import { ref } from 'vue'

interface User {
  id: number
  username: string
}

export const useUserStore = defineStore('user', () => {
})