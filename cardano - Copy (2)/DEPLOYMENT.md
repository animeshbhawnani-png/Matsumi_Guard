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
