<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'

const search: Ref<string> = ref('')

const onClick = () => {
  console.log('Search:', search.value)
}
</script>

<template>
  <v-container class="pt-10">
    <v-row>
      <v-col>
        <v-text-field
          v-model="search"
          placeholder="Search for articles..."
          variant="solo"
          density="compact"
          prepend-inner-icon="mdi-magnify"
          append-inner-icon="mdi-send"
          clearable
          rounded
          @click:append-inner="onClick"
          no-messages
        ></v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped></style>
