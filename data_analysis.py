import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
df = pd.read_csv("drop_null_data.csv")

# Display the first few rows of the dataframe to understand its structure
print(df.head())

# 1. Are sales proportionally happening more on weekends?
sales_on_weekends = df[df['weekend'] == True]['revenue'].sum()
sales_on_weekdays = df[df['weekend'] == False]['revenue'].sum()

if sales_on_weekends > sales_on_weekdays:
    print("Sales are proportionally happening more on weekends.")
else:
    print("Sales are proportionally happening more on weekdays.")


# 2. Which regions are generating the most revenue currently?
revenue_by_region = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
top_regions = revenue_by_region.head(3)
print("Top regions generating the most revenue:")
print(top_regions)


# 3. Is there any particular website traffic that stands out when generating sales?
traffic_type_revenue = df.groupby('traffic_type')['revenue'].sum().sort_values(ascending=False)
top_traffic_type = traffic_type_revenue.idxmax()
print("The website traffic type that stands out when generating sales:", top_traffic_type)


# 4. What percentage of time is spent on the website performing administrative/product or informational related tasks?
admin_duration = df['administrative_duration'].sum()
product_duration = df['product_related_duration'].sum()
info_duration = df['informational_duration'].sum()
total_duration = df[['administrative_duration', 'product_related_duration', 'informational_duration']].sum().sum()

admin_percentage = (admin_duration / total_duration) * 100
product_percentage = (product_duration / total_duration) * 100
info_percentage = (info_duration / total_duration) * 100

print("Percentage of time spent on administrative tasks:", admin_percentage)
print("Percentage of time spent on product-related tasks:", product_percentage)
print("Percentage of time spent on informational tasks:", info_percentage)


# 5. Are there any informational/administrative tasks which users spend time doing most?
admin_avg_duration = df['administrative_duration'].mean()
product_avg_duration = df['product_related_duration'].mean()
info_avg_duration = df['informational_duration'].mean()

print("Average duration of administrative tasks:", admin_avg_duration)
print("Average duration of product-related tasks:", product_avg_duration)
print("Average duration of informational tasks:", info_avg_duration)


# 6. What is the breakdown of months making the most sales?
sales_by_month = df.groupby('month')['revenue'].sum().sort_values(ascending=False)
print("Breakdown of months making the most sales:")
print(sales_by_month)

#**********************************************************************************************
# Question 1: Count of operating systems used to visit the site and the percentage of the total
operating_system_counts = df['operating_systems'].value_counts()
operating_system_percentage = (operating_system_counts / len(df)) * 100

# Plot the count of operating systems
plt.figure(figsize=(10, 6))
operating_system_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Operating Systems Used to Visit the Site')
plt.xlabel('Operating System')
plt.ylabel('Count')
plt.xticks(rotation=45)

# Add data labels above each bar
for i, count in enumerate(operating_system_counts):
    plt.text(i, count + 5, str(count), ha='center', va='bottom')

plt.show()

# Plot the percentage of operating systems
plt.figure(figsize=(10, 6))
operating_system_percentage.plot(kind='bar', color='lightgreen')
plt.title('Percentage of Operating Systems Used to Visit the Site')
plt.xlabel('Operating System')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)

# Add data labels above each bar
for i, percentage in enumerate(operating_system_percentage):
    plt.text(i, percentage + 1, f"{percentage:.2f}%", ha='center', va='bottom')

plt.show()

# Question 2: Amount of users visiting the site using mobile vs desktop operating systems
mobile_users = df[df['operating_systems'].str.contains('Mobile', case=False)].shape[0]
desktop_users = df.shape[0] - mobile_users

plt.figure(figsize=(8, 5))
plt.bar(['Mobile', 'Desktop'], [mobile_users, desktop_users], color=['lightgreen', 'lightblue'])
plt.title('Number of Users Visiting the Site Using Mobile vs Desktop Operating Systems')
plt.xlabel('Operating System')
plt.ylabel('Number of Users')

# Add data labels above each bar
for i, value in enumerate([mobile_users, desktop_users]):
    plt.text(i, value + 1000, str(value), ha='center', va='bottom')

plt.show()

# Question 3: Most commonly used browsers and their breakdown on mobile vs desktop
browser_counts = df['browser'].value_counts().head(5)

mobile_browsers_count = df[df['operating_systems'].str.contains('Mobile', case=False)]['browser'].value_counts()
mobile_browsers_count = mobile_browsers_count.reindex(browser_counts.index, fill_value=0)

desktop_browsers_count = df[~df['operating_systems'].str.contains('Mobile', case=False)]['browser'].value_counts()
desktop_browsers_count = desktop_browsers_count.reindex(browser_counts.index, fill_value=0)

plt.figure(figsize=(12, 6))
browser_counts.plot(kind='bar', color='skyblue', label='All Users')
mobile_browsers_count.plot(kind='bar', color='lightgreen', label='Mobile Users')
desktop_browsers_count.plot(kind='bar', color='lightblue', label='Desktop Users')
plt.title('Most Commonly Used Browsers and Their Breakdown on Mobile vs Desktop')
plt.xlabel('Browser')
plt.ylabel('Count')
plt.legend()
plt.xticks(rotation=45)

# Add data labels above each bar
for i, (browser, count) in enumerate(zip(browser_counts.index, browser_counts)):
    plt.text(i, count + 20, str(count), ha='center', va='bottom')

for i, (browser, count) in enumerate(zip(mobile_browsers_count.index, mobile_browsers_count)):
    plt.text(i - 0.2, count + 20, str(count), ha='center', va='bottom')

for i, (browser, count) in enumerate(zip(desktop_browsers_count.index, desktop_browsers_count)):
    plt.text(i + 0.2, count + 20, str(count), ha='center', va='bottom')

plt.show()

# Question 4: Identify regions where there is a discrepancy in popular operating systems
popular_os_regions = df.groupby('region')['operating_systems'].value_counts().unstack().fillna(0)
popular_os_regions.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Popular Operating Systems in Different Regions')
plt.xlabel('Region')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Operating System')

plt.show()

#**************************************************************************************************
# Visualize traffic generating the most revenue broken down by region
traffic_revenue_by_region = df.groupby(['region', 'traffic_type'])['revenue'].sum().unstack(fill_value=0)
traffic_revenue_by_region.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Revenue Generated by Traffic Type and Region')
plt.xlabel('Region')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.legend(title='Traffic Type')
plt.show()

# Visualize traffic with the highest bounce rate by region
traffic_bounce_rate_by_region = df.groupby(['region', 'traffic_type'])['bounce_rates'].mean().unstack(fill_value=0)
highest_bounce_rate = traffic_bounce_rate_by_region.max(axis=1)
lowest_bounce_rate = traffic_bounce_rate_by_region.min(axis=1)

plt.figure(figsize=(12, 6))
highest_bounce_rate.plot(kind='bar', color='red', alpha=0.7, label='Highest Bounce Rate')
lowest_bounce_rate.plot(kind='bar', color='green', alpha=0.7, label='Lowest Bounce Rate')
plt.title('Bounce Rate by Traffic Type and Region')
plt.xlabel('Region')
plt.ylabel('Bounce Rate')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Check which months have generated the most sales from ads traffic
# Filter the DataFrame to include only sales from ads traffic
ads_traffic_df = df[df['traffic_type'].str.contains('ads', case=False)]

# Group the data by month and calculate the total revenue for each month
monthly_revenue = ads_traffic_df.groupby('month')['revenue'].sum().sort_values(ascending=False)

# Plot the total revenue for each month
plt.figure(figsize=(12, 8))
bar_plot = monthly_revenue.plot(kind='bar', color='skyblue')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.title('Total Revenue from Ads Traffic by Month')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Add data labels on each bar
for index, value in enumerate(monthly_revenue):
    bar_plot.text(index, value, str(value), ha='center', va='bottom')

plt.show()

#**************************************************************************************************
# Question 1: Which region is currently generating the most/least revenue?
region_revenue = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=region_revenue.values, y=region_revenue.index, palette='viridis')

# Add data labels to the bar chart
for i, value in enumerate(region_revenue.values):
    plt.text(value, i, f'{value:,}', ha='left', va='center', fontsize=10)

plt.xlabel('Revenue')
plt.ylabel('Region')
plt.title('Revenue Generated by Each Region')
plt.show()

# Question 2: What percentage of our returning/new customers are making a purchase?
customer_purchase = df.groupby('visitor_type')['revenue'].sum()
plt.figure(figsize=(8, 6))
plt.pie(customer_purchase, labels=customer_purchase.index, autopct='%1.1f%%', colors=['skyblue', 'lightgreen'])

# Add color label to the lower right corner of the pie chart
plt.text(-1.5, -1.5, 'skyblue: Returning Visitor\nlightgreen: New Visitor', fontsize=10)

plt.title('Percentage of Revenue by Customer Type')
plt.show()

# Question 3: Are sales being made more on weekends comparatively to weekdays?
df['weekend'] = df['weekend'].map({True: 'Weekend', False: 'Weekday'})
weekend_sales = df.groupby('weekend')['revenue'].sum()
plt.figure(figsize=(8, 6))
sns.barplot(x=weekend_sales.index, y=weekend_sales.values, palette='pastel')

# Add data labels to the bar chart
for i, value in enumerate(weekend_sales.values):
    plt.text(i, value, f'{value:,}', ha='center', va='bottom', fontsize=10)

plt.xlabel('Day of Week')
plt.ylabel('Revenue')
plt.title('Revenue Generated on Weekends vs. Weekdays')
plt.show()

# Question 4: Which months have been the most effective for generating sales?
monthly_sales = df.groupby('month')['revenue'].sum().sort_index()
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', color='orange')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Monthly Revenue')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Question 5: Is direct/social or advertising traffic contributing heavily to sales?
traffic_sales = df.groupby('traffic_type')['revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=traffic_sales.values, y=traffic_sales.index, palette='rocket')

# Add data labels to the bar chart
for i, value in enumerate(traffic_sales.values):
    plt.text(value, i, f'{value:,}', ha='left', va='center', fontsize=10)

plt.xlabel('Revenue')
plt.ylabel('Traffic Type')
plt.title('Revenue Generated by Traffic Type')
plt.show()