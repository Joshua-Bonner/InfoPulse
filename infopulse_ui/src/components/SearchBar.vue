<script setup lang="ts">
import { ref } from 'vue'
import { useSearchStore } from '@/stores/search'
import { useArticleStore } from '@/stores/article'
import type { Ref } from 'vue'
import type { Article } from '@/types/article'
import type { Search } from '@/types/search'

const searchQuery: Ref<string> = ref('')
const searchStore = useSearchStore()
const articleStore = useArticleStore()

const onClick = () => {
  if (!searchQuery.value) return
  const article: Article = {
    id: 0,
    source: {
      id: 'test',
      name: 'test'
    },
    author: 'test',
    title: 'test',
    description: 'test',
    url: 'test',
    urlToImage: 'test',
    publishedAt: '2024-06-19T13:39:00Z',
    content:
      'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit voluptate velit esse cillum dolore fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt'
  }
  articleStore.addArticle(article)
  const newSearch: Search = {
    id: searchStore.searches.length + 1,
    query: searchQuery.value,
    articleIds: [0]
  }
  searchStore.addSearch(newSearch)
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
