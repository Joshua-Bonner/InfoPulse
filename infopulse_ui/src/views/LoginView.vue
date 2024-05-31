<script setup lang="ts">
import { ref } from 'vue'

const username = ref('')
const password = ref('')
const login = () => {
  console.log('Login', username.value, password.value)
}

</script>

<template>
  <v-container class="container">
    <v-row>
      <v-col cols="6">
        <v-card>
          <v-card-title>
            <h1>InfoPulse</h1>
          </v-card-title>
          <v-card-text>
            <v-form>
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
                type="password"
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
                  <router-link to="/cred-recovery">Forgot password?</router-link>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-img src="https://picsum.photos/500/300" />
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.container {
  display: flex;
  align-items: center;
  height: 90vh;
  width: 90vw;
}
.form {
  margin: auto;
  min-height: 90%;
}
</style>