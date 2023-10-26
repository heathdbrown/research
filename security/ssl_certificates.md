# make a valid certificate from a single line in bash

```bash
(
  echo "-----BEGIN CERTIFICATE-----"; 
  echo $CERTIFICATE | sed -e "s/.\{67\}/&\n/g"; 
  echo "-----END CERTIFICATE-----";
) > certificate.pem
```
