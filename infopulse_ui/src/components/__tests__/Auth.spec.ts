import { describe, it, expect, vi, beforeEach } from 'vitest'
import router from '@/router'
import { createPinia, setActivePinia } from 'pinia'
import { useAuthStore } from '@/stores/auth'

describe('Login Functionality', () => {
  let authStore: ReturnType<typeof useAuthStore>

  beforeEach(() => {
    const pinia = createPinia()
    setActivePinia(pinia)
    authStore = useAuthStore()
    router.push('/')
  })

  it('successfully logs in a user', async () => {
    const mockApiCall = vi.fn().mockResolvedValue({
      user: {
        token: 'fake_token',
        token_type: 'Bearer',
        username: 'testuser'
      }
    })
    vi.spyOn(authStore, 'login').mockImplementation(mockApiCall)

    const result = await useAuthStore().login('testuser', 'password123')

    expect(mockApiCall).toHaveBeenCalled()
    expect(result.user.token).toBe('fake_token')
  })
})
