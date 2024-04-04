'use client'
import { IDefaultLayout } from '@/types/layout.interface'

const App: React.FC<Readonly<IDefaultLayout>> = ({ children }) => {
  return (
    <main className='relative min-h-screen flex items-center justify-center p-24'>
      <input type="text" placeholder="Enter your link here" className="input input-ghost absolute top-60 w-full max-w-xs"/>
    </main>
  )
}

export default App
