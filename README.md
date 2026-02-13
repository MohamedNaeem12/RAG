# mini-rag
this is implementaion of the RAG project for QA 
## Requirements
-pyhon 3.8
### intsall pythin using miniconda 



# to make cli always write in new line for good readability
'''bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
'''

## Running fastapi as a server 
we will use uvicorn 
'''bash
$uvicorn main:app --reload --host 0.0.0.0 --port  5000
'''
## Install postman