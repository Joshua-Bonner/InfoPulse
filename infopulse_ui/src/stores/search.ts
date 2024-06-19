import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Ref } from 'vue'
import type { Search } from '@/types/search'

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
