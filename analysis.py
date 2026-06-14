import storage
s=storage
s.load_csv()
print()

if not s.data1:
    s.data1 = {'date': '2026-06-01', 'category': 'Rent', 'amount': '15000'}


def calculate_total():
    """totals = 0
    for i in s.data1:
        totals += int(i["amount"])
    return (totals)"""

    return sum(
        int(expense["amount"])
        for expense in s.data1
    )

#calculate_total()

def categories_expenses():
    totals = {}
    for i in s.data1:
        cat = i["category"]
        if cat in totals.items():
            totals[cat] += int(i["amount"])
        else:
            totals[cat] = int(i["amount"])

    return totals

#print(categories_expenses())

def sort_categories():
    data = categories_expenses()
    sort = sorted(data.items(), key=lambda item : int(item[1]))
    return (sort)

#print(sort_categories())

def heighest_category():
    list_is = list(sort_categories())
    return list_is[-1]

#print(heighest_category())

def lowest_category():
    list_is = list(sort_categories())
    return list_is[0]

#print(lowest_category())

def category_len():
    totals = {}
    for i in s.data1:
        cat = i["category"]
        if cat in totals.items():
            totals[cat] += 1
        else:
            totals[cat] = 1
    return totals

#print(category_len())

def get_avg():
    avg = (calculate_total()) / len(s.data1)
    return f"{avg:.2f}"

#print(get_avg())

def transaction_dates():
    dates = []
    for i in s.data1:
        dates.append(i["date"])
    return dates

def transaction_with_dates():
    list_is = []
    for i in s.data1:
        list_is.append({i["date"]:i["amount"]})
    return list_is

def generate_summary_report():
    print(f"""
                        SUMMARY REPORT -->>
          
          TOTAL_EXPENSE       -    {calculate_total()}

          CATEGORY_EXPENSES   -    {categories_expenses()}

          HIGHEST_CATEGORY    -    {heighest_category()}

          LOWEST_CATEGORY     -    {lowest_category()}

          AVERAGE_EXPENSE     -    {get_avg()}

          TRANSACTION_DATES   -    {transaction_dates()}

          TRANSACTION_DATE_AMOUNT  -   {transaction_with_dates()}

          MONTHLY_ANALYSIS    -    {get_monthly_expenses()}
""")
    
#generate_summary_report()


def get_month(date):
    return int(date.split("-")[1])


def months():
    MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
    return MONTHS

def apply_month_name(d):
    MONTHS = months()
    for key, value in d.items():
        return(MONTHS[key], " --- ", value)
    


def get_monthly_expenses():
    monthly_totals = {}

    for i in s.data1:
        month = get_month(i["date"])
        amount = i["amount"]
        monthly_totals[month] = (
            monthly_totals.get(month, 0) + int(amount)
        )
    return apply_month_name(monthly_totals)


#print(get_monthly_expenses())
