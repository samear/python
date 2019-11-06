#!/usr/bin/python
import base64
import random
import time

def encode(str):
   #encoded_result=base64.b64encode(bytes(str, 'utf-8'))
   global encoded_result
   encoded_result=base64.b64encode(bytes(str, 'utf-8'))

   print('encoded:', encoded_result)

def decode(str):
   decoded_result=base64.b64decode(str).decode('utf-8')

   print('decoded:', decoded_result)

#content = '{ "repo:name": "12345","repo:createDate": "2017-09-26T15:52:25Z", "astock:assetType": "template", "components": [{ "astock:profile": "H240", "dc:format": "image/jpeg", "tiff:imageWidth": 427, "tiff:imageLength": 240, "files": [{ "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-va6.s3-us-east-1.amazonaws.com/00/00/01/23/H240_1234.jpg" }, { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-irl1.s3-eu-west-1.amazonaws.com/00/00/01/23/H240_1234.jpg" } ] }, { "astock:profile": "H240", "dc:format": "image/webp", "tiff:imageWidth": 427, "tiff:imageLength": 240, "files": [ { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-va6.s3-us-east-1.amazonaws.com/00/00/01/23/H240_1234.webp" }, { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-irl1.s3-eu-west-1.amazonaws.com/00/00/01/23/H240_1234.webp" }] }, { "astock:profile": "500ST", "dc:format": "image/jpeg", "tiff:imageWidth": 500, "tiff:imageLength": 281, "files": [ { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-va6.s3-us-east-1.amazonaws.com/00/00/01/23/500ST_1234.jpg" } ] }, { "astock:profile": "PREVIEW_W1024", "dc:format": "image/jpeg", "tiff:imageWidth": 1024, "tiff:imageLength": 575, "files": [ { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-va6.s3-us-east-1.amazonaws.com/00/00/01/23/PREVIEW_W1024_1234.jpg" } ] } ], "derivatives": [ { "astock:derivativeType": "rendition", "astock:componentType": "thumbnail", "componentIndexes": [0] }, { "astock:derivativeType": "rendition", "astock:componentType": "thumbnail", "componentIndexes": [1] }, { "astock:derivativeType": "rendition", "astock:componentType": "thumbnail", "componentIndexes": [2] }, { "astock:derivativeType": "rendition", "astock:componentType": "preview", "componentIndexes": [3] } ] }'

for n in range(2):
   t = int(time.time() * 1000)
   r1 = random.randint(0, 10000)
   print('random number:', t + r1)
   
   content = '{ "repo:name": "' + str(t) + str(r1) + ',"repo:createDate": "2017-09-26T15:52:25Z", "astock:assetType": "template", "components": [{ "astock:profile": "H240", "dc:format": "image/jpeg", "tiff:imageWidth": 427, "tiff:imageLength": 240, "files": [{ "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-va6.s3-us-east-1.amazonaws.com/00/00/01/23/H240_1234.jpg" }, { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-irl1.s3-eu-west-1.amazonaws.com/00/00/01/23/H240_1234.jpg" } ] }, { "astock:profile": "H240", "dc:format": "image/webp", "tiff:imageWidth": 427, "tiff:imageLength": 240, "files": [ { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-va6.s3-us-east-1.amazonaws.com/00/00/01/23/H240_1234.webp" }, { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-irl1.s3-eu-west-1.amazonaws.com/00/00/01/23/H240_1234.webp" }] }, { "astock:profile": "500ST", "dc:format": "image/jpeg", "tiff:imageWidth": 500, "tiff:imageLength": 281, "files": [ { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-va6.s3-us-east-1.amazonaws.com/00/00/01/23/500ST_1234.jpg" } ] }, { "astock:profile": "PREVIEW_W1024", "dc:format": "image/jpeg", "tiff:imageWidth": 1024, "tiff:imageLength": 575, "files": [ { "repo:size": 424242, "repo:createDate": "2017-09-26T15:52:25Z", "repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178", "href": "s3://stock-public-thumbnails-stage-va6.s3-us-east-1.amazonaws.com/00/00/01/23/PREVIEW_W1024_1234.jpg" } ] } ], "derivatives": [ { "astock:derivativeType": "rendition", "astock:componentType": "thumbnail", "componentIndexes": [0] }, { "astock:derivativeType": "rendition", "astock:componentType": "thumbnail", "componentIndexes": [1] }, { "astock:derivativeType": "rendition", "astock:componentType": "thumbnail", "componentIndexes": [2] }, { "astock:derivativeType": "rendition", "astock:componentType": "preview", "componentIndexes": [3] } ] }'
   encode(content)
   decode(encoded_result)
