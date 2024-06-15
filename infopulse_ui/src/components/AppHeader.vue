<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import SearchBar from '@/components/SearchBar.vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const showTabsDialog: Ref<boolean> = ref(false)
</script>

<template>
  <v-container>
    <v-app-bar :elevation="6" fixed>
      <v-app-bar-nav-icon
        icon="mdi-menu"
        @click.stop="showTabsDialog = !showTabsDialog"
        rounded="0"
      />
      <v-toolbar-title class="d-flex justify-space-between text-uppercase font-weight-bold">
        InfoPulse
      </v-toolbar-title>
      <SearchBar />
      <v-btn class="text-uppercase font-weight-bold" rounded="0">Dashboard</v-btn>
      <v-btn rounded="0" icon="mdi-dots-vertical" />
      <v-btn rounded="0" id="logout" icon="mdi-logout" @click="userStore.logout" />
    </v-app-bar>
  </v-container>
</template>
