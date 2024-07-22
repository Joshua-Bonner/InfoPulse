<script setup lang="ts">
import type { Account } from '@/types/account'
import router from '@/router'
import { ref, type Ref } from 'vue'
import UserService from '@/services/UserService'

const accountForm = ref<HTMLFormElement | null>(null)

const newAccount = ref<Account>({
  name: '',
  username: '',
  password: '',
  security_question: '',
  security_answer: '',
  disabled: false
})

const verifyPassword: Ref<string> = ref('')

const questions: string[] = [
  'In what city where you born?',
  'What is the name of your favorite pet?',
  'What is your favorite movie?',
  'What is your mothers maiden name?'
]

const createAccount = async () => {
  if (newAccount.value.password !== verifyPassword.value) {
    alert('Passwords do not match')
    return
  }

  await UserService.createUser(newAccount.value)
    .then(() => {
      alert('Account created successfully')
      router.push({ name: 'login' })
    })
    .catch((error) => {
      alert(error)
    })
}
</script>

<template>
  <v-container class="w-25">
    <v-card>
      <v-card-title>
        <h3>Create Account</h3>
      </v-card-title>
      <v-card-text>
        <v-form ref="accountForm" @submit.prevent="createAccount">
          <v-text-field v-model="newAccount.name" label="Name" required></v-text-field>
          <v-text-field v-model="newAccount.username" label="Username" required></v-text-field>
          <v-text-field
            v-model="newAccount.password"
            label="Password"
            required
            type="password"
          ></v-text-field>
          <v-text-field
            v-model="verifyPassword"
            label="Verify Password"
            required
            type="password"
          ></v-text-field>
          <v-select
            v-model="newAccount.security_question"
            :items="questions"
            label="Security Question"
            required
          ></v-select>
          <v-text-field
            v-model="newAccount.security_answer"
            label="Security Answer"
            required
          ></v-text-field>
          <v-btn type="submit" color="primary">Create</v-btn>
          <v-btn class="ml-4" @click="$router.push('login')">Cancel</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>
