# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T10:32:27+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity
from fastapi import Path, Query

from models import (
    AddRequestResponse,
    AgeUsdExchangeInfo,
    AgeUsdInfo,
    CheckResponse,
    CreatePaymentRequest,
    ErgoPayResponse,
    FetchActionResponse,
    MosaikApp,
    MosaikBabelfeeNewofferDoitPostRequest,
    MosaikBabelfeeNewofferNewInputPostRequest,
    MosaikTokenburnPreparePostRequest,
    NotificationCheckResponse,
    PaymentRequestStateResponse,
    PeersListGetResponse,
    TokenPrice,
    TokensListBlockedGetResponse,
    TokensListGenuineGetResponse,
    TokensPricesAllGetResponse,
)

app = MCPProxy(
    description='Please see usage policies on tokenjay.app',
    termsOfService='https://tokenjay.app/apidoc.html',
    title='TokenJay API services',
    version='1.0.0',
    servers=[{'url': 'https://api.tokenjay.app/'}],
)


@app.get('/ageusd/info', tags=['age_usd_status'])
def get_age_usd_info():
    """
    Returns state of AgeUSD at this moment
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/cancelbabel/{boxId}', tags=['babel_box_management'])
def ergo_pay_create_babel_box_1(box_id: str = Path(..., alias='boxId')):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/createbabel/{address}', tags=['currency_exchange_processes', 'transaction_setup']
)
def ergo_pay_create_babel_box(
    address: str,
    token_id: str = Query(..., alias='tokenId'),
    erg_amount: int = Query(..., alias='ergAmount'),
    token_amount: int = Query(..., alias='tokenAmount'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/mosaik/babelfee/')
def get_babel_fee_overview():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/mosaik/babelfee/newoffer',
    tags=[
        'babel_box_management',
        'payment_request_operations',
        'currency_exchange_processes',
        'token_verification',
        'transaction_setup',
        'peer_information_management',
        'notification_checking',
        'age_usd_status',
    ],
)
def get_babel_fee_new_offer():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/mosaik/babelfee/newoffer/doit',
    tags=['babel_box_management', 'payment_request_operations'],
)
def do_create_babel_box(body: MosaikBabelfeeNewofferDoitPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/mosaik/babelfee/newoffer/new-input',
    tags=['babel_box_management', 'payment_request_operations'],
)
def replace_token_amount_input_fields(body: MosaikBabelfeeNewofferNewInputPostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/mosaik/babelfee/notificationcheck', tags=['notification_checking'])
def check_for_notifications():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/mosaik/boxconsolidation/', tags=['notification_checking'])
def main_app_1():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/mosaik/boxconsolidation/consolidate/{p2pkaddress}', tags=['token_verification']
)
def ep_consolidate(p2pkaddress: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/mosaik/tokenburn', tags=['notification_checking'])
def main_app():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/mosaik/tokenburn/get/{uuid}', tags=['token_verification'])
def get_burning_transaction(uuid: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post('/mosaik/tokenburn/prepare', tags=['transaction_setup', 'token_verification'])
def prepare_transaction(body: MosaikTokenburnPreparePostRequest):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post('/payment/addrequest', tags=['payment_request_operations'])
def add_payment_request(body: CreatePaymentRequest):
    """
    Creates a new payment request. Will return request id to check for transaction state and ergopay url to show the user as QR code
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/payment/state/{requestId}', tags=['payment_request_operations'])
def get_payment_state(request_id: str = Path(..., alias='requestId')):
    """
    Returns the state of a payment request. Please note that payment requests are purged after some time, so persist the state at your side when needed
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/peers/list', tags=['peer_information_management'])
def get_peers_list(
    unreachable: Optional[bool] = False,
    closed_api: Optional[bool] = Query(False, alias='closedApi'),
    limit: Optional[int] = 50,
):
    """
    Lists known peers sorted by block height
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sigrsv/exchange/',
    tags=[
        'payment_request_operations',
        'currency_exchange_processes',
        'transaction_setup',
    ],
)
def do_sigma_rsv_exchange(
    amount: int,
    address: str = ...,
    check_rate: Optional[int] = Query(0, alias='checkRate'),
    execution_fee: Optional[int] = Query(0, alias='executionFee'),
):
    """
    Builds ErgoPayRequest for SigRSV exchange
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/sigrsv/exchange/{amount}/info', tags=['currency_exchange_processes'])
def calc_sigma_rsv_exchange(amount: int):
    """
    Calculates SigRSV exchange
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/sigrsv/price', tags=['token_verification', 'currency_exchange_processes'])
def get_sigma_rsv_price():
    """
    Lists price and available volume for SigmaRSV
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/sigusd/exchange/',
    tags=['payment_request_operations', 'currency_exchange_processes'],
)
def do_sigma_usd_exchange(
    amount: int,
    address: str = ...,
    check_rate: Optional[int] = Query(0, alias='checkRate'),
    execution_fee: Optional[int] = Query(0, alias='executionFee'),
):
    """
    Builds ErgoPayRequest for SigUSD exchange
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/sigusd/exchange/{amount}/info', tags=['currency_exchange_processes'])
def calc_sigma_usd_exchange(amount: int):
    """
    Calculates SigUSD exchange
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/sigusd/price', tags=['currency_exchange_processes', 'token_verification'])
def get_sigma_usd_price():
    """
    Lists price and available volume for SigmaUSD
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/tokens/check/{tokenId}/{tokenName}', tags=['token_verification'])
def check_token(
    token_id: str = Path(..., alias='tokenId'),
    token_name: str = Path(..., alias='tokenName'),
):
    """
    Check a token verification
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/tokens/listBlocked', tags=['token_verification'])
def list_blocked():
    """
    Lists all blocked tokens
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/tokens/listGenuine', tags=['token_verification'])
def list_genuine():
    """
    Lists all genuine tokens known
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/tokens/prices/all', tags=['currency_exchange_processes', 'token_verification']
)
def get_token_prices():
    """
    Lists all token prices and available volume
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/tokens/prices/{tokenId}',
    tags=['token_verification', 'currency_exchange_processes'],
)
def get_token_price(token_id: str = Path(..., alias='tokenId')):
    """
    Lists price and available volume for a certain token
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
