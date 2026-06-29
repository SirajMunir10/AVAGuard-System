import json
from ai_ops.safety import scrub_payload

sample_evidence = {
    "finding_title": "Database connection string exposed in config",
    "details": {
        "description": "Found a hardcoded connection string.",
        "config_file": "db-prod.env",
        "affected_host": "db01.internal.corp",
        "private_ip": "10.0.5.21",
        "public_ip": "203.0.113.45",
        "arn": "arn:aws:iam::123456789012:role/ProductionDatabaseAccess",
        "uuid": "550e8400-e29b-41d4-a716-446655440000",
        "secrets": {
            "db_conn": "postgres://user:supersecret123!@10.0.5.21:5432/maindb",
            "aws_key": "AKIAIOSFODNN7EXAMPLE",
            "api_token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwi"
        },
        "network_context": {
            "source_ip": "10.0.5.21",
            "destination_ip": "10.0.5.22",
            "proxy_host": "proxy.internal.corp",
            "api_host": "api.production.internal.corp",
            "external_request_from": "198.51.100.77"
        }
    }
}

print("=== ORIGINAL EVIDENCE ===")
print(json.dumps(sample_evidence, indent=2))

print("\n=== SCRUBBED EVIDENCE ===")
scrubbed = scrub_payload(sample_evidence)
print(json.dumps(scrubbed, indent=2))
