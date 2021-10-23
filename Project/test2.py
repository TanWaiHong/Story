a = 'https://drive.google.com/open?id=1wMhGCO2U0MZFHPTLNqTA_nJzdTdr1dFY'
b = 'https://drive.google.com/uc?export=view&id='
a = a.strip('https://drive.google.com/open?id=')
print(b + a)