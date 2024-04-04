import type { Metadata } from 'next'
import { Roboto } from 'next/font/google'
import { Inter } from 'next/font/google'
import './globals.css'
import App from '@/components/App'

const roboto = Roboto({
  weight: ['400', '500', '700', '900'],
  subsets: ['latin', 'cyrillic'],
})

export const metadata: Metadata = {
  title: 'YTaudio',
  description: 'YouTube downloader',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang='en'>
      <body className={roboto.className}>
        <App>{children}</App>
      </body>
    </html>
  )
}
