from enum import Enum


class RecordType(Enum):
    NONE = None
    A = 'A'
    AAAA = 'AAAA'
    CAA = 'CAA'
    CDS = 'CDS'
    CNAME = 'CNAME'
    DNAME= 'DNAME'
    DS = 'DS'
    LOC = 'LOC'
    MX = 'MX'
    NS = 'NS'
    PTR = 'PTR'
    SPF ='SPF'
    SRV = 'SRV'
    SSHFP = 'SSHFP'
    TLSA = 'TLSA'
    TXT = 'TXT'
    WKS = 'WKS'
