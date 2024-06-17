import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Ref } from 'vue'

interface Source {
  id: string
  name: string
}

export interface Article {
  source: Source
  author: string
  title: string
  description: string
  url: string
  urlToImage: string
  publishedAt: string
  content: string
}

export const useArticleStore = defineStore('article', () => {
  const articles: Ref<Article[]> = ref([])

  return {
    articles
  }
})
