<script setup lang="ts">
import { ref } from 'vue'
import type { Account } from '@/types/Account'

const accountForm = ref<HTMLFormElement | null>(null)
const account = ref<Account>({
  username: '',
  password: '',
  security_question: '',
  security_answer: ''
})
</script>

<template>
  <v-container class="w-25">
    <v-card>
      <v-card-title>
        <h3>Account Recovery</h3>
      </v-card-title>
    </v-card>
  </v-container>
</template>
