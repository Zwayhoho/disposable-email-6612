import re
filename='4-7-2019.csv'
fHandle = open(filename)
# regex expression that gets http:// from the file
pattern =r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' 

output =[]
lines = fHandle.readlines()
fHandle.close()
img_ext = ['.jpg','.gif','.png']
for l in lines:
        out = re.findall(pattern,l)
        for url in out:
                # get rid of the parenthesis surrounding the urls
                url.strip("\"")
                # get rid of the </a></div> ending in some of the urls
                url = re.sub('\</div>$', '', url)
                url = re.sub('\</a>$', '', url)
                length = len(url)
                # skip links ending with .jpg or gif or png
                if url[length-4:] in img_ext:
                    pass
                elif url not in output:
                    output.append(url)
output_Handler = open(filename+"_output",'w')
for url in output:
    output_Handler.write(url+'\n')
output_Handler.close()