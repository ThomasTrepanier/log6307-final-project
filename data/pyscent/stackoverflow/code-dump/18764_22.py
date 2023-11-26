class MtnPayer(BaseModel):
  partyIdType: str
  partyId: str

class MtnPayment(BaseModel):
  financialTransactionId: str
  externalId: str
  amount: str
  currency: str
  payer: MtnPayer
  payerMessage: str
  payeeNote: str
  status: str
  reason: str
