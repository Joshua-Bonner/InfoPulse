<script setup lang="ts">
import { computed } from 'vue'
import { formatDate } from '@/components/article/ArticleHelper'
import type { Article } from '@/types/article'

const props = defineProps<{
  article: Article
}>()

const articleDate = computed(() => formatDate(props.article.publishedAt))
</script>

<template>
  <v-card
    class="mx-auto overflow-auto"
    max-width="400"
    min-height="300"
    elevation="10"
    @click="$router.push({ name: 'article', params: { id: props.article.id } })"
  >
    <v-card-title>{{ props.article.title }}</v-card-title>
    <v-img :src="props.article.urlToImage"></v-img>
    <v-card-subtitle>Written By: {{ props.article.author }}</v-card-subtitle>
    <v-card-subtitle>Published On: {{ articleDate }}</v-card-subtitle>
  </v-card>
</template>

<style scoped></style>
