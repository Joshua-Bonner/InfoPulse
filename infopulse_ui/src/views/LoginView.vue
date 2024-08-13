<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const username: Ref<string> = ref('')
const password: Ref<string> = ref('')
const showPass: Ref<boolean> = ref(false)
const loginForm: Ref<HTMLFormElement | null> = ref(null)

const login = () => {
  if (loginForm.value?.checkValidity()) {
    useAuthStore().login(username.value, password.value)
    loginForm.value?.reset()
  }
}
</script>

<template>
  <v-container class="container">
    <v-row justify="center" align="center">
      <v-col cols="6">
        <v-card>
          <v-card-title>
            <h1>InfoPulse</h1>
          </v-card-title>
          <v-card-text>
            <v-form @submit.prevent="login" @keyup.enter="login" ref="loginForm">
              <v-text-field
                v-model="username"
                label="Username"
                required
                prepend-icon="mdi-account"
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Password"
                required
                :append-inner-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append-inner="showPass = !showPass"
                :type="showPass ? 'text' : 'password'"
                prepend-icon="mdi-lock"
              ></v-text-field>
              <v-row>
                <v-col class="d-flex justify-end">
                  <v-btn @click="login">Login</v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="6" class="d-flex justify-start">
                  <router-link to="/acct-create">Create Account</router-link>
                </v-col>
                <v-col cols="6" class="d-flex justify-end">
                  <router-link to="/acct-recovery">Forgot password?</router-link>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-img src="https://picsum.photos/1500/1000" />
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.container {
  display: flex;
  align-items: center;
  height: 93vh;
  width: 90vw;
}
.form {
  margin: auto;
  min-height: 90%;
}
</style>
