import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  async headers() {
    return [{
      source: '/(.*)',
      headers: [
        { key: 'Strict-Transport-Security', value: 'max-age=63072000; includeSubDomains; preload' },
        { key: 'X-Frame-Options', value: 'SAMEORIGIN' },
        { key: 'X-Themed-By', value: 'SuzuBlog' },
        { key: 'X-Theme-Author', value: 'ZL Asica' },
        { key: 'X-Theme-URL', value: 'https://suzu.zla.app' },
      ],
    }]
  },
  images: {
    formats: ['image/avif', 'image/webp'],
    minimumCacheTTL: 86_400,
    localPatterns: [{
      pathname: '/images/**',
      search: '',
    }],
    remotePatterns: [{
      protocol: 'https',
      hostname: '**',
    }],
  },
  async redirects() {
    return [
      {
        source: String.raw`/:type(rss|atom|rss2)\.:format(\w+)`,
        destination: '/feed.xml',
        permanent: true,
      },
      // ASCII alias for the 2026-08-06 UK AISI post whose slug is full-Chinese.
      // Browsers/feed readers occasionally mangle non-ASCII URL segments,
      // so expose an English permanent alias that won't trip encoders.
      {
        source: '/uk-aisi-agent-incident-report',
        destination: '/uk-aisi-agent-实验事故报告',
        permanent: true,
      },
    ]
  },
}

export default nextConfig
