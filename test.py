#dannie  2018/10/17  16:42  PyCharm

from qi.utils.gql_util import GqlService
from check import get_position
from pandas.core.frame import DataFrame
import pandas as pd

def otherposition_pct():
    service = GqlService('http://dev-qi-jacob.inner.jasperam.com/graphql')
    df=get_position(date_=None)
    sym=list(df['symbol'])
    data = service.postGql('symbolData', {'symbols': sym}, ['rt_pct_chg'])
    L=[]
    for i in data:
        pct=i.get('rt_pct_chg')
        L.append(pct)
    c={"symbol" : sym,
       "pct" : L}
    data=DataFrame(c)
    data['pct'] = data['pct'].apply(lambda rec: 0 if rec is 'NaN' else rec*100)
    data=data.sort_values(axis = 0,ascending = False,by = 'pct')
    data=data.drop_duplicates(subset=['symbol'], keep='first')
    result=pd.merge(data,df,on='symbol')
    print(result)

otherposition_pct()

