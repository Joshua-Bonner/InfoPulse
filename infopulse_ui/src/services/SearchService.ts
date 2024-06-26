import { SearchClient } from './clients/SearchClient'

export default {
  search(query: string) {
    return SearchClient.post('/search', {
      query
    })
  }
}
