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
  <v-sheet class="body" heigh="200">
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>{{ props.article.title }}</v-card-title>
          <v-card-subtitle>By: {{ props.article.author }}</v-card-subtitle>
          <v-card-subtitle>Published: {{ articleDate }}</v-card-subtitle>
          <v-card-text class="overflow-auto">{{ props.article.content }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-sheet>
</template>

<style scoped>
.body {
  height: 90vh;
  width: 180vh;
  display: flex;
  padding-top: 40px;
}
</style>
