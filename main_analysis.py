import pandas as pd

print("--- Data Analysis System Started ---")

# 1. قراءة البيانات
df = pd.read_csv('raw_data.csv')

# 2. تنظيف البيانات (حذف المكرر وملء الفراغات)
df.drop_duplicates(inplace=True)
df['Quantity'] = df['Quantity'].fillna(1)

# 3. حساب إجمالي المبيعات لكل منتج
df['Total'] = df['Price'] * df['Quantity']
print("Data Cleaned and Analyzed Successfully!")

# 4. حفظ النتيجة في ملف جديد
df.to_csv('final_report.csv', index=False)
print("Final report saved as 'final_report.csv'")