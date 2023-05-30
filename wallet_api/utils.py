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

    ''' TODO: signTransaction, POST, 
    * unsignedTransactionBytes
    unsignedTransactionJSON
    secretPhrase
    200: {
    "transaction": "17286979857310322585",
    "fullHash": "998f500297b0e7ef9e4e1c18ac7921c74d76a1aabded8c36972896f8d444a2b5",
    "transactionBytes": "00203c3af80e1800c213e4144ba84af94aae2458308fae1f0cb0838...",
    "signatureHash": "a645cb3cc93176dda1b9bc172c53449dc42b2c27100b5754f70c1eb84b491230",
    "verify": true
    }'''
    
    ''' TODO: broadcastTransaction, POST 
    * transactionBytes
    transactionTransactionJSON
    200: {
    "numberPeersSentTo": 15,
    "transaction": "17286979857310322585",
    "fullHash": "998f500297b0e7ef9e4e1c18ac7921c74d76a1aabded8c36972896f8d444a2b5"
    }'''
    
    ''' TODO: parseTransaction, POST 
    * transactionBytes
    200: {
    "type": 1,
    "subtype": 0,
    "timestamp": 251047549,
    "deadline": 24,
    "senderPublicKey": "c213e4144ba84af94aae2458308fae1f0cb083870c8f3012eea58147f3b09d4a",
    "recipient": "6502115112683865257",
    "recipientRS": "TS-K37B-9V85-FB95-793HN",
    "amountNQT": "0",
    "feeNQT": "1000000",
    "signature": "9204b3eca152b72141cdfebbdbfad14c4c79a7f68f04eb5daf7f04a817495f09cca5cf85566ea2b28178702fba7aedae29728af7cd640f5b1e02b8facb21134c",
    "signatureHash": "78c4b094c0b8b1d35c23738a5fabdcabbafd1e73a99a90e3280abf98452d783a",
    "fullHash": "6ce8970b66bf8360108df8d4675c275ab2acd549219928c4d0ae4a62a284b1c7",
    "transaction": "6954612694592252012",
    "attachment": {
    "version.Message": 1,
    "message": "test",
    "messageIsText": true
    },
    "attachmentBytes": "010400008074657374",
    "sender": "2402520554221019656",
    "senderRS": "TS-QAJA-QW5Y-SWVP-4RVP4",
    "height": 2147483647,
    "version": 2,
    "ecBlockId": "7594592439957689464",
    "ecBlockHeight": 442244,
    "cashBackId": "8952122635653861124",
    "block": "13680738303626126726",
    "confirmations": 68148,
    "blockTimestamp": 232452172
    }'''
    
    ''' TODO: suggestFee, GET 
    200: {
    "cheap": 1000000,
    "standard": 2000000,
    "priority": 3000000,
    "requestProcessingTime": 0
    }'''