import { describe, it, expect, vi } from 'vitest'
import SearchService from '@/services/SearchService'
import { SearchClient } from '@/services/clients/SearchClient'

vi.mock('./clients/SearchClient', () => ({
  get: vi.fn(() => Promise.resolve({ data: 'mocked response' }))
}))

describe('Search', () => {
  it('search should call SearchClient.get with correct URL', async () => {
    const query = 'testQuery'

    await SearchService.search(query)

    expect(SearchClient.get).toHaveBeenCalledWith('/search?search_query=' + query)
  })
})
