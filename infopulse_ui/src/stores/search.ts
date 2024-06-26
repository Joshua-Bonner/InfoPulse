import { defineStore } from 'pinia'
import { ref } from 'vue'
import SearchService from '@/services/SearchService'
import type { Ref } from 'vue'
import type { Search } from '@/types/search'
import type { Article } from '@/types/article'

export const useSearchStore = defineStore('search', () => {
  const searches: Ref<Search[]> = ref([])

  async function search(query: string) {
    const newSearch = await SearchService.search(query).then((response) => {
      return {
        id: response.data.id,
        query: response.data.query,
        articles: response.data.articles
      }
    })
    addSearch(newSearch)
  }

  function addSearch(search: Search) {
    searches.value.push(search)
  }

  function getArticleById(id: number) {
    return searches.value
      .flatMap((search) => search.articles)
      .find((article) => article.id === id) as Article
  }

  function clearSearches() {
    searches.value = []
  }

  return {
    searches,
    search,
    addSearch,
    getArticleById,
    clearSearches
  }
})
