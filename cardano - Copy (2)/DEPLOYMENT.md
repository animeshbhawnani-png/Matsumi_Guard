# Deployment Configuration Guide

## GitHub Secrets Setup

To enable automated deployment, add the following secrets to your GitHub repository:
Settings → Secrets and variables → Actions → New repository secret

### Required Secrets

#### For Vercel Deployment (Frontend)
1. `VERCEL_TOKEN` - Your Vercel API token
   - Get it from: https://vercel.com/account/tokens
   
2. `VERCEL_ORG_ID` - Your Vercel organization ID
   - Run: `vercel --token=YOUR_TOKEN` in your frontend directory
   - Copy the org ID from .vercel/project.json
   
3. `VERCEL_PROJECT_ID` - Your Vercel project ID
   - Same as above, copy project ID from .vercel/project.json

#### For Railway Deployment (Backend)
1. `RAILWAY_TOKEN` - Your Railway API token
   - Get it from: Railway Dashboard → Account → Tokens
   
2. `BLOCKFROST_API_KEY` - Your Blockfrost API key
   - Get it from: https://blockfrost.io

#### For Docker Hub (Optional)
1. `DOCKER_USERNAME` - Your Docker Hub username
2. `DOCKER_PASSWORD` - Your Docker Hub password or access token

#### For Render Deployment (Alternative Backend)
1. `RENDER_DEPLOY_HOOK_BACKEND` - Your Render deploy hook URL
   - Get it from: Render Dashboard → Your Service → Settings → Deploy Hook

### Environment Variables

Add these as GitHub Actions secrets:

1. `NEXT_PUBLIC_API_URL` - Your deployed backend URL
   - Example: `https://your-app.railway.app`

## Alternative Deployment Platforms

### 1. Render (Best Railway Alternative)

**Free Tier: 750 hours/month**

**Pros:**
- Very similar to Railway
- Auto-deploys from GitHub
- No credit card needed
- Great performance

**Deploy Backend:**
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Runtime: Python
5. Build command: `pip install -r requirements.txt`
6. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Add environment: `BLOCKFROST_API_KEY=your_key`
8. Deploy

### 2. Fly.io (Generous Free Tier)

**Free: 3 shared CPU VMs, 3GB storage**

**Pros:**
- Excellent for production
- Global network
- Simple CLI setup
- Great documentation

**Deploy Backend:**
```bash
curl -L https://fly.io/install.sh | sh
flyctl auth login
flyctl launch
# Answer prompts: choose region, set app name
flyctl secrets set BLOCKFROST_API_KEY=your_key
flyctl deploy
```

### 3. Google Cloud Run (Excellent Free Tier)

**Free: 2 million requests/month, 360,000 GB-seconds**

**Pros:**
- Pay-as-you-go
- Auto-scaling
- Excellent performance
- Simple deployment

**Deploy Backend:**
```bash
# Install Google Cloud SDK
# https://cloud.google.com/sdk/docs/install

gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Build and deploy
gcloud run deploy cardano-backend \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars BLOCKFROST_API_KEY=your_key
```

### 4. Azure Container Instances

**Free: $200 credit for 30 days**

**Pros:**
- Pay-as-you-go model
- Generous free tier
- Good for testing
- Integration with Azure services

**Deploy Backend:**
```bash
# Install Azure CLI
az login
az group create --name cardano-rg --location eastus

# Build container
az acr build --registry YOUR_ACR_NAME --image cardano-backend .

# Deploy
az container create \
  --resource-group cardano-rg \
  --name cardano-backend \
  --image YOUR_ACR_NAME.azurecr.io/cardano-backend:latest \
  --environment-variables BLOCKFROST_API_KEY=your_key \
  --ports 8000
```

### 5. PythonAnywhere (Python-Specific)

**Free: 512MB RAM, limited CPU**

**Pros:**
- Python-specific platform
- Web-based development
- Easy for beginners
- Free tier available

**Deploy:**
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for free account
3. Upload code or clone from GitHub
4. Configure WSGI application
5. Set environment variables
6. Enable web app

### Option 1: Netlify (Frontend) + Render (Backend)

**Netlify Secrets:**
- `NETLIFY_AUTH_TOKEN` - From Netlify User Settings → Applications
- `NETLIFY_SITE_ID` - From Site Settings → General

**Render:**
- Use the deploy hook method (no CLI token needed)
- Add `RENDER_DEPLOY_HOOK_BACKEND` secret

### Option 2: All Docker-based

**For any cloud provider (AWS, GCP, Azure, DigitalOcean):**
- Push to Docker Hub
- Pull and deploy from your cloud provider

### Option 3: Railway for Both

```yaml
# Add to deploy.yml in the Railway sections
- name: Deploy Backend to Railway
  run: railway up --service backend
  env:
    RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}

- name: Deploy Frontend to Railway
  run: railway up --service frontend
  env:
    RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
```

## Manual Deployment Commands

### Deploy to Vercel (Frontend)
```bash
cd frontend
npm install -g vercel
vercel login
vercel --prod
```

### Deploy to Railway (Backend)
```bash
npm install -g @railway/cli
railway login
railway link
railway up
```

### Deploy to Render
- Connect your GitHub repository
- Configure build command: `pip install -r requirements.txt`
- Configure start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Deploy to Heroku
```bash
# Backend
heroku create your-app-backend
heroku stack:set container
git push heroku main

# Frontend
cd frontend
heroku create your-app-frontend
heroku stack:set container
git push heroku main
```

## Docker Compose for Production

```bash
# On your server
git clone your-repo
cd your-repo
cp .env.example .env
# Edit .env with your API keys
docker-compose up -d
```

## Monitoring and Logs

### Railway
```bash
railway logs
```

### Vercel
```bash
vercel logs
```

### Docker
```bash
docker-compose logs -f
```

## Updating Deployments

The GitHub Actions workflow automatically deploys when you push to the `main` branch.

To deploy manually:
```bash
git add .
git commit -m "Your changes"
git push origin main
```

## Troubleshooting

### Build Fails
- Check that all secrets are properly set
- Verify environment variables are correct
- Check GitHub Actions logs for specific errors

### Frontend Can't Connect to Backend
- Verify `NEXT_PUBLIC_API_URL` is set correctly
- Check CORS settings in backend
- Ensure both services are running

### Docker Build Issues
- Increase Docker build memory if needed
- Check Dockerfile syntax
- Verify all paths are correct
