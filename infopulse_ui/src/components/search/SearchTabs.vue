<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import { useSearchStore } from '@/stores/search'
import articleCard from '@/components/article/ArticleCard.vue'
import { useArticleStore } from '@/stores/article'

const searchTab: Ref<number | null> = ref(0)
const searchStore = useSearchStore()
const articleStore = useArticleStore()
</script>
<template>
  <v-tabs v-model="searchTab" direction="vertical" class="tabs" color="deep-purple-accent-4">
    <v-tab v-for="search in searchStore.searches" :key="search.id" :value="search.id" class="tab">
      {{ search.query }}
    </v-tab>
  </v-tabs>

  <v-tabs-window v-model="searchTab" class="tab-content">
    <v-tabs-window-item v-for="search in searchStore.searches" :key="search.id" :value="search.id">
      <v-row>
        <v-col v-for="articleId in search.articleIds" :key="articleId">
          <article-card :article="articleStore.getArticleById(articleId)" />
        </v-col>
      </v-row>
    </v-tabs-window-item>
  </v-tabs-window>
</template>

<style scoped>
.tab-content {
  margin-top: 10px;
  width: 90%;
  padding: 0;
  justify-items: center;
}
.tabs {
  max-width: 200px;
}
.tab {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
