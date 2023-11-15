from fastapi import Header, HTTPException, Depends


async def verify_headers(
        x_signature_key: str = Header(
            ...,
            alias = "X-Signature-Key",
            description = "The signature key needed for validating from where we are receiving requests" 
        ),
    ):

    signature_key = x_signature_key

    # Verificamos que exista el signature en el header
    if not signature_key:
        raise HTTPException(status_code=400, detail="X-Signature-Key header missing")

    