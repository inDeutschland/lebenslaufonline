import sqlite3

# الاتصال بقاعدة البيانات
conn = sqlite3.connect("flask_app.db")
cur = conn.cursor()

# تنفيذ الاستعلام مع الترتيب حسب التصنيف أولاً ثم اسم الوكيل
cur.execute("""
SELECT 
    attributes.id,
    attributes.name AS attribute_name,
    categories.name AS category_name
FROM 
    attributes
JOIN 
    categories
ON 
    attributes.category_id = categories.id
ORDER BY 
    category_name, attribute_name
""")

# جلب النتائج
results = cur.fetchall()

# طباعة رأس الجدول
print(f"{'ID':<4} {'Attribute':<30} {'Category'}")
print("-" * 60)

# طباعة النتائج
for id, attribute, category in results:
    print(f"{id:<4} {attribute:<30} {category}")

# إغلاق الاتصال
conn.close()
