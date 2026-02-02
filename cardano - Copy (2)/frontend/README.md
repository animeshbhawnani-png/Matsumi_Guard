# Cardano Compliance Dashboard - Frontend

A modern Next.js frontend for the Cardano Risk & Compliance Engine.

## 🚀 Quick Start

### Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000)

### Production Build

```bash
# Build for production
npm run build

# Start production server
npm start
```

## 🔧 Configuration

### Environment Variables

Create a `.env.local` file:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

For production, set this to your deployed backend URL.

## 📦 Dependencies

- **Next.js 14** - React framework
- **React 18** - UI library
- **Axios** - HTTP client
- **Tailwind CSS** - Styling
- **ESLint** - Code linting

## 🏗️ Project Structure

```
frontend/
├── components/
│   └── WalletConnector.jsx    # Cardano wallet integration
├── pages/
│   ├── _app.js                # App wrapper
│   └── index.js               # Main dashboard
├── styles/
│   └── globals.css            # Global styles
├── public/                    # Static assets
├── next.config.mjs            # Next.js configuration
├── tailwind.config.js         # Tailwind configuration
└── package.json               # Dependencies
```

## 🎨 Features

- 📊 Transaction risk analysis UI
- 👛 Cardano wallet integration (Nami, Eternl)
- 🎯 Real-time compliance scoring
- 📱 Responsive design
- 🌙 Modern dark theme

## 🐳 Docker

```bash
# Build
docker build -t cardano-frontend .

# Run
docker run -p 3000:3000 -e NEXT_PUBLIC_API_URL=http://backend:8000 cardano-frontend
```

## 🚢 Deployment

### Vercel (Recommended)

1. Import repository on [Vercel](https://vercel.com)
2. Set root directory to `frontend`
3. Add environment variable: `NEXT_PUBLIC_API_URL`
4. Deploy

### Netlify

```bash
npm install -g netlify-cli
netlify deploy --prod --dir=.next
```

### Other Platforms

The frontend can be deployed to any platform that supports Next.js:
- Railway
- Render
- AWS Amplify
- Google Cloud Run
- Azure Static Web Apps

## 🧪 Testing

```bash
# Lint
npm run lint

# Build test
npm run build
```

## 🔗 API Integration

The frontend connects to the backend API at `NEXT_PUBLIC_API_URL`.

### Key Endpoints Used

- `POST /api/analyzeTransaction` - Analyze transactions
- `POST /api/analyzeWallet` - Analyze wallets
- `GET /health` - Health check

## 🎯 Supported Wallets

- Nami Wallet
- Eternl Wallet
- More wallets can be added via cardano-serialization-lib

## 📚 Learn More

- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Cardano Documentation](https://docs.cardano.org/)

## 🤝 Contributing

Contributions are welcome! Please read the main [README](../README.md) for guidelines.

## 📄 License

MIT License - See [LICENSE](../LICENSE) for details.
