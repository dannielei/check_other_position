#dannie  2018/10/17  15:50  PyCharm

from jt.operate.data_loader import DataLoader
from jt.utils.calendar import TradeCalendar


def get_position(date_=None):
    trade_cal = TradeCalendar()
    data_loader = DataLoader()
    if date_ is None:
        date_ = trade_cal.get_cur_date()
    date_yester = trade_cal.get_trading_date(date_, -1)
    df = data_loader.get_position_gql(from_date=date_yester, to_date=date_yester, account_ids=None, symbols=None)
    df['OTHER'] = df['account_id'].apply(lambda rec: 'OTHER' in rec)
    df=df[df.OTHER==True]
    df=df[['account_id','symbol','volume']]
    df = df[df.volume!=0]
    return (df)


# print(get_position(date_='20181025'))

