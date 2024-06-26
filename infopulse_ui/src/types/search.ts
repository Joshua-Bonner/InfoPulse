import type { Article } from './article'

export interface Search {
  id: number
  query: string
  articles: Article[]
}
