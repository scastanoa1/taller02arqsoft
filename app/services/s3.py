import os
import boto3

BUCKET = os.getenv("S3_BUCKET", "")
REGION = os.getenv("AWS_REGION", "us-east-2")
USE_PRESIGNED = os.getenv("USE_PRESIGNED", "false").lower() == "true"

def _public_url(key: str) -> str:
    return f"https://{BUCKET}.s3.{REGION}.amazonaws.com/{key}"

def _presigned_url(key: str, expires: int = 3600) -> str:
    s3 = boto3.client("s3", region_name=REGION)
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET, "Key": key},
        ExpiresIn=expires,
    )

def url_for_key(key: str) -> str:
    if not BUCKET:
        raise RuntimeError("S3_BUCKET no configurado")
    return _presigned_url(key) if USE_PRESIGNED else _public_url(key)
