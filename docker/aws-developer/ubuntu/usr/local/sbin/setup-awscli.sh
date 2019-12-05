#!/bin/bash

sed -i -e "s/region = us-east-1/region = $AWS_REGION/g" /root/.aws/config
sed -i -e "s/aws_access_key_id = NONE/aws_access_key_id = $AWS_ACCESS_KEY/g" /root/.aws/credentials
sed -i -e "s/aws_secret_access_key = NONE/aws_secret_access_key = $AWS_SECRET_KEY/g" /root/.aws/credentials

exit 0