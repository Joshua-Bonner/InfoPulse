<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import { useSearchStore } from '@/stores/search'

const searchQuery: Ref<string> = ref('')
const searchStore = useSearchStore()

const onClick = () => {
  if (!searchQuery.value) return
  searchStore.search(searchQuery.value)
  searchQuery.value = ''
}
</script>

<template>
  <v-container class="pt-10">
    <v-row>
      <v-col>
        <v-text-field
          v-model="searchQuery"
          placeholder="Search for articles..."
          variant="solo"
          density="compact"
          prepend-inner-icon="mdi-magnify"
          append-inner-icon="mdi-send"
          clearable
          rounded
          @click:append-inner="onClick"
          @keyup.enter="onClick"
          no-messages
        ></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped></style>
