Masala: Eng faol foydalanuvchilar reytingi
📄 Kirish fayl: users.csv
Faylda foydalanuvchilarning ismi va ular yozgan postlar soni bor. Siz ularni eng ko‘p post yozganidan boshlab saralaysiz va top_users.csv faylga reyting raqami bilan yozasiz.

📁 Fayl tuzilmasi:
Copy
Edit
user_ranking/
├── users.csv        ← Kiruvchi fayl
├── top_users.csv    ← Natija yoziladigan fayl
└── user_ranker.py   ← Siz yozadigan kod
📄 users.csv (kirish)
Copy
Edit
username,posts
anvar,56
laylo,102
kamron,87
nilufar,93
javohir,40
🎯 Maqsad:
top_users.csv fayl quyidagicha bo‘lishi kerak:

Copy
Edit
rank,username,posts
1,laylo,102
2,nilufar,93
3,kamron,87
4,anvar,56
5,javohir,40
✅ Talablar:
csv.DictReader va csv.DictWriter ishlating.

sorted() yoki .sort() ishlatishingiz mumkin.

Natijani rank bilan top_users.csv faylga yozing.