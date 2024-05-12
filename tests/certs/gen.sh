mkdir out

openssl x509 -inform DER -outform PEM -in pass.cer -out out/signerCert.pem
openssl x509 -inform DER -outform PEM -in wwdr.cer -out out/wwdr.pem

# openssl pkcs12 -in pass.p12 -clcerts -nokeys -out out/signerCert.pem -passin:$1 -legacy
openssl pkcs12 -in pass.p12 -nocerts -out out/signerKey.pem -passin pass:$1 -passout pass:$1 -legacy
