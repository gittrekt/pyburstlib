'''
pyburstlib
:author: drownedcoast
:date: 4-26-2018
'''
from json import loads

from pyburstlib.wallet_api.base import BaseApi
from pyburstlib.wallet_api.models.utils import *
from pyburstlib.constants import BASE_WALLET_PATH

class UtilsApi(BaseApi):

    def rs_convert(self, account_id=None):
        '''
        Converts from numeric id to account address (rs format).

        :param account_id: Numeric ID for the account (required)
        :type account_id: str
        :returns: An instance of :class:`AccountRS`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'rsConvert',
                                           'account': account_id})
        return AccountRS.from_json(response.text)

    def long_convert(self, id=None):
        '''

        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'longConvert',
                                           'id': id})
        return AccountLong.from_json(response.text)

    def sign_transaction(self, unsigned_transaction_bytes=None, secret_phrase=None):
        '''
        Sign a transaction
        :param unsigned_transaction_bytes: Unsigned transaction bytes (required)
        :param secret_phrase: Secret phrase of the account (required)
        
        returns: An instance of :class:`SignTransaction`
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'signTransaction',
                                           'unsignedTransactionBytes': unsigned_transaction_bytes,
                                           'secretPhrase': secret_phrase})
        return SignTransaction.from_json(response.text)
    
    def broadcast_transaction(self, transaction_bytes=None):
        '''
        Broadcast a transaction to the network
        :param transaction_bytes: Transaction bytes (required)
        
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'broadcastTransaction',
                                           'transactionBytes': transaction_bytes})
        return BroadcastTransaction.from_json(response.text)
    
    def parse_transaction(self, transaction_bytes=None):
        '''
        Parse a transaction
        :param transaction_bytes: Transaction bytes (required)
        
        '''
        response = self._client.post(uri=BASE_WALLET_PATH, 
                                   params={'requestType': 'parseTransaction',
                                           'transactionBytes': transaction_bytes})
        return ParseTransaction.from_json(response.text)
    
    def suggest_fee(self):
        response = self._client.get(uri=BASE_WALLET_PATH,
                                    params={'requestType': 'suggestFee'})
        return SuggestFee.from_json(response.text)