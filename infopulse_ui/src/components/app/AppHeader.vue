<script setup lang="ts">
import SearchBar from '@/components/search/SearchBar.vue'
import SearchPref from '@/components/search/SearchPref.vue'
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const searchPrefVisible = ref(false)
const userStore = useUserStore()
</script>

<template>
  <v-container>
    <v-if>
      <search-pref v-model="searchPrefVisible" />
    </v-if>
    <v-app-bar :elevation="6" fixed color="deep-purple-accent-4">
      <v-app-bar-nav-icon icon="mdi-menu" rounded="0" />
      <v-toolbar-title class="d-flex justify-space-between text-uppercase font-weight-bold">
        InfoPulse
      </v-toolbar-title>
      <search-bar />
      <v-btn
        class="text-uppercase font-weight-bold"
        rounded="0"
        @click="$router.push({ name: 'dashboard' })"
        >Dashboard</v-btn
      >
      <v-btn rounded="0" icon="mdi-dots-vertical" @click="searchPrefVisible = true" />
      <v-btn rounded="0" id="logout" icon="mdi-logout" @click="userStore.logout" />
    </v-app-bar>
  </v-container>
</template>
