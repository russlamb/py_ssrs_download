
import calendar
import datetime

def get_month_end_dates(start_year, start_month=1, end_year=-1, end_month=-1):
    """Return a list of month end dates.  End year and month default to today"""
    date_list = []
    today=datetime.date.today()
    if end_year == -1:
        end_year=today.year
    if end_month== -1:
        end_month=today.month

    end_date = get_last_day_in_month(end_year, end_month)
    # if no year or month specified, assume today is the cutoff
    if (end_year==-1 and end_month==-1) and end_date>today:
        end_date=today            
    
    for i in range(start_year ,end_year + 1):
            for j in range(start_month, end_month):
                d=get_last_day_in_month(i,j)
                
                # only include month ends before end date
                if(d<=end_date):
                    date_list.append(d)
    return date_list

def get_last_day_in_month(year, month):
    """get last day given a year and month"""
    mrange = calendar.monthrange(year,month)
    d = datetime.date(year,month,mrange[1])
    return d
    
def print_month_end_dates(start_year):    
    date_list = get_month_end_dates(start_year)
    for i in date_list:
        print(i)



