'''
pyburstlib
:author: drownedcoast
:date: 4-26-2018
'''
from pyburstlib.wallet_api.models.base import BaseModel

class AccountRS(BaseModel):
    def __init__(
            self,
            accountRS=None,
            requestProcessingTime=None,
            account=None):
        self.accountRS = accountRS
        self.requestProcessingTime = requestProcessingTime
        self.account = account

class AccountLong(BaseModel):
    def __init__(
            self,
            stringId=None,
            requestProcessingTime=None,
            longId=None):
        self.stringId = stringId
        self.requestProcessingTime = requestProcessingTime
        self.longId = longId

# TODO: Actually test this at some point
class SignTransaction(BaseModel):
    def __init__(
            self,
            requestProcessingTime=None,
            transaction=None,
            fullHash=None,
            transactionBytes=None,
            signatureHash=None,
            verify=None):
        self.transaction = transaction
        self.fullHash = fullHash
        self.transactionBytes = transactionBytes
        self.signatureHash = signatureHash
        self.verify = verify
        self.requestProcessingTime = requestProcessingTime
    
class BroadcastTransaction(BaseModel):
    def __init__(
            self,
            requestProcessingTime=None,
            numberPeersSentTo=None,
            transaction=None,
            fullHash=None,):
        self.numberPeersSentTo = numberPeersSentTo
        self.transaction = transaction
        self.fullHash = fullHash
        self.requestProcessingTime = requestProcessingTime

class ParseTransaction(BaseModel):
    def __init__(
            self,
            requestProcessingTime=None,
            type=None,
            subtype=None,
            timestamp=None,
            deadline=None,
            senderPublicKey=None,
            recipient=None,
            recipientRS=None,
            amountNQT=None,
            feeNQT=None,
            signature=None,
            signatureHash=None,
            fullHash=None,
            transaction=None,
            attachment={
                "version.Message": None,
                "message": None,
                "messageIsText": None
            },
            attachmentBytes=None,
            sender=None,
            senderRS=None,
            height=None,
            version=None,
            ecBlockId=None,
            ecBlockHeight=None,
            cashBackId=None,
            block=None,
            confirmations=None,
            blockTimestamp=None):            
        self.requestProcessingTime = requestProcessingTime
        self.type = type
        self.subtype = subtype
        self.timestamp = timestamp
        self.deadline = deadline
        self.senderPublicKey = senderPublicKey
        self.recipient = recipient
        self.recipientRS = recipientRS
        self.amountNQT = amountNQT
        self.feeNQT = feeNQT
        self.signature = signature
        self.signatureHash = signatureHash
        self.fullHash = fullHash
        self.transaction = transaction
        self.attachment = attachment
        self.attachmentBytes = attachmentBytes
        self.sender = sender
        self.senderRS = senderRS
        self.height = height
        self.version = version
        self.ecBlockId = ecBlockId
        self.ecBlockHeight = ecBlockHeight
        self.cashBackId = cashBackId
        self.block = block
        self.confirmations = confirmations
        self.blockTimestamp = blockTimestamp

class SuggestFee(BaseModel):
    def __init__(
            self,
            requestProcessingTime=None,
            cheap=None,
            standard=None,
            priority=None):
        self.requestProcessingTime = requestProcessingTime
        self.cheap = cheap
        self.standard = standard
        self.priority = priority