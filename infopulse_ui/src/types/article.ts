interface Source {
  id: string
  name: string
}

export interface Article {
  id: number
  source: Source
  author: string
  title: string
  description: string
  url: string
  urlToImage: string
  publishedAt: string
  content: string
}
