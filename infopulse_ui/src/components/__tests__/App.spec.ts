import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import { createPinia } from 'pinia'
import App from '@/App.vue'
import router from '@/router'

describe('App', () => {
  it('renders without errors', async () => {
    const pinia = createPinia()
    const wrapper = mount(App, {
      global: {
        plugins: [router, pinia]
      }
    })

    await router.isReady()

    expect(wrapper.exists()).toBe(true)
  })
})
