'use client'
import { IDefaultLayout } from '@/types/layout.interface'
import axios from 'axios'
import * as cheerio from 'cheerio'

const App: React.FC<Readonly<IDefaultLayout>> = ({ children }) => {
  const video_id: string = 'YouTube video link'

  async function getYouTubePreview(id: string): Promise<string | null> {
    try {
      const response = await axios.get(`https://www.youtube.com/watch?v=${id}`)
      const $ = cheerio.load(response.data)
      const previewUrl = $('meta[property="og:image"]').attr('content')

      if (previewUrl) {
        return previewUrl
      } else {
        console.log('Failed to find preview image URL.')
        return null
      }
    } catch (error) {
      console.error('Error fetching YouTube video preview:')
      return null
    }
  }

  const linkSubmit = async () => {
    getYouTubePreview(video_id)
    console.log("EQEQEQ")
  }

  return (
    <main className='relative min-h-screen flex items-center justify-center p-24'>
      <form
        onSubmit={linkSubmit}
        className='absolute top-60 w-full max-w-xs'
      >
        <label className='input input-bordered flex items-center gap-2 absolute w-full max-w-xs'>
          <input type='text' className='grow' placeholder='Search' />
          <svg
            xmlns='http://www.w3.org/2000/svg'
            viewBox='0 0 16 16'
            fill='currentColor'
            className='w-4 h-4 opacity-70'
          >
            <path
              fillRule='evenodd'
              d='M9.965 11.026a5 5 0 1 1 1.06-1.06l2.755 2.754a.75.75 0 1 1-1.06 1.06l-2.755-2.754ZM10.5 7a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0Z'
              clipRule='evenodd'
            />
          </svg>
        </label>
      </form>
    </main>
  )
}

export default App
