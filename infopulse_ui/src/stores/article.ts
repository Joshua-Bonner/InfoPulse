import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { Article } from '@/types/article'

export const useArticleStore = defineStore('article', () => {
  const articles: Ref<Article[]> = ref([])

  function addArticle(article: Article) {
    articles.value.push(article)
  }

  function getArticleById(id: number): Article {
    return articles.value.find((article) => article.id === id) as Article
  }

  return {
    articles,
    addArticle,
    getArticleById
  }
})
