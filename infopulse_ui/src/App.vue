<script setup lang="ts">
import { RouterView } from 'vue-router'
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
</script>

<template>
  <v-app id="app">
    <AppHeader v-if="userStore.curentUserName" />
    <RouterView />
    <AppFooter />
  </v-app>
</template>

<style scoped></style>
