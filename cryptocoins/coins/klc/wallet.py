from django.db import transaction
from web3signer_service import Web3SignerService
from aws_kms_service import AwsKmsService
from core.models.cryptocoins import UserWallet
from django.conf import settings
from web3 import Web3

class TransactionController:
    def __init__(self, web3signer_url):
        self.web3signer_service = Web3SignerService(web3signer_url)

    def create_klc_address(self):
        # Initialize the AWS KMS service
        aws_kms_service = AwsKmsService(endpoint_url=settings.AWS_KMS_ENDPOINT)

        # Create a new key using the AWS KMS service
        try:
            key_id = aws_kms_service.create_new_key()
        except Exception as e:
            # Log the exception and re-raise
            print(f"Failed to create new key: {e}")
            raise

        # Initialize the Web3Signer service
        web3signer_service = Web3SignerService(key_id=key_id)

        # Create a new address using the Web3Signer service
        address = web3signer_service.create_new_address()

        # Encrypt the private key using the AWS KMS service
        encrypted_key = aws_kms_service.encrypt_key(web3signer_service.get_private_key())

        return address, encrypted_key

    def create_transaction(self, transaction, key_id):
        from_address = transaction['from']
        to_address = transaction['to']
        gas = transaction['gas']
        gas_price = transaction['gasPrice']
        value = transaction['value']
        signed_transaction = self.web3signer_service.sign_transaction(from_address, to_address, gas, gas_price, value, key_id)
        # Use the signed_transaction to send the transaction

    @transaction.atomic
    def get_or_create_klc_wallet(self, user_id, is_new=False):
        klc_wallet = UserWallet.objects.filter(
            user_id=user_id,
            currency='KLC',
            blockchain_currency='KLC',
        ).first()

        if not is_new and klc_wallet is not None:
            return klc_wallet

        aws_kms_service = AwsKmsService()
        key_id = aws_kms_service.create_new_key()
        # Use the key_id to create a new KLC wallet
        # Return the wallet

    def is_valid_klc_address(self, address):
        return Web3.is_address(address)

    def klc_wallet_creation_wrapper(self, user_id, is_new=False):
        wallet = self.get_or_create_klc_wallet(user_id, is_new=is_new)
        return UserWallet.objects.filter(id=wallet.id)
    
    @transaction.atomic
    def create_krc20_address(self, user_id, token_name, is_new=False):
        krc20_wallet = UserWallet.objects.filter(
            user_id=user_id,
            currency=token_name,
            blockchain_currency='KLC',
        ).first()

        if not is_new and krc20_wallet is not None:
            return krc20_wallet

        aws_kms_service = AwsKmsService()
        key_id = aws_kms_service.create_new_key()
        # Use the key_id to create a new KRC20 wallet
        # Return the wallet