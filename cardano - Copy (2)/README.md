# Cardano Risk & Compliance Engine

A risk and compliance scoring engine for Cardano blockchain transactions and wallets using the Blockfrost API.

## 🚀 Features

- Transaction risk analysis
- Wallet compliance scoring
- Real-time Cardano blockchain data via Blockfrost
- Modern Next.js frontend with wallet integration
- FastAPI backend with async support

## 📋 Prerequisites

- Python 3.12+
- Node.js 20+
- Blockfrost API key (get one at [blockfrost.io](https://blockfrost.io))

## 🛠️ Local Development

### Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the backend server
uvicorn main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run the development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and start both services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Individual Docker Builds

**Backend:**
```bash
docker build -t cardano-backend .
docker run -p 8000:8000 cardano-backend
```

**Frontend:**
```bash
cd frontend
docker build -t cardano-frontend .
docker run -p 3000:3000 cardano-frontend
```

## 🚢 Deployment Options

### Option 1: Vercel (Frontend) + Railway/Render (Backend)

1. **Frontend on Vercel:**
   - Connect your GitHub repository to Vercel
   - Set root directory to `frontend`
   - Add environment variable: `NEXT_PUBLIC_API_URL=<your-backend-url>`
   - Deploy

2. **Backend on Railway:**
   - Connect your GitHub repository
   - Add environment variable: `BLOCKFROST_API_KEY=<your-key>`
   - Deploy from root directory

### Option 2: Docker on Cloud Platforms

**Google Cloud Run:**
```bash
# Backend
gcloud run deploy cardano-backend --source . --platform managed

# Frontend
cd frontend
gcloud run deploy cardano-frontend --source . --platform managed
```

**AWS ECS/Fargate:**
- Push images to ECR
- Create task definitions for both services
- Deploy to ECS cluster

### Option 3: Kubernetes

```bash
# Build and push images
docker build -t your-registry/cardano-backend:latest .
docker build -t your-registry/cardano-frontend:latest ./frontend

docker push your-registry/cardano-backend:latest
docker push your-registry/cardano-frontend:latest

# Apply Kubernetes manifests
kubectl apply -f k8s/
```

## 🔑 Environment Variables

### Backend
- `BLOCKFROST_API_KEY` - Your Blockfrost API key
- `PORT` - Server port (default: 8000)
- `ENVIRONMENT` - Environment name (development/production)

### Frontend
- `NEXT_PUBLIC_API_URL` - Backend API URL

## 📝 GitHub Actions CI/CD

The repository includes a GitHub Actions workflow that:
- Tests backend and frontend on every push
- Lints code for quality
- Builds Docker images
- Deploys to production on main branch

### Required GitHub Secrets

For automated deployment, add these secrets to your GitHub repository:

**For Vercel (Frontend):**
- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`

**For Railway (Backend):**
- `RAILWAY_TOKEN`

**For Docker Hub:**
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

**Environment Variables:**
- `NEXT_PUBLIC_API_URL` - Your deployed backend URL
- `BLOCKFROST_API_KEY` - Your Blockfrost API key

## 🧪 Testing

### Backend Tests
```bash
pip install pytest pytest-asyncio
pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
npm run lint
npm run build  # Validates build
```

## 📚 API Documentation

Once the backend is running, visit:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### Key Endpoints

- `GET /health` - Health check
- `GET /api/test` - Test endpoint
- `POST /api/analyzeTransaction` - Analyze a transaction
- `POST /api/analyzeWallet` - Analyze a wallet

## 🏗️ Project Structure

```
.
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── Dockerfile             # Backend Docker config
├── docker-compose.yml     # Multi-container orchestration
├── .github/
│   └── workflows/
│       └── deploy.yml     # CI/CD pipeline
├── routes/                # API routes
├── schemas/               # Pydantic models
├── services/              # Business logic
└── frontend/
    ├── pages/            # Next.js pages
    ├── components/       # React components
    ├── styles/           # CSS styles
    ├── Dockerfile        # Frontend Docker config
    └── package.json      # Node dependencies
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🔗 Links

- [Blockfrost API Documentation](https://docs.blockfrost.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
