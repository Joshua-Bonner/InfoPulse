import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { Article } from '@/stores/article'

interface Search {
  id: number
  query: string
  content: Article[]
}

export const useSearchStore = defineStore('search', () => {
  const searches: Ref<Search[]> = ref([])

  function addSearch(search: Search) {
    searches.value.push(search)
  }

  function clearSearches() {
    searches.value = []
  }

  return {
    searches,
    addSearch,
    clearSearches
  }
})
