from fastapi import Header, HTTPException, Depends
import jwt, os
from cryptography.hazmat.primitives import serialization

from dotenv import load_dotenv
load_dotenv()

PASSPHRASE_1 = os.getenv('PASSPHRASE_1')
PASSPHRASE_2 = os.getenv('PASSPHRASE_2')

async def verify_headers_students(
        Authorization: str = Header(
            ...,
            alias = "Authorization",
            description = "The signature key needed for validating from where we are receiving requests" 
        ),
        Student_ID: str = Header(
            ...,
            alias = "Student-ID",
            description= "We need the student-id to verify if the Authorization token is valid"
        )
):

    token = Authorization
    student_id = Student_ID

    # Verificamos que exista el signature en el header
    if not token or not student_id:
        raise HTTPException(status_code=400, detail="Header verification is missing parameters")
    
    # Recogemos el public key
    dir_path = os.path.dirname(os.path.realpath(__file__))
    public_key_path = os.path.join(dir_path, "..", "..", "..", "certs", "public.pem")
    
    with open(public_key_path, 'r') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    try:
        token_decoded = jwt.decode(token, public_key, algorithms=['RS256'])
        if str(token_decoded['student_id']) != student_id:
            raise HTTPException(status_code=403, detail="Student ID does not match token")

        return token_decoded

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

    

async def verfiy_headers_admin(
        Authorization: str = Header(
            ...,
            alias = "Authorization",
            description = "The signature key needed for validating from where we are receiving requests" 
        ),
        Admin_Pass: str = Header(
            ...,
            alias = "Admin_Pass",
            description= "We need the student-id to verify if the Authorization token is valid"
        )
):
    token = Authorization
    admin_pass = Admin_Pass

    # Verificamos que exista el signature en el header
    if not token or not admin_pass:
        raise HTTPException(status_code=400, detail="Header verification is missing parameters")
    
    # Recogemos el public key
    dir_path = os.path.dirname(os.path.realpath(__file__))
    public_key_path = os.path.join(dir_path, "..", "..", "..", "certs", "public.pem")
    
    with open(public_key_path, 'r') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    try:
        token_decoded = jwt.decode(token, public_key, algorithms=['RS256'])
        if str(token_decoded['admin_pass']) != admin_pass:
            raise HTTPException(status_code=403, detail="Admin Pass does not match token")

        return token_decoded

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")
    