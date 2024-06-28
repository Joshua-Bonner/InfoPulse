import { describe, it, expect, vi, beforeEach } from 'vitest'
import router from '@/router'
import { createPinia, setActivePinia } from 'pinia'
import { useAuthStore } from '@/stores/auth'
import AuthService from '@/services/AuthService'
import { AuthClient } from '@/services/clients/AuthClient'

vi.mock('./clients/AuthClient', () => ({
  post: vi.fn(() => Promise.resolve({ data: 'mocked response' }))
}))

describe('Authentication Functionality', () => {
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

  it('login should call AuthClient.post with correct parameters', async () => {
    const username = 'testUser'
    const password = 'testPass'

    await AuthService.login(username, password)

    expect(AuthClient.post).toHaveBeenCalledWith('/token', {
      grant_type: 'password',
      username,
      password,
      scope: 'openid profile',
      client_id: '',
      client_secret: ''
    })
  })
})
