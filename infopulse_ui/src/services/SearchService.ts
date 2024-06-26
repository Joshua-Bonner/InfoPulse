import { SearchClient } from './clients/SearchClient'

export default {
  search(query: string) {
    return SearchClient.get('/search?search_query=' + query)
  }
}
