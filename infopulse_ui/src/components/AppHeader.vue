<script setup lang="ts">
import SearchBar from '@/components/SearchBar.vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
</script>

<template>
  <v-container>
    <v-app-bar :elevation="6" fixed>
      <v-app-bar-nav-icon icon="mdi-menu" rounded="0" />
      <v-toolbar-title class="d-flex justify-space-between text-uppercase font-weight-bold">
        InfoPulse
      </v-toolbar-title>
      <search-bar />
      <v-btn class="text-uppercase font-weight-bold" rounded="0">Dashboard</v-btn>
      <v-btn rounded="0" icon="mdi-dots-vertical" />
      <v-btn rounded="0" id="logout" icon="mdi-logout" @click="userStore.logout" />
    </v-app-bar>
  </v-container>
</template>
