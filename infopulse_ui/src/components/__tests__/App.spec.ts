import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import App from '../../App.vue'
import router from '../../router'

describe('App', () => {
  it('renders without errors', async () => {
    const wrapper = mount(App, {
      global: {
        plugins: [router]
      }
    })

    await router.isReady()

    expect(wrapper.exists()).toBe(true)
  })
})