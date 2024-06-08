import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import { createPinia } from 'pinia'
import LoginView from '@/views/LoginView.vue'
import router from '@/router'

describe('Login', () => {
  it('renders without errors', async () => {
    const pinia = createPinia()
    const wrapper = mount(LoginView, {
      global: {
        plugins: [router, pinia]
      }
    })

    await router.isReady()

    expect(wrapper.exists()).toBe(true)
  })
})
