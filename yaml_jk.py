#coding=utf8
#coding=utf8
import yaml

p={'method':'get','url':'http://127.0.0.1:8000/rjson','data':'','result':'333'}
ps={'method':'get','url':'http://127.0.0.1:8000/person','data':'','result':u'张df'}
f= open(r'config.yml','w')
yaml.dump_all([p,ps],f)
f.close()
with open(r'config.yaml','r') as y:
    yi=yaml.load_all(y,Loader=yaml.FullLoader)
    ya=list(yi)
    print ya
