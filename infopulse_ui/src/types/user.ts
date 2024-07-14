export interface UserToken {
  token: string
  token_type: string
  username: string
}

export interface User {
  id: number
  name: string
  username: string
  disabled: boolean
  token: UserToken
}

export interface UserSearchPref {
  id: number
  user_id: number
  search_in?: string[] | null
  search_from?: Date | null
  search_to?: Date | null
  sort_by?: string | null
}
