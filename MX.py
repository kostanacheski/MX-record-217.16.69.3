import dns.resolver
import pandas as pd
import time
import sys


pd.__version__

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['217.16.69.3']

filename = 'domains.txt'

try:
    print("Otvori file ",filename)
    with open(filename) as f:
        domains = [line.rstrip() for line in f]
except:
    print("Error ",filename)
    sys.exit("IO Error")
else:
    print(len(domains),"loading adresses...MX lookup \n\n")

time.sleep(1)

MXRekordi =[]
mail_address = []


for domain in domains:
    try:
        answers = dns.resolver.resolve(domain,'MX')
    except:
        print("error")
        MXRekord = "error"
    else:
        MXRekord = answers[0].exchange.to_text()
    finally:
        MXRekordi.append(MXRekord)
        mail_address.append(domain)
        print(domain)
        time.sleep(.200)


df = pd.DataFrame({"Domain":mail_address,"MXRecords":MXRekordi})
print("\n",str(len(mail_address)),"processed records")
new_file='output.txt'
df.to_csv(new_file,index=False)
