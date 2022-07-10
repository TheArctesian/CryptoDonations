#...
InnerTxnBuilder.Begin(),
InnerTxnBuilder.SetFields({
    TxnField.type_enum: TxnType.AssetTransfer,
    TxnField.asset_receiver: Txn.sender(),
    TxnField.asset_amount: Int(1000),
    TxnField.xfer_asset: Txn.assets[0], # Must be in the assets array sent as part of the application call
}),
InnerTxnBuilder.Submit(),
#...

