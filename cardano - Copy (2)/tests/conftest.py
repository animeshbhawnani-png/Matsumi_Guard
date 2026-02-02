"""
Test configuration and fixtures
"""
import pytest


@pytest.fixture
def mock_blockfrost_response():
    """Mock Blockfrost API response for testing"""
    return {
        "hash": "test_tx_hash",
        "block": "test_block",
        "block_height": 12345,
        "slot": 67890,
        "index": 0,
        "output_amount": [
            {
                "unit": "lovelace",
                "quantity": "1000000"
            }
        ],
        "fees": "170000",
        "deposit": "0",
        "size": 300,
        "invalid_before": None,
        "invalid_hereafter": "67900",
        "utxo_count": 2,
        "withdrawal_count": 0,
        "mir_cert_count": 0,
        "delegation_count": 0,
        "stake_cert_count": 0,
        "pool_update_count": 0,
        "pool_retire_count": 0,
        "asset_mint_or_burn_count": 0,
        "redeemer_count": 0,
        "valid_contract": True
    }
