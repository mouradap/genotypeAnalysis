#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import myvariant
mv = myvariant.MyVariantInfo()


# In[5]:


geno = pd.read_csv('Genetic.csv')
rsList = []

for i in range(0,len(geno.SNP)):
    if geno.SNP[i][0:2] == 'rs':
        rs = geno.SNP[i]
        rsList.append(rs)

rsList


# In[9]:


res = mv.querymany(rsList, scopes='dbsnp.rsid', fields='clinvar')


# In[10]:


res


# In[214]:


genotype = dict()

for i in range(0,len(res)):
    if len(res[i]) > 3:
        if 'gene' in res[i]['clinvar']:
            gene = res[i]['clinvar']['gene']['symbol']
        
        else:
            gene = i
        
        if isinstance(res[i]['clinvar']['rcv'], dict):
            CS = res[i]['clinvar']['rcv']['clinical_significance']
            condition = res[i]['clinvar']['rcv']['conditions']['name']

            
        else:
            CS = res[i]['clinvar']['rcv'][0]['clinical_significance']
            condition = res[i]['clinvar']['rcv'][0]['conditions']['name']
        
        if 'coding' in res[i]['clinvar']['hgvs']:
            coding = res[i]['clinvar']['hgvs']['coding']
        else:
            coding = res[i]['clinvar']['hgvs']
        
        rs = res[i]['query']
            
        
    genotype[gene] = [rs, coding, condition, CS]
        
        


# In[215]:


len(genotype)


# In[216]:


df = pd.DataFrame.from_dict(genotype, orient='index')


# In[217]:


df.columns = ['rs', 'Coding', 'Condition', 'Clinical Significance']


# In[219]:


df


# In[218]:


df['Clinical Significance'].unique()


# In[211]:


df[df['Clinical Significance'].str.contains('drug response')]


# In[212]:


df[df['Clinical Significance'].str.contains('association')]


# In[213]:


df[df['Clinical Significance'].str.contains('Uncertain significance')]


# In[220]:


df.to_csv('Genotype and Clinical Significance.csv')


# In[241]:


report = str('This is your genotype report based on ClinVar variant annotations.\nWe found a total of {} significant SNPs in your genotype file.\n'.format(len(df['rs']))
             +str('Your file is accessible as "Genotype and Clinical Significance.csv"\n') +
            str('This file is indexed by gene name of genes with significant SNPs, the respective SNP annotation,\n') +
            str('the variation in coding sequence, coditions associated to such variantion, and its clinical significance.')).splitlines()


# In[245]:


report = open("Report.txt", "w")
report.write(str(str('This is your genotype report based on ClinVar variant annotations.\nWe found a total of {} significant SNPs in your genotype file.\n'.format(len(df['rs']))
             +str('Your file is accessible as "Genotype and Clinical Significance.csv"\n') +
            str('This file is indexed by gene name of genes with significant SNPs, the respective SNP annotation,\n') +
            str('the variation in coding sequence, coditions associated to such variantion, and its clinical significance.')).splitlines()))
text_file.close()


# In[ ]:




