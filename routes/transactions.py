from fastapi import APIRouter, HTTPException

from schemas.requests import AnalyzeTransactionRequest, AnalyzeWalletRequest
from schemas.responses import AnalyzeTransactionResponse, AnalyzeWalletResponse
from services.risk_engine import analyze_transaction, analyze_wallet


router = APIRouter(tags=["Transactions"])


@router.post("/analyzeTransaction", response_model=AnalyzeTransactionResponse)
async def analyze_transaction_route(payload: AnalyzeTransactionRequest):
    """
    Analyze a Cardano transaction for risk & compliance.
    """
    try:
        result = await analyze_transaction(
            tx_hash=payload.txHash,
            wallet_address=payload.walletAddress,
            metadata=payload.metadata or {},
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing transaction: {str(e)}"
        )


@router.post("/analyzeWallet", response_model=AnalyzeWalletResponse)
async def analyze_wallet_route(payload: AnalyzeWalletRequest):
    """
    Analyze a Cardano wallet for risk & compliance.
    """
    try:
        result = await analyze_wallet(
            wallet_address=payload.walletAddress,
            metadata=payload.metadata or {},
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing wallet: {str(e)}"
        )


