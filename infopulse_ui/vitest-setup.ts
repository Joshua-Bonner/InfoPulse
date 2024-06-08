import { config } from '@vue/test-utils'
import { createVuetify } from 'vuetify'
import { createPinia, setActivePinia } from 'pinia'
import 'vuetify/styles'

const vuetify = createVuetify()

// Global Vue Test Utils configuration
config.global.plugins.push({
  install: (app) => {
    app.use(vuetify)
  }
})

// Global Pinia configuration
export function setupPinia() {
  const pinia = createPinia()
  setActivePinia(pinia)
}
