# This python script generate unique name (unique_value) and converts the sting to base64encoded format.
# 
#!/usr/bin/python
import base64
import random
import time

# generate unique value. this value is used for repo:name
def unique_value():
    time.sleep(0.000001)
    r = random.randint(0, 10000)
    return r + time.time()

# convert to base64
def encode_Assets(content):
    global f1
    global encodedStr

    encoded_data = base64.b64encode(content.encode("utf-8"))
    encodedStr = str(encoded_data, "utf-8")
    f1.write(str(encodedStr) + '\n')

def encode_Renditions(content):
    global f2
    global encodedStr

    encoded_data = base64.b64encode(content.encode("utf-8"))
    encodedStr = str(encoded_data, "utf-8")
    f2.write(str(encodedStr) + '\n')

# decode
def decode(str):
   decodedStr=base64.b64decode(str).decode('utf-8')

   print('decoded:', decodedStr)

# record asset name to a file
def record_assetName(name):
   global f3
   
   f3.write(name +'\n')

num_content = 10
f1 = open('/Users/samear/apache-jmeter-5.1.1/projects/repo-man/data/assets' + '.txt', 'w')
f2 = open('/Users/samear/apache-jmeter-5.1.1/projects/repo-man/data/renditions' + '.txt', 'w')
f3 = open('/Users/samear/apache-jmeter-5.1.1/projects/repo-man/data/assetName' + '.txt', 'w')


for n in range(num_content):
   assetName = str(unique_value())
   renditionName = str(unique_value())
   
   record_assetName(assetName)
   record_assetName(renditionName)

   print('Generating...', n + 1, 'Asset:', assetName, '- Rendition:', renditionName)
   #{"repo:name": "1", "repo:createDate": "2017-09-26T15:52:25Z","astock:assetType": "vector","components": [{"astock:profile": "zipVector","dc:format": "application/vnd.adobe.stock.vec+zip","files": [{"repo:size": 424242,"repo:createDate": "2017-09-26T15:52:25Z","repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178","href": "s3://fotolia-stage-vectors.s3-eu-west-1.amazonaws.com/00/00/01/23/zipVector_1234.zip"}]},{"astock:profile": "vector","dc:format": "application/postscript","tiff:imageWidth": 2048,"tiff:imageLength": 1152,"tiff:XResolution": {"tiff:numerator": 300,"tiff:denominator": 1},"files": [{"repo:size": 424243,"repo:createDate": "2017-09-27T15:52:25Z","repo:etag": "95b9b5e299d60bf4e5972d61ef6d2179","href": "s3://fotolia-stage-vectors.s3-eu-west-1.amazonaws.com/00/00/01/23/vector_1234.ai"}]},{"astock:profile": "image","dc:format": "image/jpeg","tiff:imageWidth": 2048,"tiff:imageLength": 1152,"files": [{"repo:size": 424244,"repo:createDate": "2017-09-28T15:52:25Z","repo:etag": "95b9b5e299d60bf4e5972d61ef6d2180","href": "s3://fotolia-stage-vectors.s3-eu-west-1.amazonaws.com/00/00/01/23/image_1234.jpg"}]}],"derivatives": [{"astock:derivativeType": "original","astock:componentType": "primary","componentIndexes": [0]},{"astock:derivativeType": "original","astock:componentType": "zipEntry","componentIndexes": [1, 2]},{"astock:derivativeType": "deliverable","astock:componentType": "primary","componentIndexes": [1]}]}
    
   asset_data = '{"repo:name": "' + assetName + '", "repo:createDate": "2017-09-26T15:52:25Z","astock:assetType": "vector","components": [{"astock:profile": "zipVector","dc:format": "application/vnd.adobe.stock.vec+zip","files": [{"repo:size": 424242,"repo:createDate": "2017-09-26T15:52:25Z","repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178","href": "s3://fotolia-stage-vectors.s3-eu-west-1.amazonaws.com/00/00/01/23/zipVector_1234.zip"}]},{"astock:profile": "vector","dc:format": "application/postscript","tiff:imageWidth": 2048,"tiff:imageLength": 1152,"tiff:XResolution": {"tiff:numerator": 300,"tiff:denominator": 1},"files": [{"repo:size": 424243,"repo:createDate": "2017-09-27T15:52:25Z","repo:etag": "95b9b5e299d60bf4e5972d61ef6d2179","href": "s3://fotolia-stage-vectors.s3-eu-west-1.amazonaws.com/00/00/01/23/vector_1234.ai"}]},{"astock:profile": "image","dc:format": "image/jpeg","tiff:imageWidth": 2048,"tiff:imageLength": 1152,"files": [{"repo:size": 424244,"repo:createDate": "2017-09-28T15:52:25Z","repo:etag": "95b9b5e299d60bf4e5972d61ef6d2180","href": "s3://fotolia-stage-vectors.s3-eu-west-1.amazonaws.com/00/00/01/23/image_1234.jpg"}]}],"derivatives": [{"astock:derivativeType": "original","astock:componentType": "primary","componentIndexes": [0]},{"astock:derivativeType": "original","astock:componentType": "zipEntry","componentIndexes": [1, 2]},{"astock:derivativeType": "deliverable","astock:componentType": "primary","componentIndexes": [1]}]}'
   encode_Assets(asset_data)

   rendition_data = '{"repo:name": "' + renditionName + '", "repo:createDate": "2017-09-26T15:52:25Z","astock:assetType": "vector","components": [{"astock:profile": "zipVector","dc:format": "application/vnd.adobe.stock.vec+zip","files": [{"repo:size": 424242,"repo:createDate": "2017-09-26T15:52:25Z","repo:etag": "95b9b5e299d60bf4e5972d61ef6d2178","href": "s3://fotolia-stage-vectors.s3-eu-west-1.amazonaws.com/00/00/01/23/zipVector_1234.zip"}]},{"astock:profile": "vector","dc:format": "application/postscript","tiff:imageWidth": 2048,"tiff:imageLength": 1152,"tiff:XResolution": {"tiff:numerator": 300,"tiff:denominator": 1},"files": [{"repo:size": 424243,"repo:createDate": "2017-09-27T15:52:25Z","repo:etag": "95b9b5e299d60bf4e5972d61ef6d2179","href": "s3://fotolia-stage-vectors.s3-eu-west-1.amazonaws.com/00/00/01/23/vector_1234.ai"}]},{"astock:profile": "image","dc:format": "image/jpeg","tiff:imageWidth": 2048,"tiff:imageLength": 1152,"files": [{"repo:size": 424244,"repo:createDate": "2017-09-28T15:52:25Z","repo:etag": "95b9b5e299d60bf4e5972d61ef6d2180","href": "s3://fotolia-stage-vectors.s3-eu-west-1.amazonaws.com/00/00/01/23/image_1234.jpg"}]}],"derivatives": [{"astock:derivativeType": "original","astock:componentType": "primary","componentIndexes": [0]},{"astock:derivativeType": "original","astock:componentType": "zipEntry","componentIndexes": [1, 2]},{"astock:derivativeType": "deliverable","astock:componentType": "primary","componentIndexes": [1]}]}'
   encode_Renditions(rendition_data)

   #decode(encodedStr)
f1.close()
f2.close()
f3.close()
