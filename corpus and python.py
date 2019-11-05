#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nltk.corpus import stopwords
stopwords.words('english')


# In[18]:


text = """Springer Handbook provides a concise compilation of approved key information on methods of research, general principles and functional relationships in physical and applied sciences."""
text.lower()
text.upper()


# In[19]:


text = """Springer Handbook provides a concise compilation of approved key 
information on methods of research, general principles and functional 
relationships in physical and applied sciences."""
aaa = text.split()
[w for w in aaa if not w.islower()]


# In[20]:


text = """Springer Handbook provides a concise compilation of approved key 
information on methods of research, general principles and functional 
relationships in physical and applied sciences."""
aaa = text.split()
bbb = [w.upper() for w in aaa]
''.join(bbb)


# In[24]:


from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
wnl.lemmatize('universities')
wnl.lemmatize('was','v')
wnl.lemmatize('happier','a')


# In[29]:


text = """Springer Handbook provides a concise compilation of approved key information on methods of research, general principles and functional relationships in physical and applied sciences."""
import nltk
from nltk import word_tokenize
nltk.word_tokenize(text)
nltk.sent_tokenize(text)


# In[31]:


from nltk.corpus import inaugural
inaugural.words('2017-Trump.txt')
inaugural.sents('2017-Trump.txt')


# In[38]:


text = """Springer Handbook provides a concise compilation of approved key information on methods of research, general principles and functional relationships in physical and applied sciences."""
import nltk
text1 = text.split()
nltk.pos_tag(text1)


# In[39]:


tagged_text = nltk.pos_tag(text1)
noun = [(word,tag) for word, tag in tagged_text if any (pos_tag in tag for pos_tag in ['NNP','NN'])]
print (noun[0:6])


# In[40]:


text = """Springer Handbook provides a concise compilation of approved key information on methods of research, general principles and functional relationships in physical and applied sciences."""
import nltk
tokens = nltk.word_tokenize(text)
tagged_sent = nltk.pos_tag(tokens, tagset = 'universal')
print (tagged_sent)


# In[44]:


text = """Springer Handbook provides a concise compilation of approved key information on methods of research, general principles and functional relationships in physical and applied sciences."""
import nltk
tokens = nltk.word_tokenize(text)
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents()
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
tagged_text = unigram_tagger.tag(tokens)
print (tagged_text)


# In[46]:





# In[47]:


text = """Springer Handbook provides a concise compilation of approved key information on methods of research, general principles and functional relationships in physical and applied sciences. The world's leading experts in the fields of physics and engineering will be assigned by one or several renowned editors to write the chapters comprising each volume. The content is selected by these experts from Springer sources (books, journals, online content) and other systematic and approved recent publications of scientific and technical information. This handbook contains 3 volumes."""
text1 = text.split()
len(text1)
x = [word.lower() for word in text1 if word.isalpha()]
len(x)


# In[ ]:




