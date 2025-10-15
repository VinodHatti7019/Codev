// Root layout for Codev Web UI
// This file defines the basic HTML structure and providers for the entire application
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { ChakraProvider } from '@chakra-ui/react'
import { theme } from './theme'

// Configure Inter font for the application
const inter = Inter({ subsets: ['latin'] })

// Application metadata
export const metadata: Metadata = {
  title: 'Codev - AI-Powered Task Execution Platform',
  description: 'Modern web interface for Codev AI task execution platform with real-time results',
}

// Root layout component
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="dark">
      <body className={inter.className}>
        {/* Wrap application in Chakra UI provider for component library support */}
        <ChakraProvider theme={theme}>
          {children}
        </ChakraProvider>
      </body>
    </html>
  )
}
