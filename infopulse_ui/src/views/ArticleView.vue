<script setup lang="ts">
import { computed } from 'vue'
import { formatDate } from '@/components/article/ArticleHelper'
import { useArticleStore } from '@/stores/article'
import type { Article } from '@/types/article'

const props = defineProps<{
  id: number
}>()

const article: Article = useArticleStore().getArticleById(props.id)
const articleDate = computed(() => formatDate(article.publishedAt))
</script>

<template>
  <v-sheet class="body" heigh="200">
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>{{ article.title }}</v-card-title>
          <v-card-subtitle>By: {{ article.author }}</v-card-subtitle>
          <v-card-subtitle>Published: {{ articleDate }}</v-card-subtitle>
          <v-card-text class="overflow-auto">{{ article.content }}</v-card-text>
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
