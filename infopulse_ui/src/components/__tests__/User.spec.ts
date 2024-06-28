import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import { createPinia } from 'pinia'
import AppHeader from '@/components/app/AppHeader.vue'
import router from '@/router'
import { useUserStore } from '@/stores/user'

describe('User', () => {
  it('Logout', async () => {
    const pinia = createPinia()
    const wrapper = mount(AppHeader, {
      global: {
        plugins: [router, pinia]
      }
    })
    const userStore = useUserStore(pinia)
    userStore.setUser({
      token: 'test',
      token_type: 'Bearer',
      username: 'test'
    })

    await router.isReady()
    await wrapper.find('#logout').trigger('click')

    expect(router.currentRoute.value.path).toBe('/login')
    expect(userStore.user).toEqual({})
    expect(wrapper.exists()).toBe(true)
  })
})
