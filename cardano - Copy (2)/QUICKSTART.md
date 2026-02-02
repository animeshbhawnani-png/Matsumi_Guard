# Quick Start Guide

## 🚀 Deploy to Production in 5 Minutes

### Method 1: Vercel + Railway (Recommended)

#### Step 1: Deploy Backend to Railway
1. Go to [Railway](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select this repository
4. Railway will auto-detect the Python app
5. Add environment variable: `BLOCKFROST_API_KEY=your_key`
6. Copy the deployment URL (e.g., `https://your-app.up.railway.app`)

#### Step 2: Deploy Frontend to Vercel
1. Go to [Vercel](https://vercel.com)
2. Click "Import Project" → Select this repository
3. Set **Root Directory** to `frontend`
4. Add environment variable: `NEXT_PUBLIC_API_URL=<railway-backend-url>`
5. Click Deploy

✅ Done! Your app is now live.

---

### Method 1a: Vercel + Render (Alternative)

#### Step 1: Deploy Backend to Render
1. Go to [Render](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Render will auto-detect Python
5. Add environment variable: `BLOCKFROST_API_KEY=your_key`
6. Deploy (copy your backend URL)

#### Step 2: Deploy Frontend to Vercel
(Same as Method 1, Step 2 above)

---

### Method 1b: Vercel + Fly.io (Alternative)

#### Step 1: Deploy Backend to Fly.io
1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Login: `flyctl auth login`
3. Deploy: `flyctl launch` (in project root)
4. Set secrets: `flyctl secrets set BLOCKFROST_API_KEY=your_key`
5. Deploy: `flyctl deploy`
6. Get URL: `flyctl open` (shows your backend URL)

#### Step 2: Deploy Frontend to Vercel
(Same as Method 1, Step 2 above)

---

### Method 1c: Netlify + Render (Full Netlify Stack)

#### Step 1: Deploy Backend to Render
(See Method 1a, Step 1 above)

#### Step 2: Deploy Frontend to Netlify
1. Go to [Netlify](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect your GitHub repository
4. Select `frontend` folder as base directory
5. Build command: `npm run build`
6. Publish directory: `.next`
7. Add environment: `NEXT_PUBLIC_API_URL=<render-backend-url>`
8. Deploy

---

### Method 2: Docker Compose on Any VPS

```bash
# On your server (Ubuntu/Debian)
git clone <your-repo>
cd cardano-risk-engine

# Create environment file
cp .env.example .env
nano .env  # Add your BLOCKFROST_API_KEY

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Start the application
docker-compose up -d

# Check status
docker-compose ps
```

Access at: `http://your-server-ip:3000`

---

### Method 3: GitHub Actions Auto-Deploy

With GitHub Actions, you can automatically deploy to your preferred platform (Vercel, Netlify, Railway, Render, etc.).

---

## 🔧 Local Development

### Prerequisites
- Python 3.12+
- Node.js 20+
- npm or yarn

### Quick Start

**Terminal 1 - Backend:**
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Visit: `http://localhost:3000`

---

## 🐳 Docker Quick Start

```bash
# Build and run everything
docker-compose up

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop everything
docker-compose down
```

---

## 🔑 Get Your Blockfrost API Key

1. Go to [blockfrost.io](https://blockfrost.io)
2. Sign up (free tier available)
3. Create a new project
4. Copy your API key
5. Add to `.env` file or deployment platform

---

## 📊 Platform Comparison

| Platform | Frontend | Backend | Cost | Setup Time | Ease |
|----------|----------|---------|------|------------|------|
| Vercel + Railway | ✅ | ✅ | Free tier | 5 min | ⭐⭐⭐⭐⭐ |
| Vercel + Render | ✅ | ✅ | Free tier | 5 min | ⭐⭐⭐⭐⭐ |
| Vercel + Fly.io | ✅ | ✅ | Free tier | 5 min | ⭐⭐⭐⭐ |
| Netlify + Render | ✅ | ✅ | Free tier | 5 min | ⭐⭐⭐⭐ |
| Docker on VPS | ✅ | ✅ | $5/mo | 10 min | ⭐⭐⭐ |
| Google Cloud Run | ✅ | ✅ | Free tier | 15 min | ⭐⭐⭐ |
| AWS/GCP/Azure | ✅ | ✅ | Variable | 30 min | ⭐⭐ |

---

## 🆘 Troubleshooting

### Frontend can't connect to backend
- Check `NEXT_PUBLIC_API_URL` is correct
- Verify backend is running: `curl http://backend-url/health`
- Check CORS settings in `main.py`

### Backend won't start
- Verify Python version: `python --version` (need 3.12+)
- Check all dependencies installed: `pip install -r requirements.txt`
- Verify Blockfrost API key is set

### Docker issues
- Increase Docker memory to 4GB+
- Clear cache: `docker system prune -a`
- Rebuild: `docker-compose build --no-cache`

### Tests failing
- Install test deps: `pip install pytest pytest-asyncio`
- Run: `pytest tests/ -v`

---

## 📱 Next Steps

After deployment:
1. Test the health endpoint: `GET /health`
2. Test a transaction analysis
3. Connect a Cardano wallet (Nami/Eternl)
4. Monitor logs for errors
5. Set up monitoring (optional)

---

## 🔗 Useful Links

- [Full Deployment Guide](./DEPLOYMENT.md)
- [API Documentation](http://localhost:8000/docs) (when running)
- [Blockfrost API Docs](https://docs.blockfrost.io/)
- [Railway Docs](https://docs.railway.app/)
- [Vercel Docs](https://vercel.com/docs)

---

## 💡 Pro Tips

1. **Use environment variables** - Never commit API keys
2. **Monitor your usage** - Blockfrost free tier has limits
3. **Enable logging** - Helps debug production issues
4. **Use Docker** - Consistent across all environments
5. **Set up alerts** - Know when things break

---

Need help? Check the [README.md](./README.md) for detailed documentation.
