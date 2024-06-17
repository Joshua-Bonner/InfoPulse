<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import { useSearchStore } from '@/stores/search'

const searchTab: Ref<string | null> = ref(null)
const searchStore = useSearchStore()
</script>
<template>
  <v-tabs v-model="searchTab" direction="vertical">
    <v-tab v-for="search in searchStore.searches" :key="search.id" :value="search.query">
      {{ search.query }}
    </v-tab>
  </v-tabs>

  <v-tabs-window v-model="searchTab" class="tab-content">
    <v-tabs-window-item
      v-for="search in searchStore.searches"
      :key="search.id"
      :value="search.content"
    >
      <v-card flat>
        <v-card-text> Content for {{ search.content }} </v-card-text>
      </v-card>
    </v-tabs-window-item>
  </v-tabs-window>
</template>

<style scoped>
.tab-content {
  margin-top: 10px;
  width: 90%;
  padding: 0;
}
</style>
