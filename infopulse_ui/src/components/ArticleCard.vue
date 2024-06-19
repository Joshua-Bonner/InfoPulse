<script setup lang="ts">
import { computed } from 'vue'
import type { Article } from '@/types/article'

const props = defineProps<{
  article: Article
}>()

const articleDate = computed(() => formatDate(props.article.publishedAt))

function formatDate(date: string): string {
  return new Date(date).toLocaleTimeString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>

<template>
  <v-card class="mx-auto" max-width="400" min-height="300" elevation="10">
    <v-img src="https://picsum.photos/400/100"></v-img>
    <v-card-title>{{ props.article.title }}</v-card-title>
    <v-card-subtitle>Written By: {{ props.article.author }}</v-card-subtitle>
    <v-card-subtitle>Published On: {{ articleDate }}</v-card-subtitle>
  </v-card>
</template>

<style scoped></style>
