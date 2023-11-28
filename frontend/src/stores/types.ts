export interface User {
  id: number,
  username: string,
  first_name: string,
  last_name: string,
  email: string
}

export interface Message {
  owner: number,
  group: number,
  content: string,
  share_id: number,
  share_count: number,
  good_count: number,
  pub_date: Date,
}