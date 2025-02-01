"""
import pandas as pd
from collections import defaultdict

# Specify the column that should be read as strings
df = pd.read_csv('sitecode_did.csv', dtype={'DID': str})
# print(df) 
# Convert to a dictionary where keys are column names and values are lists
# data_dict = df.to_dict(orient='records')

# print(data_dict)
# to_dict with out any parameter it converts it as a dictionary 
# site_code_dict = df.to_dict()
# print(f"\n Without using any options: {site_code_dict}")

# In list format 
# site_code_dict = df.to_dict("list")
# print(f"\n Using list: {site_code_dict}")

# In split format 
site_code_dict = df.to_dict("split")
# print(f"\n Using split: {site_code_dict}")
# print(f"\n List of values from DF without index and header: {site_code_dict['data']}")

raw_data = site_code_dict['data']
# convert a list of list in  dictionary where key is the first element of the list and values are list
print(raw_data)
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}

# info_dict = {}
# for i in range(len(info_list)):
#     info_dict[info_detail[i]] = info_list[i]
# print(info_dict)


# Using Zip
# z = zip (info_detail, info_list)
# print(dict(z))

# new_dict = {expression for item in iterable if condition }
new_dict = {}
for row in raw_data:
    if row[0] not in new_dict:
        new_dict[row[0]]= []
    new_dict[row[0]].append(row[1])
# print(new_dict)
# a_list = [[a, 10], [a, 20], [a, 40], [b, 100], [b,30], [b, 55]]
# a_dict = {a:[10,20,40], b:[40, 100, 55]}

# x_dict = {}
# for item in a_list:
#     if item not in x_dict:
#         x_dict[item[0]].append(item[1])
#     else: 
#         x_dict[item[0]] = [item[1]]

# print(x_dict)

from collections import defaultdict

d1 = defaultdict(list)

for k, v in raw_data:
    d1[k].append(v)

# print(d1)
# d = dict((k:list(v)) for k, v in d1.items())
d = {k: list(v) for k, v in d1.items()}

print(d)
"""
reg = """
23:50:05-182
Registration Stats                -- Period -- -------- Lifetime --------
                        Active    High   Total      Total  PerMax    High
Total Registrations         1       1       0      64546     410     320
 SIP Registrations          1       1       0      64546     410     320
 H.323 Registrations        0       0       0          0       0       0
"""

session="""
23:49:15-132 Capacity=25000
Session Stats                     -- Period -- -------- Lifetime --------
                        Active    High   Total      Total  PerMax    High
Total Sessions              1       1       0      24555      30      94
SIP Sessions                1       1       0      24555      30      94
H.323 Sessions              0       0       0          0       0       0

IWF Stats                         -- Period -- -------- Lifetime --------
                        Active    High   Total      Total  PerMax    High
H.323 to SIP Calls          0       0       0          0       0       0
SIP to H.323 Calls          0       0       0          0       0       0

"""
def get_reg_config (input_string):
    """Returns a list of dictionaries
 
    Args:
        input_string (string): The output of the show command
    """
 
    # Three lines are the headers, which we can get using slicing 
    # The data we get is the tabular data
    # print(len(input_string.splitlines()))
    lines = input_string.splitlines()[4:]
    hostname = None 
    config = []
    for line in lines:
        words = line.split()
        print(words)
        # if hostname is None:
        #     # hostname = words[0]
        #     hostname = words.pop(0)
        if len(words) > 0:
            status = words[2:3][0]
            hostname= "_".join(words[0:2])
            config.append({hostname: status})
            hostname = None
    print(config)
    return (config)


def get_sess_config (input_string):
    """Returns a list of dictionaries
 
    Args:
        input_string (string): The output of the show command
    """
 
    # Three lines are the headers, which we can get using slicing 
    # The data we get is the tabular data
    # print(len(input_string.splitlines()))
    lines = input_string.splitlines()[4:7]
    hostname = None 
    config = []
    for line in lines:
        words = line.split()
        print(words)
        # if hostname is None:
        #     # hostname = words[0]
        #     hostname = words.pop(0)
        if len(words) > 0:
            status = words[2:3][0]
            hostname= "_".join(words[0:2])
            config.append({hostname: status})
            hostname = None
    print(config)
    return (config)
print()
get_reg_config(reg)
print()
get_sess_config(session)


cert = """

certificate-record: host-cr
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            01:22:9c:56:22:46:6e:79:42:75:3b:0a:e7:aa:78:d8
    Signature Algorithm: sha256WithRSAEncryption
        Issuer:
            C=US
            O=Amazon
            CN=Amazon RSA 2048 M01
        Validity
            Not Before: Jun  3 00:00:00 2024 GMT
            Not After : Jun  1 23:59:59 2025 GMT
        Subject:
            CN=reg.vtc.amazonuc.com
        X509v3 extensions:
            X509v3 Authority Key Identifier:
                keyid:81:B8:0E:63:8A:89:12:18:E5:FA:3B:3B:50:95:9F:E6:E5:90:13:85

            X509v3 Subject Key Identifier:
                AE:6D:DD:38:A6:E8:00:C0:9F:21:C5:B0:42:E8:77:8F:30:0E:C9:1E
            X509v3 Subject Alternative Name:
                DNS:reg.vtc.amazonuc.com, DNS:reg-use.vtc.amazonuc.com, DNS:reg-useA.vtc.amazonuc.com, DNS:reg-useB.vtc.amazonuc.com, DNS:reg-usw.vtc.amazonuc.com, DNS:reg-uswA.vtc.amazonuc.com, DNS:reg-uswB.vtc.amazonuc.com, DNS:reg-dub.vtc.amazonuc.com, DNS:reg-dubA.vtc.amazonuc.com, DNS:reg-dubB.vtc.amazonuc.com, DNS:reg-apse.vtc.amazonuc.com, DNS:reg-apseA.vtc.amazonuc.com, DNS:reg-apseB.vtc.amazonuc.com, DNS:reg-apne.vtc.amazonuc.com, DNS:reg-apneB.vtc.amazonuc.com, DNS:reg-apneC.vtc.amazonuc.com, DNS:reg-prodA.vtc.amazonuc.com, DNS:reg-prodB.vtc.amazonuc.com, DNS:reg-prodC.vtc.amazonuc.com, DNS:reg-prodD.vtc.amazonuc.com, DNS:reg-prodE.vtc.amazonuc.com, DNS:reg-sjo-use.vtc.amazonuc.com, DNS:reg-sjo-useA.vtc.amazonuc.com, DNS:reg-sjo-useB.vtc.amazonuc.com
            X509v3 Certificate Policies:
                Policy: 2.23.140.1.2.1

            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment
            X509v3 Extended Key Usage:
                TLS Web Server Authentication, TLS Web Client Authentication
            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://crl.r2m01.amazontrust.com/r2m01.crl

            Authority Information Access:
                OCSP - URI:http://ocsp.r2m01.amazontrust.com
                CA Issuers - URI:http://crt.r2m01.amazontrust.com/r2m01.cer

            X509v3 Basic Constraints: critical
                CA:FALSE
            CT Precertificate SCTs:
                Signed Certificate Timestamp:
                    Version   : v1(0)
                    Log ID    : CF:11:56:EE:D5:2E:7C:AF:F3:87:5B:D9:69:2E:9B:E9:
                                1A:71:67:4A:B0:17:EC:AC:01:D2:5B:77:CE:CC:3B:08
                    Timestamp : Jun  3 00:19:59.731 2024 GMT
                    Extensions: none
                    Signature : ecdsa-with-SHA256
                                30:44:02:20:0F:DA:60:EA:B2:5E:83:2A:17:D4:91:AF:
                                AC:4F:9A:19:AF:FE:70:33:1E:FF:AB:30:54:77:13:A6:
                                B4:5E:F0:CA:02:20:4B:D4:35:30:25:B6:11:2E:65:A3:
                                A5:E5:40:D0:4D:58:73:86:BA:15:99:ED:05:F8:06:AE:
                                2A:04:10:C3:2A:FE
                Signed Certificate Timestamp:
                    Version   : v1(0)
                    Log ID    : 7D:59:1E:12:E1:78:2A:7B:1C:61:67:7C:5E:FD:F8:D0:
                                87:5C:14:A0:4E:95:9E:B9:03:2F:D9:0E:8C:2E:79:B8
                    Timestamp : Jun  3 00:19:59.732 2024 GMT
                    Extensions: none
                    Signature : ecdsa-with-SHA256
                                30:45:02:21:00:EA:A5:69:29:D7:75:9A:40:44:72:6D:
                                C5:41:67:FB:B9:41:86:EE:28:71:48:D0:3F:71:B3:92:
                                91:22:AC:02:46:02:20:2D:B7:43:CC:DC:DA:1A:CE:6A:
                                21:33:B9:D6:07:E3:4F:EC:BC:4B:3C:77:EB:51:C3:46:
                                91:89:1C:2B:4D:FD:C0
                Signed Certificate Timestamp:
                    Version   : v1(0)
                    Log ID    : E6:D2:31:63:40:77:8C:C1:10:41:06:D7:71:B9:CE:C1:
                                D2:40:F6:96:84:86:FB:BA:87:32:1D:FD:1E:37:8E:50
                    Timestamp : Jun  3 00:19:59.750 2024 GMT
    Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            07:73:12:38:0b:9d:66:88:a3:3b:1e:d9:bf:9c:cd:a6:8e:0e:0f
    Signature Algorithm: sha256WithRSAEncryption
        Issuer:
            C=US
            O=Amazon
            CN=Amazon Root CA 1
        Validity
            Not Before: Aug 23 22:21:28 2022 GMT
            Not After : Aug 23 22:21:28 2030 GMT
        Subject:
            C=US
            O=Amazon
            CN=Amazon RSA 2048 M01
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:TRUE, pathlen:0
            X509v3 Key Usage: critical
                Digital Signature, Certificate Sign, CRL Sign
            X509v3 Extended Key Usage:
                TLS Web Server Authentication, TLS Web Client Authentication
            X509v3 Subject Key Identifier:
                81:B8:0E:63:8A:89:12:18:E5:FA:3B:3B:50:95:9F:E6:E5:90:13:85
            X509v3 Authority Key Identifier:
                keyid:84:18:CC:85:34:EC:BC:0C:94:94:2E:08:59:9C:C7:B2:10:4E:0A:08

            Authority Information Access:
                OCSP - URI:http://ocsp.rootca1.amazontrust.com
                CA Issuers - URI:http://crt.rootca1.amazontrust.com/rootca1.cer

            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://crl.rootca1.amazontrust.com/rootca1.crl

            X509v3 Certificate Policies:
                Policy: 2.23.140.1.2.1

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            06:7f:94:4a:2a:27:cd:f3:fa:c2:ae:2b:01:f9:08:ee:b9:c4:c6
    Signature Algorithm: sha256WithRSAEncryption
        Issuer:
            C=US
            ST=Arizona
            L=Scottsdale
            O=Starfield Technologies, Inc.
            CN=Starfield Services Root Certificate Authority - G2
        Validity
            Not Before: May 25 12:00:00 2015 GMT
            Not After : Dec 31 01:00:00 2037 GMT
        Subject:
            C=US
            O=Amazon
            CN=Amazon Root CA 1
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:TRUE
            X509v3 Key Usage: critical
                Digital Signature, Certificate Sign, CRL Sign
            X509v3 Subject Key Identifier:
                84:18:CC:85:34:EC:BC:0C:94:94:2E:08:59:9C:C7:B2:10:4E:0A:08
            X509v3 Authority Key Identifier:
                keyid:9C:5F:00:DF:AA:01:D7:30:2B:38:88:A2:B8:6D:4A:9C:F2:11:91:83

            Authority Information Access:
                OCSP - URI:http://ocsp.rootg2.amazontrust.com
                CA Issuers - URI:http://crt.rootg2.amazontrust.com/rootg2.cer

            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://crl.rootg2.amazontrust.com/rootg2.crl

            X509v3 Certificate Policies:
                Policy: X509v3 Any Policy

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            a7:0e:4a:4c:34:82:b7:7f
    Signature Algorithm: sha256WithRSAEncryption
        Issuer:
            C=US
            O=Starfield Technologies, Inc.
            OU=Starfield Class 2 Certification Authority
        Validity
            Not Before: Sep  2 00:00:00 2009 GMT
            Not After : Jun 28 17:39:16 2034 GMT
        Subject:
            C=US
            ST=Arizona
            L=Scottsdale
            O=Starfield Technologies, Inc.
            CN=Starfield Services Root Certificate Authority - G2
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:TRUE
            X509v3 Key Usage: critical
                Digital Signature, Certificate Sign, CRL Sign
            X509v3 Subject Key Identifier:
                9C:5F:00:DF:AA:01:D7:30:2B:38:88:A2:B8:6D:4A:9C:F2:11:91:83
            X509v3 Authority Key Identifier:
                keyid:BF:5F:B7:D1:CE:DD:1F:86:F4:5B:55:AC:DC:D7:10:C2:0E:A9:88:E7

            Authority Information Access:
                OCSP - URI:http://o.ss2.us/
                CA Issuers - URI:http://x.ss2.us/x.cer

            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://s.ss2.us/r.crl

            X509v3 Certificate Policies:
                Policy: X509v3 Any Policy
"""
def get_cert_config (input_string):
    """Returns a list of dictionaries
 
    Args:
        input_string (string): The output of the show command
    """
 
    # Three lines are the headers, which we can get using slicing 
    # The data we get is the tabular data
    print(len(input_string.splitlines()))
    lines = input_string.splitlines()[7:8]
    print(lines)
    hostname = None 
    config = []
    for line in lines:
        words = line.split()
        print(words)
        # if hostname is None:
        #     # hostname = words[0]
        #     hostname = words.pop(0)
        if len(words) > 0:
            status = words[2:3][0]
            hostname= "_".join(words[0:2])
            config.append({hostname: status})
            hostname = None
    print(config)
    return (config)
# get_cert_config(cert)


PHONE_NUMBERS = """
+14256003340
+14256003341
+14256003342
+14256003343
+14256003354
""".strip().splitlines()
empty = []
list_of_dict = [{'phoneNumber': '+14699416402', 'state': 'ACTIVE', 'phoneNumberType': 'PRIMARY', 'mainNumber': False, 'includedTelephonyTypes': 'PSTN_NUMBER', 'tollFreeNumber': False, 'location': {'id': 'Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzc1YzcxMTRiLWViNTctNDc3MS1hYmUxLTVmODRiMDdlOTMwZQ', 'name': 'IAD28'}}, {'phoneNumber': '+14699416403', 'state': 'ACTIVE', 'phoneNumberType': 'PRIMARY', 'mainNumber': False, 'includedTelephonyTypes': 'PSTN_NUMBER', 'tollFreeNumber': False, 'location': {'id': 'Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzc1YzcxMTRiLWViNTctNDc3MS1hYmUxLTVmODRiMDdlOTMwZQ', 'name': 'IAD28'}}, {'phoneNumber': '+14699416405', 'state': 'ACTIVE', 'phoneNumberType': 'PRIMARY', 'mainNumber': False, 'includedTelephonyTypes': 'PSTN_NUMBER', 'tollFreeNumber': False, 'location': {'id': 'Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzc1YzcxMTRiLWViNTctNDc3MS1hYmUxLTVmODRiMDdlOTMwZQ', 'name': 'IAD28'}}, {'phoneNumber': '+14699416407', 'state': 'ACTIVE', 'phoneNumberType': 'PRIMARY', 'mainNumber': False, 'includedTelephonyTypes': 'PSTN_NUMBER', 'tollFreeNumber': False, 'location': {'id': 'Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzc1YzcxMTRiLWViNTctNDc3MS1hYmUxLTVmODRiMDdlOTMwZQ', 'name': 'IAD28'}}]
for lst in list_of_dict:
    (empty.append(lst['phoneNumber']))
print(empty)