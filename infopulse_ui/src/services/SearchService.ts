import { SearchClient } from './clients/SearchClient'

export default {
  search(query: string) {
    return SearchClient.get('/?search_query=' + query)
  },
  fetchSearches() {
    return SearchClient.get('/all')
  }
}
