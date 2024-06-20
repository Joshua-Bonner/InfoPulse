export function formatDate(date: string): string {
  return new Date(date).toLocaleTimeString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
