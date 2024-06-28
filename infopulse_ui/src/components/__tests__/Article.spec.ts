import { describe, it, expect } from 'vitest'
import { formatDate } from '@/components/article/ArticleHelper'

describe('Article Page', () => {
  it('formatDate function', () => {
    const date = '2024-06-28T16:41:02Z'
    const formattedDate = formatDate(date)
    expect(formattedDate).toBe('June 28, 2024 at 12:41:02 PM')
  })
})
