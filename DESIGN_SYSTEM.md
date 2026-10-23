# سند طراحی سیستم لندینگ پیج پویش هوشمندسازی کسب‌وکارهای خرد
**پروژه: سایفر (Cypher) — منشی هوشمند بی‌پنل + CRM آموزشگاه**

---

## فهرست مطالب
1. [نقشه سایت و ساختار صفحات](#۱-نقشه-سایت-و-ساختار-صفحات)
2. [پالت رنگی](#۲-پالت-رنگی)
3. [تایپوگرافی و فونت‌ها](#۳-تایپوگرافی-و-فونت‌ها)
4. [کپی‌رایتینگ و متون سایت](#۴-کپی‌رایتینگ-و-متون-سایت)
5. [زبان بصری، موتیف‌ها و انیمیشن‌ها](#۵-زبان-بصری-موتیف‌ها-و-انیمیشن‌ها)
6. [جزئیات کامپوننت‌های کلیدی](#۶-جزئیات-کامپوننت‌های-کلیدی)

---

## ۱. نقشه سایت و ساختار صفحات

### ۱.۱ نقشه سایت (Sitemap)
```
صفحه اصلی (/)
├─ Hero Section با دموی زنده
├─ بخش ارزش‌پیشنهادی (Value Proposition)
├─ دموی تعاملی چت + واریز
├─ فیچرهای کلیدی (Features Grid)
├─ ماشین‌حساب ارزش (ROI Calculator)
├─ مقایسه با روش‌های سنتی (Comparison Table)
├─ تستیمونیال‌ها (Social Proof)
└─ CTA نهایی

صفحه منشی بی‌پنل (/zero-ui-assistant)
├─ معرفی منشی محاورهای
├─ سناریوهای استفاده واقعی
├─ دموی تعاملی روی تلگرام/روبیکا
└─ راهنمای راه‌اندازی ۳ دقیقه‌ای

صفحه موتور مالی (/financial-engine)
├─ دفتریار هوشمند
├─ صدور آنی لینک پرداخت
├─ اتصال قطعی به درگاه (API Verification)
├─ دفتر پول دوبل داخلی
└─ داشبورد مالی لایو

صفحه CRM آموزشگاه (/academy-crm)
├─ Case Study: کرمانشاهکارت
├─ مدیریت هنرجویان و دوره‌ها
├─ سیستم آزمون‌ها
├─ ربات تلگرام یکپارچه
├─ کوپایلوت Gemini
└─ حسابداری داخلی

صفحه تعرفه‌ها (/pricing)
├─ مدل اشتراک شفاف (Transparent Pricing)
├─ مقایسه پلن‌ها
├─ سوالات متداول مالی
└─ دکمه شروع آزمایشی

صفحه تماس / درخواست راه‌اندازی (/start)
├─ فرم درخواست سریع
├─ دکمه اتصال مستقیم به پیامرسان
├─ تقویم زمان‌بندی (Scheduling)
└─ اطلاعات پشتیبانی
```

### ۱.۲ ساختار صفحه اصلی (Homepage Sections)

#### **Section 1: Hero Section**
- **محتوا:**
  - تیتر اصلی جذاب و تکان‌دهنده
  - زیرتیتر شفاف با ارزش قابل‌لمس
  - دو CTA اصلی: «مشاهده دموی زنده» + «شروع رایگان»
  - شبیه‌ساز چت زنده سمت راست (Floating Chat Demo)
  
- **انیمیشن:**
  - Mesh Gradient پس‌زمینه با حرکت نرم
  - Floating cards با موشن میکرو
  - شبیه‌ساز چت با تایپینگ واقعی و پیام‌های متحرک

#### **Section 2: ارزش‌پیشنهادی (Value Props)**
- ۳ ستون کلیدی:
  1. **بدون پنل، بدون سردرگمی** — همه چیز در همان پیامرسانی که هر روز باز می‌کنی
  2. **پول واقعی، نه ادعا** — فقط وقتی درگاه تأیید کند، تراکنش ثبت می‌شود
  3. **CRM زنده برای آموزشگاه** — ثبت‌نام، آزمون، حسابداری، همه جا

#### **Section 3: دموی تعاملی (Interactive Demo)**
- **چت شبیه‌ساز:**
  - نمایش تبدیل پیام صوتی به فاکتور
  - تولید آنی لینک پرداخت
  - نمایش تأییدیه واریز از درگاه
  
- **داشبورد مالی لایو:**
  - نمودار رشد تراکنش‌ها
  - آمار زنده فروش

#### **Section 4: فیچرهای کلیدی (Features Grid)**
- **۶ فیچر اصلی به صورت کارت‌های شناور:**
  1. منشی محاورهای دوطرفه
  2. موتور دفتریار
  3. اتصال قطعی درگاه
  4. مدیریت هنرجویان
  5. ربات تلگرام یکپارچه
  6. کوپایلوت AI (Gemini)

#### **Section 5: ماشین‌حساب ارزش (ROI Calculator)**
- ورودی:
  - تعداد تراکنش ماهانه
  - میانگین مبلغ تراکنش
  - زمان صرف‌شده برای پیگیری دستی
  
- خروجی:
  - میزان صرفه‌جویی زمانی
  - کاهش خطای انسانی
  - افزایش سرعت دریافت وجه

#### **Section 6: مقایسه (Comparison Table)**
| ویژگی | روش سنتی (دفتر + اکسل) | پنل‌های پیچیده | **سایفر** |
|--------|----------------------|----------------|-----------|
| نیاز به آموزش | ✗ بالا | ✗ متوسط | ✓ صفر |
| اتصال درگاه | ✗ دستی | ~ نیمه‌خودکار | ✓ خودکار کامل |
| تأیید واقعی پرداخت | ✗ ادعایی | ~ گزارش متنی | ✓ API لحظه‌ای |
| محل کار | ✗ دفترچه | ✗ پنل جداگانه | ✓ همان پیامرسان |

#### **Section 7: تستیمونیال‌ها (Social Proof)**
- ۳ کارت شهادت با عکس، نام، نوع کسب‌وکار
- یکی از آموزشگاه کرمانشاهکارت (Case Study بزرگ)
- یکی از کسب‌وکار خرد (مثلاً باشگاه ورزشی)
- یکی از فروشگاه محلی

#### **Section 8: CTA نهایی**
- تیتر: **«حالا نوبت توست — منشی‌ات را روشن کن»**
- دو دکمه:
  - «شروع رایگان در تلگرام»
  - «شروع رایگان در روبیکا»
- زیرنویس اطمینان: «بدون نیاز به کارت اعتباری، بدون تعهد ماهانه در دوره آزمایشی»

---

## ۲. پالت رنگی

### ۲.۱ فلسفه رنگ
ترکیبی از **اعتماد مالی** (آبی‌های عمیق)، **انرژی فناوری** (بنفش‌های نئونی) و **گرمای انسانی** (نارنجی‌های نرم) برای کسب‌وکارهای خرد.

### ۲.۲ پالت اصلی (Primary Palette)

#### **رنگ اصلی (Primary) — آبی فناوری**
```
نام: Tech Blue
استفاده: دکمه‌های اصلی، لینک‌ها، هدرها

Primary-50:  #EFF6FF | hsl(214, 100%, 97%)
Primary-100: #DBEAFE | hsl(214, 95%, 93%)
Primary-200: #BFDBFE | hsl(214, 95%, 85%)
Primary-300: #93C5FD | hsl(213, 97%, 78%)
Primary-400: #60A5FA | hsl(213, 94%, 68%)
Primary-500: #3B82F6 | hsl(217, 91%, 60%) ← پایه اصلی
Primary-600: #2563EB | hsl(221, 83%, 53%)
Primary-700: #1D4ED8 | hsl(224, 76%, 48%)
Primary-800: #1E40AF | hsl(226, 71%, 40%)
Primary-900: #1E3A8A | hsl(224, 64%, 33%)
```

#### **رنگ کمکی (Accent) — بنفش نئونی**
```
نام: Cyber Purple
استفاده: هایلایت‌ها، انیمیشن‌ها، گرادینت‌ها

Accent-50:  #FAF5FF | hsl(270, 100%, 98%)
Accent-100: #F3E8FF | hsl(269, 100%, 95%)
Accent-200: #E9D5FF | hsl(269, 100%, 91%)
Accent-300: #D8B4FE | hsl(270, 95%, 85%)
Accent-400: #C084FC | hsl(270, 91%, 76%)
Accent-500: #A855F7 | hsl(271, 91%, 65%) ← پایه اصلی
Accent-600: #9333EA | hsl(271, 81%, 56%)
Accent-700: #7E22CE | hsl(272, 72%, 47%)
Accent-800: #6B21A8 | hsl(273, 67%, 39%)
Accent-900: #581C87 | hsl(274, 66%, 32%)
```

#### **رنگ گرما (Warmth) — نارنجی انرژی**
```
نام: Energy Orange
استفاده: CTA ثانویه، Badge‌ها، نوتیفیکیشن‌ها

Warmth-50:  #FFF7ED | hsl(33, 100%, 96%)
Warmth-100: #FFEDD5 | hsl(34, 100%, 92%)
Warmth-200: #FED7AA | hsl(32, 98%, 83%)
Warmth-300: #FDBA74 | hsl(31, 97%, 72%)
Warmth-400: #FB923C | hsl(27, 96%, 61%)
Warmth-500: #F97316 | hsl(25, 95%, 53%) ← پایه اصلی
Warmth-600: #EA580C | hsl(21, 90%, 48%)
Warmth-700: #C2410C | hsl(17, 88%, 40%)
Warmth-800: #9A3412 | hsl(15, 79%, 34%)
Warmth-900: #7C2D12 | hsl(14, 75%, 28%)
```

### ۲.۳ رنگهای معنایی (Semantic Colors)

#### **موفقیت (Success) — سبز تأیید**
```
Success-50:  #F0FDF4 | hsl(138, 76%, 97%)
Success-500: #10B981 | hsl(158, 64%, 52%) ← پایه
Success-600: #059669 | hsl(160, 84%, 39%)

استفاده: تأییدیه پرداخت موفق، وضعیت فعال، تیک‌های تأیید
```

#### **هشدار (Warning) — زرد احتیاط**
```
Warning-50:  #FEFCE8 | hsl(55, 92%, 95%)
Warning-500: #EAB308 | hsl(48, 96%, 53%) ← پایه
Warning-600: #CA8A04 | hsl(43, 96%, 56%)

استفاده: وضعیت معلق درگاه، در انتظار تأیید
```

#### **خطا (Error) — قرمز هشدار**
```
Error-50:  #FEF2F2 | hsl(0, 86%, 97%)
Error-500: #EF4444 | hsl(0, 72%, 51%) ← پایه
Error-600: #DC2626 | hsl(0, 84%, 60%)

استفاده: پرداخت ناموفق، خطاهای ولیدیشن، هشدارهای حیاتی
```

#### **خنثی (Neutral) — خاکستری متعادل**
```
Neutral-50:  #FAFAFA | hsl(0, 0%, 98%)
Neutral-100: #F5F5F5 | hsl(0, 0%, 96%)
Neutral-200: #E5E5E5 | hsl(0, 0%, 90%)
Neutral-300: #D4D4D4 | hsl(0, 0%, 83%)
Neutral-400: #A3A3A3 | hsl(0, 0%, 64%)
Neutral-500: #737373 | hsl(0, 0%, 45%)
Neutral-600: #525252 | hsl(0, 0%, 32%)
Neutral-700: #404040 | hsl(0, 0%, 25%)
Neutral-800: #262626 | hsl(0, 0%, 15%)
Neutral-900: #171717 | hsl(0, 0%, 9%)
```

### ۲.۴ توزیع رنگ (60-30-10 Rule)

```
۶۰٪ — Neutral (پس‌زمینه، متن‌های بدنه، فضای سفید)
  Light Mode: Neutral-50, Neutral-100
  Dark Mode: Neutral-900, Neutral-800

۳۰٪ — Primary (هدرها، دکمه‌های اصلی، ناوبری)
  Primary-500, Primary-600

۱۰٪ — Accent + Warmth (هایلایت، CTA، گرادینت‌ها)
  Accent-500, Warmth-500
```

### ۲.۵ Light Mode vs Dark Mode

#### **Light Mode (پیش‌فرض)**
```
Background: Neutral-50 (#FAFAFA)
Surface: #FFFFFF
Text Primary: Neutral-900 (#171717)
Text Secondary: Neutral-600 (#525252)
Border: Neutral-200 (#E5E5E5)
```

#### **Dark Mode**
```
Background: Neutral-900 (#171717)
Surface: Neutral-800 (#262626)
Text Primary: Neutral-50 (#FAFAFA)
Text Secondary: Neutral-400 (#A3A3A3)
Border: Neutral-700 (#404040)
```

### ۲.۶ گرادینت‌های ویژه

#### **Gradient 1: Hero Mesh**
```css
background: linear-gradient(
  135deg,
  hsl(217, 91%, 60%) 0%,
  hsl(271, 91%, 65%) 50%,
  hsl(25, 95%, 53%) 100%
);
```

#### **Gradient 2: Card Glassmorphism**
```css
background: linear-gradient(
  135deg,
  rgba(59, 130, 246, 0.1) 0%,
  rgba(168, 85, 247, 0.05) 100%
);
backdrop-filter: blur(20px);
border: 1px solid rgba(255, 255, 255, 0.2);
```

#### **Gradient 3: Success Glow**
```css
background: radial-gradient(
  circle at center,
  rgba(16, 185, 129, 0.2) 0%,
  transparent 70%
);
```

---

## ۳. تایپوگرافی و فونت‌ها

### ۳.۱ فونت‌های اصلی

#### **فونت فارسی — Vazirmatn**
```
فونت: Vazirmatn Variable
منبع: https://github.com/rastikerdar/vazirmatn
مجوز: SIL Open Font License
فرمت: WOFF2 Variable

وزن‌های مورد استفاده:
- Thin (100) — برای دیسپلی بسیار بزرگ
- ExtraLight (200) — زیرتیترهای ظریف
- Light (300) — متن‌های سبک
- Regular (400) — متن بدنه پایه
- Medium (500) — تأکیدهای متوسط
- SemiBold (600) — عناوین کوچک
- Bold (700) — عناوین اصلی
- ExtraBold (800) — تیترهای Hero
- Black (900) — دیسپلی‌های قوی
```

#### **فونت انگلیسی و اعداد — Inter**
```
فونت: Inter Variable
منبع: https://rsms.me/inter/
مجوز: SIL Open Font License
فرمت: WOFF2 Variable

ویژگی‌ها:
- Font Feature Settings: 'tnum' on (Tabular Numbers)
- پشتیبانی از OpenType Features
- بهینه‌سازی شده برای UI و صفحه‌نمایش

وزن‌های مورد استفاده: 300, 400, 500, 600, 700, 800
```

#### **فونت مونو — JetBrains Mono**
```
فونت: JetBrains Mono
استفاده: کدها، اعداد مالی، توکن‌ها، لاگ‌ها

وزن‌های مورد استفاده: 400, 500, 700
ویژگی: Ligatures برای کدنویسی
```

### ۳.۲ مقیاس تایپوگرافی (Type Scale)

#### **سیستم نامگذاری**
```
Display: تیترهای بسیار بزرگ (Hero)
Heading: عناوین اصلی (H1-H6)
Body: متن بدنه
Caption: متن‌های کوچک و توضیحی
```

#### **جدول مقیاس**

| سطح | نام | سایز | وزن | ارتفاع خط | فاصله حروف | استفاده |
|-----|-----|------|-----|-----------|------------|----------|
| **Display** |
| XL | Display-XL | 64px / 4rem | 800 | 1.1 (110%) | -0.02em | Hero تیتر اصلی |
| LG | Display-LG | 52px / 3.25rem | 800 | 1.15 (115%) | -0.015em | Hero زیرتیتر |
| MD | Display-MD | 44px / 2.75rem | 700 | 1.2 (120%) | -0.01em | Section تیترهای |
| **Heading** |
| H1 | Heading-1 | 36px / 2.25rem | 700 | 1.25 (125%) | -0.01em | عنوان صفحه |
| H2 | Heading-2 | 30px / 1.875rem | 700 | 1.3 (130%) | -0.005em | عنوان بخش |
| H3 | Heading-3 | 24px / 1.5rem | 600 | 1.35 (135%) | 0 | زیربخش |
| H4 | Heading-4 | 20px / 1.25rem | 600 | 1.4 (140%) | 0 | کارت تیتر |
| H5 | Heading-5 | 18px / 1.125rem | 600 | 1.45 (145%) | 0 | لیست تیتر |
| H6 | Heading-6 | 16px / 1rem | 600 | 1.5 (150%) | 0 | زیرعنوان کوچک |
| **Body** |
| LG | Body-LG | 18px / 1.125rem | 400 | 1.6 (160%) | 0 | متن مقدماتی |
| MD | Body-MD | 16px / 1rem | 400 | 1.65 (165%) | 0 | متن پایه |
| SM | Body-SM | 14px / 0.875rem | 400 | 1.7 (170%) | 0 | متن کوچک |
| **Caption** |
| MD | Caption-MD | 14px / 0.875rem | 500 | 1.5 (150%) | 0.01em | برچسب، Badge |
| SM | Caption-SM | 12px / 0.75rem | 500 | 1.5 (150%) | 0.015em | توضیحات |
| XS | Caption-XS | 10px / 0.625rem | 500 | 1.4 (140%) | 0.02em | متادیتا |

### ۳.۳ قوانین تایپوگرافی

#### **فاصله‌گذاری عمودی (Vertical Rhythm)**
```
Base Line Height: 1.65 (برای Body-MD)
Spacing Unit: 8px (0.5rem)

فواصل بین المان‌ها:
Tight: 8px (0.5rem)
Normal: 16px (1rem)
Relaxed: 24px (1.5rem)
Loose: 32px (2rem)
```

#### **عرض ماکزیمم متن (Max Width)**
```
Body Text: 65-75 کاراکتر (تقریباً 680px)
Heading: 100% (بدون محدودیت)
Caption: 50-60 کاراکتر (تقریباً 520px)
```

#### **Hierarchy وزن فونت**
```
Display: 700-900 (Bold to Black)
Heading: 600-700 (SemiBold to Bold)
Body: 400 (Regular)
Caption/Label: 500-600 (Medium to SemiBold)
```

### ۳.۴ نمونه کدهای CSS

```css
/* Display XL */
.display-xl {
  font-family: 'Vazirmatn', sans-serif;
  font-size: 4rem; /* 64px */
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.02em;
}

/* Heading 2 */
.heading-2 {
  font-family: 'Vazirmatn', sans-serif;
  font-size: 1.875rem; /* 30px */
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -0.005em;
}

/* Body MD */
.body-md {
  font-family: 'Vazirmatn', sans-serif;
  font-size: 1rem; /* 16px */
  font-weight: 400;
  line-height: 1.65;
  letter-spacing: 0;
}

/* Numeric (Tabular) */
.numeric {
  font-family: 'Inter', sans-serif;
  font-feature-settings: 'tnum' on;
  font-variant-numeric: tabular-nums;
}

/* Code/Mono */
.mono {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5;
}
```

---

## ۴. کپی‌رایتینگ و متون سایت

### ۴.۱ Hero Section

#### **تیتر اصلی (Hero Headline)**
```
فارسی:
«منشی هوشمندی که توی همون پیامرسانت کار می‌کنه —
بدون پنل، بدون سردرگمی، فقط فروش»

انگلیسی (اختیاری برای برند):
"Your AI Assistant Lives in Your Messenger —
No Dashboard, No Confusion, Just Sales"
```

**تحلیل:**
- **تکان‌دهنده:** مفهوم «منشی توی پیامرسان» غیرمنتظره است
- **ملموس:** «بدون پنل» درد واقعی کاسبان سنتی را حل می‌کند
- **واضح:** «فقط فروش» نتیجه نهایی را نشان می‌دهد

#### **زیرتیتر (Hero Subheadline)**
```
«از این لحظه، هر پیام مشتری‌ات می‌تونه تبدیل به فاکتور بشه،
هر فاکتور به لینک پرداخت، و هر پرداخت به پول واقعی توی حسابت —
بدون اینکه یه دفعه هم وارد پنل بشی.»
```

**تحلیل:**
- **سفر مشتری:** مسیر کامل از پیام تا پول را نشان می‌دهد
- **تأکید بر واقعیت:** «پول واقعی توی حسابت»
- **تکرار تمایز:** «بدون اینکه یه دفعه هم وارد پنل بشی»

### ۴.۲ Value Propositions (۳ ستون)

#### **ستون ۱: Zero-UI**
```
عنوان: «بدون پنل، بدون سردرگمی»

متن:
«همون جایی که با مشتری‌هات حرف می‌زنی،
همونجا فاکتور صادر کن، لینک پرداخت بفرست و پول دریافت کن.
نه لاگین، نه رمز عبور، نه آموزش —
فقط یه گفتگوی ساده توی تلگرام یا روبیکا.»

آیکون: 💬 (Message Bubble)
```

#### **ستون ۲: Real Money**
```
عنوان: «پول واقعی، نه ادعا»

متن:
«فراموش کن که بگی "فلانی گفت واریز کرده ولی پیدا نکردم".
سیستم ما مستقیم با API درگاه صحبت می‌کنه —
فقط وقتی درگاه تأیید کنه که تراکنش واقعیه، پول ثبت می‌شه.
صفر خطا، صفر دروغ، صد درصد اعتماد.»

آیکون: ✅ (Verified Check)
```

#### **ستون ۳: Academy CRM**
```
عنوان: «CRM زنده برای آموزشگاه»

متن:
«ثبت‌نام هنرجو، صدور کارنامه، برگزاری آزمون،
حسابداری دوبل داخلی، ربات تلگرام و کوپایلوت هوش مصنوعی —
همه‌اش توی یه سیستم یکپارچه.
کرمانشاهکارت باهاش ۱۲۰۰ هنرجو مدیریت می‌کنه.»

آیکون: 🎓 (Graduation Cap)
```

### ۴.۳ دکمه‌های CTA (Call to Action)

#### **CTA اصلی (Primary CTAs)**
```
Hero:
- «مشاهده دموی زنده» (Watch Live Demo)
- «منشی من را روشن کن» (Activate My Assistant)

Pricing:
- «شروع آزمایشی رایگان» (Start Free Trial)

Contact:
- «درخواست راه‌اندازی سریع» (Request Quick Setup)
```

#### **CTA ثانویه (Secondary CTAs)**
```
- «مشاهده تعرفه‌ها» (View Pricing)
- «مطالعه Case Study کرمانشاهکارت» (Read Case Study)
- «محاسبه میزان صرفه‌جویی من» (Calculate My Savings)
- «دانلود کاتالوگ PDF» (Download Catalog)
```

#### **CTA پیامرسان (Messenger CTAs)**
```
- «شروع در تلگرام» + آیکون تلگرام
- «شروع در روبیکا» + آیکون روبیکا

زیرنویس:
«کلیک کن و مستقیم با منشی هوشمند چت کن —
بدون نیاز به ثبت‌نام، بدون فرم.»
```

### ۴.۴ میکروکپی‌ها (Microcopy) — کاهش اضطراب

#### **اطمینان‌بخش مالی**
```
- «بدون نیاز به سواد حسابداری» (برای بخش دفتریار)
- «بدون کارت اعتباری برای آزمایش» (صفحه Pricing)
- «تنها زمانی پول ثبت می‌شود که درگاه تأیید کند» (بخش Financial Engine)
- «لغو در هر لحظه، بدون جریمه» (Pricing FAQ)
```

#### **اطمینان‌بخش فنی**
```
- «نصب خودکار، راه‌اندازی ۳ دقیقه‌ای» (Setup Section)
- «پشتیبانی زنده فارسی، هر روز ۹ صبح تا ۹ شب» (Footer)
- «داده‌هات روی سرورهای ایران، تحت کنترل خودت» (Security Badge)
```

#### **اطمینان‌بخش کسب‌وکار**
```
- «بیش از ۱۵۰۰ تراکنش موفق در ماه گذشته» (Stats Counter)
- «۹۸٪ مشتری‌ها می‌گن سردرگمی‌شون کاهش یافته» (Testimonial Section)
- «میانگین افزایش ۴۵٪ در سرعت دریافت وجه» (ROI Calculator)
```

### ۴.۵ متون بخش Features

#### **Feature 1: منشی محاورهای**
```
عنوان: «منشی که فارسی حرف می‌زنه»

متن:
«حتی پیام صوتی مشتری رو می‌فهمه، فاکتور می‌سازه و بهش جواب می‌ده.
دیگه لازم نیست شب‌ها بیدار بمونی تا به پیام‌ها جواب بدی —
منشی هوشمندت ۲۴ساعته پای کاره.»
```

#### **Feature 2: موتور دفتریار**
```
عنوان: «دفتر پول بدون نیاز به دست‌خط»

متن:
«هر تراکنش، هر دریافت، هر پرداخت —
همه‌شون خودکار توی دفتر دوبل ثبت می‌شن.
دیگه نیازی نیست شب‌ها دفتر بچرخونی یا با اکسل کلنجار بری.»
```

#### **Feature 3: اتصال قطعی درگاه**
```
عنوان: «فقط وقتی درگاه بگه آره»

متن:
«دیگه نگران جعلی‌ها نباش.
سیستم ما مستقیم از API درگاه می‌پرسه "این پرداخت واقعیه؟"
اگه جواب آره بود، اونوقت ثبت می‌شه. اگه نه، حتی توی لیست نمیاد.»
```

#### **Feature 4: مدیریت هنرجویان**
```
عنوان: «از ثبت‌نام تا کارنامه، همه‌جا»

متن:
«ثبت‌نام هنرجو، تعریف دوره، برگزاری آزمون و صدور کارنامه —
همه توی یه سیستم.
کرمانشاهکارت الان ۱۲۰۰ نفر رو با همین سیستم مدیریت می‌کنه.»
```

#### **Feature 5: ربات تلگرام یکپارچه**
```
عنوان: «ربات اختصاصی برای هنرجوهات»

متن:
«هنرجوها می‌تونن توی تلگرام کارناماشونو ببینن،
برای آزمون ثبت‌نام کنن و حتی شهریه بدن —
بدون نیاز به تماس یا مراجعه حضوری.»
```

#### **Feature 6: کوپایلوت AI (Gemini)**
```
عنوان: «دستیار هوشمند برای تصمیم‌های بهتر»

متن:
«از کوپایلوت هوش مصنوعی بپرس "کدوم دوره بیشترین فروش رو داشته؟"
یا "چه هنرجوهایی شهریه‌شونو ندادن؟"
اون بهت جواب می‌ده، نه تو باید گزارش بچرخونی.»
```

### ۴.۶ متن Comparison Table

#### **هدر ستون‌ها**
```
| ویژگی | روش سنتی (دفتر + اکسل) | پنل‌های پیچیده | سایفر (Cypher) |
```

#### **ردیف‌ها**
```
| سهولت استفاده | ⚠️ نیاز به آموزش و دقت بالا | ⚠️ نیاز به آموزش متوسط | ✅ صفر آموزش، فقط چت |
| اتصال درگاه پرداخت | ❌ کپی‌پیست دستی کد پیگیری | 🔶 نیمه‌خودکار (ادعایی) | ✅ خودکار کامل با API |
| تأیید واقعی تراکنش | ❌ بر اساس گفته مشتری | 🔶 گزارش متنی از درگاه | ✅ تأیید لحظه‌ای از API |
| محل کار | 📒 دفترچه فیزیکی یا اکسل | 🌐 پنل جداگانه در مرورگر | 💬 همان پیامرسان شما |
| گزارش‌گیری | ❌ دستی، زمان‌بر | 🔶 گزارش‌های از پیش تعریف‌شده | ✅ کوپایلوت AI برای هر سؤال |
| پشتیبانی | ❌ خودت | 🔶 تیکت (گاهی چند روز طول می‌کشد) | ✅ چت زنده فارسی، هر روز |
| هزینه راه‌اندازی | رایگان (ولی خطا پرهزینه) | معمولاً بالا | ✅ آزمایشی رایگان، اشتراک منعطف |
| قابلیت مقیاس‌پذیری | ❌ محدود به زمان شما | 🔶 بستگی به پلن دارد | ✅ نامحدود در همه پلن‌ها |
```

### ۴.۷ Testimonials (نمونه)

#### **Testimonial 1: آموزشگاه کرمانشاهکارت**
```
متن:
«قبلاً هر روز باید ۳-۴ ساعت وقت می‌ذاشتم برای چک کردن واریزی‌ها و ثبت‌نام‌ها.
الان همه‌اش خودکاره. ربات تلگرام ثبت‌نام می‌کنه، درگاه خودش چک می‌کنه،
و من فقط گزارش نهایی رو می‌بینم.
۱۲۰۰ هنرجو داریم و هیچ سردرگمی‌ای نیست.»

نام: سینا م.
سمت: مدیر فنی، آموزشگاه کرمانشاهکارت
عکس: [آواتار یا لوگو آموزشگاه]
```

#### **Testimonial 2: باشگاه ورزشی**
```
متن:
«مشتری‌ها توی تلگرام پیام می‌دن "می‌خوام برای ماه آینده تمدید کنم"،
منشی هوشمند بهشون لینک پرداخت می‌ده، اونا می‌پردازن و تمام.
من حتی نمی‌دونستم این همه راحت میشه!»

نام: رضا ک.
سمت: صاحب باشگاه بدنسازی، تهران
عکس: [آواتار]
```

#### **Testimonial 3: فروشگاه محلی**
```
متن:
«قبلاً مشتری می‌گفت "واریز کردم" و من باید می‌رفتم بانک چک کنم.
حالا سیستم خودش می‌گه "این پرداخت تأیید شد" یا نشد.
دیگه استرس ندارم که کسی دروغ بگه یا اشتباه بشه.»

نام: مریم ا.
سمت: صاحب فروشگاه لوازم خانگی، اصفهان
عکس: [آواتار]
```

### ۴.۸ FAQ Pricing (میکروکپی)

```
س: آیا برای دوره آزمایشی نیاز به کارت اعتباری دارم؟
ج: نه، اصلاً. فقط روی "شروع رایگان" کلیک کن و توی تلگرام یا روبیکا شروع کن.

س: اگه راضی نشدم، چطور لغو کنم؟
ج: در هر لحظه می‌تونی از طریق همون پیامرسان بگی "لغو اشتراک" و تمام. بدون جریمه، بدون سؤال.

س: داده‌های مالی من امن هست؟
ج: صد در صد. همه داده‌ها روی سرورهای ایران ذخیره می‌شن، رمزنگاری شده‌ان،
   و هیچ شخص ثالثی بدون اجازه شما دسترسی نداره.

س: اگه مشکل فنی پیش بیاد، چی کار کنم؟
ج: تیم پشتیبانی فارسی‌زبان ما هر روز از ۹ صبح تا ۹ شب آماده‌ست.
   فقط توی همون پیامرسان بنویس "پشتیبانی" و یکی از تیم بهت جواب می‌ده.
```

---

## ۵. زبان بصری، موتیف‌ها و انیمیشن‌ها

### ۵.۱ فلسفه بصری

**تم کلی: "Cyber Warm" — ترکیب فناوری مدرن و گرمای انسانی**

```
مفاهیم کلیدی:
✦ Glassmorphism: شفافیت و عمق برای کارت‌ها و Modal‌ها
✦ Mesh Gradients: گرادینت‌های نرم و پویا برای پس‌زمینه‌های Hero
✦ Floating Elements: عناصر شناور با سایه‌های نرم
✦ Micro-interactions: انیمیشن‌های کوچک و زنده برای کلیک، هاور، اسکرول
✦ Data Visualization: نمودارها و چارت‌های نئونی زنده
✦ Neon Highlights: خطوط و نقاط نئونی برای تأکید بر نقاط کلیدی
```

### ۵.۲ Glassmorphism Cards

```css
.glass-card {
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.1),
    rgba(255, 255, 255, 0.05)
  );
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 16px;
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

/* Dark Mode Variant */
.glass-card-dark {
  background: linear-gradient(
    135deg,
    rgba(23, 23, 23, 0.7),
    rgba(38, 38, 38, 0.5)
  );
  border: 1px solid rgba(255, 255, 255, 0.1);
}
```

**استفاده:**
- کارت‌های فیچرها
- Modal‌های تعاملی
- Tooltip‌ها
- Navigation Bar (Sticky Header)

### ۵.۳ Mesh Gradient Backgrounds

#### **Hero Mesh (پس‌زمینه اصلی)**
```css
.hero-mesh {
  background: 
    radial-gradient(at 27% 37%, hsla(215, 98%, 61%, 0.3) 0px, transparent 50%),
    radial-gradient(at 97% 21%, hsla(125, 98%, 72%, 0.2) 0px, transparent 50%),
    radial-gradient(at 52% 99%, hsla(354, 98%, 61%, 0.2) 0px, transparent 50%),
    radial-gradient(at 10% 29%, hsla(256, 96%, 67%, 0.3) 0px, transparent 50%),
    radial-gradient(at 97% 96%, hsla(38, 60%, 74%, 0.2) 0px, transparent 50%),
    radial-gradient(at 33% 50%, hsla(222, 67%, 73%, 0.3) 0px, transparent 50%),
    radial-gradient(at 79% 53%, hsla(343, 68%, 79%, 0.2) 0px, transparent 50%);
  
  /* Animation */
  background-size: 200% 200%;
  animation: meshMove 20s ease infinite;
}

@keyframes meshMove {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
```

#### **Section Gradient (بخش‌های میانی)**
```css
.section-gradient {
  background: linear-gradient(
    180deg,
    hsl(217, 91%, 60%, 0.05) 0%,
    transparent 100%
  );
}
```

### ۵.۴ Floating Cards & Shadows

```css
.floating-card {
  border-radius: 16px;
  box-shadow:
    0 2px 4px rgba(0, 0, 0, 0.02),
    0 8px 16px rgba(0, 0, 0, 0.04),
    0 16px 32px rgba(0, 0, 0, 0.06);
  
  transition: 
    transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1),
    box-shadow 0.3s ease;
}

.floating-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow:
    0 4px 8px rgba(0, 0, 0, 0.04),
    0 16px 32px rgba(0, 0, 0, 0.08),
    0 32px 64px rgba(0, 0, 0, 0.12);
}
```

**استفاده:**
- کارت‌های فیچر
- کارت‌های Pricing
- کارت‌های Testimonial

### ۵.۵ Neon Highlights & Glow Effects

```css
.neon-border {
  border: 2px solid transparent;
  background: 
    linear-gradient(var(--surface-color), var(--surface-color)) padding-box,
    linear-gradient(135deg, hsl(217, 91%, 60%), hsl(271, 91%, 65%)) border-box;
  border-radius: 12px;
}

.neon-glow {
  box-shadow:
    0 0 10px hsla(217, 91%, 60%, 0.3),
    0 0 20px hsla(217, 91%, 60%, 0.2),
    0 0 40px hsla(217, 91%, 60%, 0.1);
}

.neon-text {
  color: hsl(271, 91%, 65%);
  text-shadow:
    0 0 10px hsla(271, 91%, 65%, 0.5),
    0 0 20px hsla(271, 91%, 65%, 0.3);
}
```

**استفاده:**
- دکمه‌های Primary CTA
- Badge‌های "New" یا "Popular"
- آیکون‌های فعال (Active State)

### ۵.۶ آیکونوگرافی (Iconography)

#### **استایل آیکون‌ها**
```
کتابخانه: Lucide Icons (یا Phosphor Icons)
استایل: Outline (خطی) با ضخامت ۲px
سایز پایه: 24×24px
رنگ پایه: Primary-600 (تم روشن) / Primary-400 (تم تاریک)

سایزهای مختلف:
- Small: 16×16px (برای Caption و Inline)
- Medium: 24×24px (پایه، برای Body)
- Large: 32×32px (برای Heading و Feature Cards)
- XLarge: 48×48px (برای Hero Icons)
```

#### **آیکون‌های کلیدی پروژه**
```
💬 Message Bubble → منشی محاورهای
✅ Verified Check → تأیید واقعی پرداخت
🎓 Graduation Cap → CRM آموزشگاه
💳 Credit Card → درگاه پرداخت
📊 Chart → داشبورد و گزارش‌ها
🤖 Robot → AI Copilot
⚡ Lightning → سرعت و خودکارسازی
🔒 Lock → امنیت
🌐 Globe → دسترسی همه‌جا
💎 Diamond → ویژگی Premium
```

#### **وضعیت‌های آیکون (Icon States)**
```css
/* Default */
.icon-default {
  color: hsl(0, 0%, 45%);
  transition: color 0.2s ease;
}

/* Hover */
.icon-default:hover {
  color: hsl(217, 91%, 60%);
}

/* Active */
.icon-active {
  color: hsl(217, 91%, 60%);
  filter: drop-shadow(0 0 8px hsla(217, 91%, 60%, 0.4));
}

/* Success */
.icon-success {
  color: hsl(158, 64%, 52%);
}

/* Error */
.icon-error {
  color: hsl(0, 72%, 51%);
}
```

### ۵.۷ موشن و انیمیشن‌ها (Motion & Animations)

#### **اصول موشن**
```
سرعت پایه: 300ms
Easing: cubic-bezier(0.4, 0.0, 0.2, 1) — Material Design Standard

طبقه‌بندی:
- Micro (0-300ms): Hover, Click, Toggle
- Transition (300-500ms): Page Section, Modal Open/Close
- Animation (500ms-2s): Loading, Success Celebration, Hero Elements
- Ambient (2s+): Background Mesh, Floating Elements
```

#### **انیمیشن ۱: دموی چت تعاملی (Interactive Chat Demo)**

**سناریو:**
```
1. پیام مشتری (صوتی): "سلام، می‌خوام برای دوره کارت‌خوانی ثبت‌نام کنم"
   → انیمیشن: ظاهر شدن حباب پیام از سمت راست با Fade + Slide
   → Typing Indicator (۳ نقطه متحرک) برای ۱.۵ ثانیه

2. پاسخ منشی هوشمند:
   "سلام! حتماً. دوره کارت‌خوانی ۲ میلیون تومن هست.
    می‌خوای الان لینک پرداخت بفرستم؟"
   → انیمیشن: ظاهر شدن حباب پاسخ از سمت چپ با Fade + Slide
   → Typing effect (حرف به حرف) با سرعت ۳۰ms/حرف

3. پیام مشتری: "بله لطفاً"
   → انیمیشن مشابه مرحله ۱

4. پاسخ منشی + لینک پرداخت:
   "لینک پرداخت شما: [لینک کلیک‌پذیر]
    بعد از پرداخت، ثبت‌نام شما قطعی می‌شه."
   → انیمیشن: ظاهر شدن لینک با Glow Effect نئونی
   → دکمه "پرداخت" با Pulse Animation

5. شبیه‌سازی کلیک روی لینک:
   → Transition به صفحه درگاه (فید شدن کل چت و ظاهر شدن Mock Gateway)
   → لودینگ ۲ ثانیه‌ای
   → پیام موفقیت با آیکون ✅ و Confetti Animation (ریزش کاغذهای رنگی)

6. بازگشت به چت:
   پیام سیستم: "پرداخت شما با موفقیت تأیید شد. کد پیگیری: 123456789"
   → انیمیشن: Success Badge با Scale + Glow
```

**کد انیمیشن نمونه:**
```css
/* Typing Indicator */
@keyframes typingDot {
  0%, 60%, 100% { transform: translateY(0); }
  30% { transform: translateY(-10px); }
}

.typing-indicator span {
  animation: typingDot 1.4s infinite;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 0.4s;
}

/* Message Appear */
@keyframes messageAppear {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.message-bubble {
  animation: messageAppear 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Pulse Button */
@keyframes pulse {
  0%, 100% {
    box-shadow: 0 0 0 0 hsla(217, 91%, 60%, 0.7);
  }
  50% {
    box-shadow: 0 0 0 10px hsla(217, 91%, 60%, 0);
  }
}

.btn-pulse {
  animation: pulse 2s infinite;
}
```

#### **انیمیشن ۲: شبیه‌ساز تبدیل پیام صوتی به فاکتور**

**سناریو بصری:**
```
1. آیکون پیام صوتی (🎤) در مرکز
   → Glow Effect
   
2. موج صوتی متحرک (Waveform Animation)
   → ۱.۵ ثانیه
   
3. Morph Transition:
   آیکون پیام صوتی → آیکون فاکتور (📄)
   → با استفاده از SVG Morph یا Scale + Rotate
   
4. فاکتور کامل ظاهر می‌شود:
   - شماره فاکتور
   - آیتم: دوره کارت‌خوانی
   - مبلغ: ۲,۰۰۰,۰۰۰ تومان
   - دکمه "صدور لینک پرداخت"
   
5. کلیک روی دکمه:
   → انیمیشن Loading (Spinner یا Progress Bar)
   → ظاهر شدن لینک پرداخت با Copy Button
   → Success Checkmark
```

**کد نمونه Morph:**
```css
@keyframes morphToInvoice {
  0% {
    transform: scale(1) rotate(0deg);
    opacity: 1;
  }
  50% {
    transform: scale(0) rotate(180deg);
    opacity: 0;
  }
  51% {
    transform: scale(0) rotate(0deg);
  }
  100% {
    transform: scale(1) rotate(0deg);
    opacity: 1;
  }
}

.icon-transform {
  animation: morphToInvoice 1s ease-in-out;
}
```

#### **انیمیشن ۳: نمودار رشد تراکنش‌ها (Live Chart Animation)**

```javascript
// فرض: استفاده از Chart.js یا D3.js

const chartAnimation = {
  duration: 2000,
  easing: 'easeOutQuart',
  delay: (context) => context.dataIndex * 100,
  
  // هر ستون نمودار به تدریج از پایین به بالا رشد می‌کند
  onProgress: (animation) => {
    // Glow effect در حین انیمیشن
  }
};

// نمودار خطی با Gradient Fill
const gradientFill = ctx.createLinearGradient(0, 0, 0, 400);
gradientFill.addColorStop(0, 'hsla(217, 91%, 60%, 0.3)');
gradientFill.addColorStop(1, 'hsla(217, 91%, 60%, 0)');
```

#### **انیمیشن ۴: Scroll-triggered Animations**

```css
/* استفاده از Intersection Observer + CSS */

.fade-in-up {
  opacity: 0;
  transform: translateY(40px);
  transition: 
    opacity 0.6s cubic-bezier(0.34, 1.56, 0.64, 1),
    transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.fade-in-up.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger Effect (تأخیر پله‌ای) */
.feature-card:nth-child(1) { transition-delay: 0ms; }
.feature-card:nth-child(2) { transition-delay: 100ms; }
.feature-card:nth-child(3) { transition-delay: 200ms; }
.feature-card:nth-child(4) { transition-delay: 300ms; }
```

**موارد استفاده:**
- کارت‌های فیچر هنگام اسکرول
- آیتم‌های Comparison Table
- Testimonial Cards

#### **انیمیشن ۵: Loading States**

```css
/* Skeleton Loading */
@keyframes skeleton-loading {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}

.skeleton {
  background: linear-gradient(
    90deg,
    hsl(0, 0%, 90%) 25%,
    hsl(0, 0%, 95%) 50%,
    hsl(0, 0%, 90%) 75%
  );
  background-size: 200% 100%;
  animation: skeleton-loading 1.5s ease-in-out infinite;
}

/* Spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}

.spinner {
  border: 3px solid rgba(59, 130, 246, 0.1);
  border-top-color: hsl(217, 91%, 60%);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 0.8s linear infinite;
}
```

#### **انیمیشن ۶: Success Celebration (تأیید پرداخت)**

```css
/* Confetti Animation */
@keyframes confetti-fall {
  0% {
    transform: translateY(-100vh) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: translateY(100vh) rotate(720deg);
    opacity: 0;
  }
}

.confetti {
  position: absolute;
  width: 10px;
  height: 10px;
  background: hsl(158, 64%, 52%);
  animation: confetti-fall 3s ease-out forwards;
}

/* Checkmark Draw */
@keyframes checkmark-draw {
  0% {
    stroke-dashoffset: 100;
  }
  100% {
    stroke-dashoffset: 0;
  }
}

.checkmark-path {
  stroke-dasharray: 100;
  animation: checkmark-draw 0.6s ease-out forwards;
}
```

### ۵.۸ Responsive Behavior

#### **Breakpoints**
```css
/* Mobile First Approach */

/* Extra Small (Mobile) */
@media (min-width: 0px) {
  --container-padding: 16px;
  --grid-columns: 1;
}

/* Small (Large Mobile) */
@media (min-width: 640px) {
  --container-padding: 24px;
  --grid-columns: 2;
}

/* Medium (Tablet) */
@media (min-width: 768px) {
  --container-padding: 32px;
  --grid-columns: 2;
}

/* Large (Desktop) */
@media (min-width: 1024px) {
  --container-padding: 48px;
  --grid-columns: 3;
}

/* Extra Large (Wide Desktop) */
@media (min-width: 1280px) {
  --container-padding: 64px;
  --grid-columns: 3;
}
```

#### **تایپوگرافی ریسپانسیو**
```css
/* Display XL */
.display-xl {
  font-size: clamp(2.5rem, 5vw + 1rem, 4rem); /* 40px → 64px */
}

/* Heading 1 */
.heading-1 {
  font-size: clamp(1.75rem, 3vw + 0.5rem, 2.25rem); /* 28px → 36px */
}

/* Body MD */
.body-md {
  font-size: clamp(0.875rem, 1vw + 0.5rem, 1rem); /* 14px → 16px */
}
```

---

## ۶. جزئیات کامپوننت‌های کلیدی

### ۶.۱ Navigation Bar (Header)

#### **ساختار**
```
[Logo] ──────────── [منشی بی‌پنل] [موتور مالی] [CRM آموزشگاه] [تعرفه‌ها] ──── [تماس با ما] [شروع رایگان]
```

#### **مشخصات**
```css
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  height: 72px;
  
  /* Glassmorphism */
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  
  /* Shadow on Scroll */
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0);
  transition: box-shadow 0.3s ease;
}

.navbar.scrolled {
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.08);
}

/* Logo */
.navbar-logo {
  font-size: 1.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, hsl(217, 91%, 60%), hsl(271, 91%, 65%));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* Nav Links */
.nav-link {
  font-size: 0.9375rem; /* 15px */
  font-weight: 500;
  color: hsl(0, 0%, 32%);
  transition: color 0.2s ease;
  
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background: hsl(217, 91%, 60%);
  transition: width 0.3s ease;
}

.nav-link:hover {
  color: hsl(217, 91%, 60%);
}

.nav-link:hover::after {
  width: 100%;
}

/* CTA Button */
.navbar-cta {
  padding: 10px 20px;
  background: linear-gradient(135deg, hsl(217, 91%, 60%), hsl(271, 91%, 65%));
  color: white;
  border-radius: 8px;
  font-weight: 600;
  box-shadow: 0 4px 12px hsla(217, 91%, 60%, 0.3);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.navbar-cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px hsla(217, 91%, 60%, 0.4);
}
```

#### **Mobile Menu (Hamburger)**
```
حالت موبایل:
- آیکون همبرگر (☰) سمت راست
- کلیک → Full-Screen Overlay Menu با انیمیشن Slide from Right
- آیتم‌ها به صورت عمودی با Stagger Animation
- دکمه بستن (✕) در بالای راست
```

### ۶.۲ Hero Section

#### **Layout**
```
┌─────────────────────────────────────────────────────┐
│  [Mesh Gradient Background]                         │
│                                                      │
│  ┌──────────────────┐       ┌──────────────────┐   │
│  │                  │       │                  │   │
│  │  تیتر اصلی       │       │  شبیه‌ساز چت    │   │
│  │  زیرتیتر         │       │  (Floating Card) │   │
│  │                  │       │                  │   │
│  │  [CTA 1] [CTA 2] │       │                  │   │
│  │                  │       │                  │   │
│  │  [Trust Badges]  │       │                  │   │
│  └──────────────────┘       └──────────────────┘   │
│                                                      │
└─────────────────────────────────────────────────────┘
```

#### **Trust Badges (زیر CTA)**
```
✓ بدون نیاز به کارت اعتباری
✓ راه‌اندازی ۳ دقیقه‌ای
✓ پشتیبانی فارسی ۷ روز هفته
```

**استایل Badge:**
```css
.trust-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.875rem;
  color: hsl(0, 0%, 45%);
}

.trust-badge svg {
  color: hsl(158, 64%, 52%);
  width: 20px;
  height: 20px;
}
```

### ۶.۳ Feature Cards

#### **ساختار کارت**
```
┌─────────────────────────────┐
│  [Icon 48×48]               │
│                             │
│  عنوان فیچر                 │
│  (Heading-4, SemiBold)      │
│                             │
│  متن توضیحی کوتاه            │
│  (Body-MD, Regular)         │
│                             │
│  [دکمه "بیشتر بخوانید" →]   │
└─────────────────────────────┘
```

#### **استایل**
```css
.feature-card {
  padding: 32px;
  border-radius: 16px;
  background: white;
  border: 1px solid hsl(0, 0%, 90%);
  transition: 
    transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1),
    box-shadow 0.3s ease,
    border-color 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 
    0 16px 32px rgba(0, 0, 0, 0.08),
    0 32px 64px rgba(0, 0, 0, 0.12);
  border-color: hsl(217, 91%, 60%);
}

.feature-card-icon {
  width: 48px;
  height: 48px;
  margin-bottom: 16px;
  
  /* Gradient Background */
  background: linear-gradient(135deg, hsl(217, 91%, 60%), hsl(271, 91%, 65%));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  
  color: white;
  font-size: 24px;
}
```

### ۶.۴ Pricing Cards

#### **Layout (۳ پلن)**
```
┌─────────┐  ┌─────────┐  ┌─────────┐
│ پایه    │  │ حرفه‌ای  │  │ سازمانی │
│         │  │ [محبوب] │  │         │
│ قیمت    │  │ قیمت    │  │ قیمت    │
│         │  │         │  │         │
│ ویژگی‌ها│  │ ویژگی‌ها│  │ ویژگی‌ها│
│         │  │         │  │         │
│ [شروع]  │  │ [شروع]  │  │ [تماس]  │
└─────────┘  └─────────┘  └─────────┘
```

#### **پلن محبوب (Highlighted)**
```css
.pricing-card-popular {
  position: relative;
  border: 2px solid hsl(217, 91%, 60%);
  box-shadow: 
    0 0 0 4px hsla(217, 91%, 60%, 0.1),
    0 16px 32px rgba(0, 0, 0, 0.12);
  
  /* Scale بزرگ‌تر */
  transform: scale(1.05);
}

.pricing-card-popular::before {
  content: 'محبوب‌ترین';
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  
  background: linear-gradient(135deg, hsl(217, 91%, 60%), hsl(271, 91%, 65%));
  color: white;
  padding: 4px 16px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
}
```

#### **لیست ویژگی‌ها**
```html
<ul class="pricing-features">
  <li class="feature-included">✓ منشی محاورهای نامحدود</li>
  <li class="feature-included">✓ ۵۰۰ تراکنش ماهانه</li>
  <li class="feature-included">✓ اتصال یک درگاه</li>
  <li class="feature-excluded">✗ کوپایلوت AI</li>
  <li class="feature-excluded">✗ CRM آموزشگاه</li>
</ul>
```

```css
.pricing-features li {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 0;
  font-size: 0.9375rem;
}

.feature-included {
  color: hsl(0, 0%, 15%);
}

.feature-included::before {
  content: '✓';
  color: hsl(158, 64%, 52%);
  font-weight: 700;
}

.feature-excluded {
  color: hsl(0, 0%, 64%);
  text-decoration: line-through;
}

.feature-excluded::before {
  content: '✗';
  color: hsl(0, 0%, 64%);
}
```

### ۶.۵ Testimonial Cards

#### **Layout**
```
┌─────────────────────────────────┐
│  [Avatar 64×64]  نام شخص        │
│                  سمت / کسب‌وکار │
│                                 │
│  "متن شهادت..."                 │
│                                 │
│  ⭐⭐⭐⭐⭐                         │
└─────────────────────────────────┘
```

#### **استایل**
```css
.testimonial-card {
  padding: 32px;
  border-radius: 16px;
  background: white;
  border: 1px solid hsl(0, 0%, 90%);
  position: relative;
}

/* Quote Mark */
.testimonial-card::before {
  content: '"';
  position: absolute;
  top: 16px;
  right: 16px;
  font-size: 4rem;
  color: hsla(217, 91%, 60%, 0.1);
  font-family: Georgia, serif;
  line-height: 1;
}

.testimonial-avatar {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid hsl(217, 91%, 60%);
}

.testimonial-rating {
  color: hsl(48, 96%, 53%);
  font-size: 1.25rem;
}
```

### ۶.۶ CTA Buttons

#### **Primary CTA**
```css
.btn-primary {
  padding: 14px 32px;
  font-size: 1rem;
  font-weight: 600;
  color: white;
  
  background: linear-gradient(135deg, hsl(217, 91%, 60%), hsl(271, 91%, 65%));
  border: none;
  border-radius: 8px;
  
  box-shadow: 0 4px 12px hsla(217, 91%, 60%, 0.3);
  
  transition: 
    transform 0.2s ease,
    box-shadow 0.2s ease;
  
  cursor: pointer;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px hsla(217, 91%, 60%, 0.4);
}

.btn-primary:active {
  transform: translateY(0);
}
```

#### **Secondary CTA**
```css
.btn-secondary {
  padding: 14px 32px;
  font-size: 1rem;
  font-weight: 600;
  
  color: hsl(217, 91%, 60%);
  background: white;
  border: 2px solid hsl(217, 91%, 60%);
  border-radius: 8px;
  
  transition: 
    background-color 0.2s ease,
    color 0.2s ease;
  
  cursor: pointer;
}

.btn-secondary:hover {
  background: hsl(217, 91%, 60%);
  color: white;
}
```

#### **Ghost Button (متن + آیکون)**
```css
.btn-ghost {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  
  padding: 10px 16px;
  font-size: 0.9375rem;
  font-weight: 600;
  color: hsl(217, 91%, 60%);
  
  background: transparent;
  border: none;
  
  transition: gap 0.2s ease;
  cursor: pointer;
}

.btn-ghost:hover {
  gap: 12px;
}

.btn-ghost svg {
  transition: transform 0.2s ease;
}

.btn-ghost:hover svg {
  transform: translateX(4px);
}
```

### ۶.۷ Footer

#### **ساختار**
```
┌───────────────────────────────────────────────────┐
│  [Logo + توضیح کوتاه]                             │
│                                                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │ محصولات  │  │ پشتیبانی │  │ ارتباط   │        │
│  │ - منشی   │  │ - راهنما │  │ - تلگرام │        │
│  │ - CRM    │  │ - وبلاگ  │  │ - روبیکا │        │
│  │ - تعرفه  │  │ - تماس   │  │ - ایمیل  │        │
│  └──────────┘  └──────────┘  └──────────┘        │
│                                                   │
│  ──────────────────────────────────────────────   │
│                                                   │
│  © ۱۴۰۳ سایفر (Cypher) — تمامی حقوق محفوظ است    │
│  [حریم خصوصی] [شرایط استفاده] [امنیت]           │
└───────────────────────────────────────────────────┘
```

#### **استایل**
```css
.footer {
  background: hsl(0, 0%, 9%);
  color: hsl(0, 0%, 83%);
  padding: 64px 0 32px;
}

.footer-logo {
  font-size: 1.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, hsl(217, 91%, 60%), hsl(271, 91%, 65%));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 16px;
}

.footer-link {
  color: hsl(0, 0%, 64%);
  transition: color 0.2s ease;
}

.footer-link:hover {
  color: hsl(217, 91%, 60%);
}

.footer-bottom {
  border-top: 1px solid hsl(0, 0%, 25%);
  padding-top: 24px;
  margin-top: 48px;
  text-align: center;
  font-size: 0.875rem;
  color: hsl(0, 0%, 64%);
}
```

---

## ۷. دستورالعمل‌های پیاده‌سازی

### ۷.۱ فایل‌های CSS پیشنهادی

```
styles/
├── reset.css          # CSS Reset (مثل normalize.css)
├── tokens.css         # Design Tokens (متغیرهای رنگ، فونت، فواصل)
├── typography.css     # قوانین تایپوگرافی
├── components/
│   ├── buttons.css
│   ├── cards.css
│   ├── navbar.css
│   ├── footer.css
│   └── animations.css
├── sections/
│   ├── hero.css
│   ├── features.css
│   ├── pricing.css
│   └── testimonials.css
└── utilities.css      # کلاس‌های کمکی (spacing, colors, etc.)
```

### ۷.۲ Design Tokens (نمونه)

```css
:root {
  /* Colors - Primary */
  --color-primary-50: hsl(214, 100%, 97%);
  --color-primary-500: hsl(217, 91%, 60%);
  --color-primary-600: hsl(221, 83%, 53%);
  
  /* Colors - Accent */
  --color-accent-500: hsl(271, 91%, 65%);
  --color-accent-600: hsl(271, 81%, 56%);
  
  /* Colors - Warmth */
  --color-warmth-500: hsl(25, 95%, 53%);
  
  /* Colors - Semantic */
  --color-success: hsl(158, 64%, 52%);
  --color-warning: hsl(48, 96%, 53%);
  --color-error: hsl(0, 72%, 51%);
  
  /* Colors - Neutral */
  --color-neutral-50: hsl(0, 0%, 98%);
  --color-neutral-900: hsl(0, 0%, 9%);
  
  /* Typography */
  --font-primary: 'Vazirmatn', sans-serif;
  --font-secondary: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  /* Font Sizes */
  --text-display-xl: 4rem;
  --text-heading-1: 2.25rem;
  --text-body-md: 1rem;
  --text-caption-sm: 0.75rem;
  
  /* Spacing */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-4: 1rem;     /* 16px */
  --space-8: 2rem;     /* 32px */
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  
  /* Shadows */
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.02);
  --shadow-md: 0 8px 16px rgba(0, 0, 0, 0.04);
  --shadow-lg: 0 16px 32px rgba(0, 0, 0, 0.08);
  
  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 300ms ease;
  --transition-slow: 500ms ease;
}
```

### ۷.۳ استراتژی RTL (راست به چپ)

```css
/* Set direction globally */
html {
  direction: rtl;
}

/* Flexbox adjustments */
.flex-row {
  flex-direction: row-reverse;
}

/* Text alignment */
body {
  text-align: right;
}

/* Padding/Margin adjustments */
.btn-ghost svg {
  /* به جای margin-left */
  margin-right: 8px;
}

/* Gradient direction (معکوس برای RTL) */
.hero-mesh {
  background: linear-gradient(
    -135deg, /* معکوس ۱۳۵ */
    /* ... */
  );
}
```

### ۷.۴ Performance Optimization

#### **فونت‌ها**
```html
<!-- Preload Critical Fonts -->
<link rel="preload" href="/fonts/Vazirmatn-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/Inter-Variable.woff2" as="font" type="font/woff2" crossorigin>

<!-- Font Display Swap -->
<style>
  @font-face {
    font-family: 'Vazirmatn';
    src: url('/fonts/Vazirmatn-Variable.woff2') format('woff2-variations');
    font-display: swap;
  }
</style>
```

#### **تصاویر**
```html
<!-- Lazy Loading -->
<img src="feature.jpg" loading="lazy" alt="...">

<!-- Responsive Images -->
<img 
  srcset="
    feature-320.jpg 320w,
    feature-640.jpg 640w,
    feature-1280.jpg 1280w
  "
  sizes="(max-width: 640px) 100vw, 50vw"
  src="feature-640.jpg"
  alt="..."
>

<!-- Modern Formats -->
<picture>
  <source srcset="feature.avif" type="image/avif">
  <source srcset="feature.webp" type="image/webp">
  <img src="feature.jpg" alt="...">
</picture>
```

#### **انیمیشن‌ها**
```css
/* Respect User Preferences */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## ۸. چک‌لیست نهایی طراحی

### ✅ ساختار و محتوا
- [x] نقشه سایت کامل (۶ صفحه اصلی)
- [x] Hierarchy صفحه اصلی (۸ بخش)
- [x] ساختار تمام صفحات فرعی

### ✅ پالت رنگی
- [x] رنگ‌های اصلی (Primary, Accent, Warmth)
- [x] رنگ‌های معنایی (Success, Warning, Error)
- [x] رنگ‌های خنثی (Neutral Scale)
- [x] Light Mode و Dark Mode
- [x] توزیع ۶۰-۳۰-۱۰
- [x] گرادینت‌های ویژه (۳ نوع)

### ✅ تایپوگرافی
- [x] فونت‌های فارسی و انگلیسی
- [x] مقیاس تایپوگرافی کامل (Display, Heading, Body, Caption)
- [x] وزن‌ها و Line Heights
- [x] قوانین Vertical Rhythm
- [x] ریسپانسیو با clamp()

### ✅ کپی‌رایتینگ
- [x] Hero Headlines و Subheadlines
- [x] Value Propositions (۳ ستون)
- [x] دکمه‌های CTA (Primary, Secondary, Ghost)
- [x] میکروکپی‌های اطمینان‌بخش (۹ نمونه)
- [x] متون Features (۶ فیچر)
- [x] Comparison Table
- [x] Testimonials (۳ نمونه)
- [x] FAQ (۴ سؤال)

### ✅ زبان بصری و موشن
- [x] فلسفه بصری (Cyber Warm)
- [x] Glassmorphism
- [x] Mesh Gradients
- [x] Floating Cards
- [x] Neon Highlights
- [x] آیکونوگرافی (۱۰ آیکون کلیدی)
- [x] ۶ سناریوی انیمیشن کامل:
  - دموی چت تعاملی
  - تبدیل پیام صوتی به فاکتور
  - نمودار رشد تراکنش
  - Scroll-triggered Animations
  - Loading States
  - Success Celebration

### ✅ کامپوننت‌ها
- [x] Navigation Bar (+ Mobile Menu)
- [x] Hero Section
- [x] Feature Cards
- [x] Pricing Cards (+ Popular Highlight)
- [x] Testimonial Cards
- [x] CTA Buttons (۳ نوع)
- [x] Footer

### ✅ دستورالعمل‌های فنی
- [x] ساختار فایل‌های CSS
- [x] Design Tokens
- [x] استراتژی RTL
- [x] Performance Optimization
- [x] Responsive Breakpoints

---

## ۹. منابع و ابزارهای پیشنهادی

### طراحی
- **Figma** — برای پروتوتایپ و دیزاین نهایی
- **Spline / Rive** — برای انیمیشن‌های پیشرفته 3D/2D
- **LottieFiles** — برای انیمیشن‌های سبک و بهینه

### فونت‌ها
- **Vazirmatn:** https://github.com/rastikerdar/vazirmatn
- **Inter:** https://rsms.me/inter/
- **JetBrains Mono:** https://www.jetbrains.com/lp/mono/

### رنگ‌ها
- **Coolors.co** — تولید پالت رنگی
- **ColorBox by Lyft** — تولید Color Scale

### انیمیشن و موشن
- **Framer Motion** (React) — کتابخانه انیمیشن
- **GSAP** — کتابخانه انیمیشن قدرتمند JavaScript
- **AOS (Animate On Scroll)** — انیمیشن‌های Scroll-triggered

### آیکون‌ها
- **Lucide Icons:** https://lucide.dev/
- **Phosphor Icons:** https://phosphoricons.com/

### Chart و نمودار
- **Chart.js** — نمودارهای ساده و سریع
- **Recharts** (React) — نمودارهای ترکیبی
- **D3.js** — نمودارهای پیشرفته و سفارشی

---

## ۱۰. نتیجه‌گیری

این سند طراحی سیستم (Design System) یک راهنمای کامل، عملیاتی و زنده برای پیاده‌سازی سایت معرفی محصول و لندینگ پیج **سایفر (Cypher)** است.

### نکات کلیدی:
1. **بدون نیاز به کدنویسی:** تمام مفاهیم به صورت دقیق، بصری و قابل‌اجرا تدوین شده‌اند.
2. **مدرن و زنده:** استفاده از Glassmorphism، Mesh Gradients، انیمیشن‌های تعاملی و Neon Highlights.
3. **اعتمادبخش:** رنگ‌ها، متون و میکروکپی‌ها برای کاهش اضطراب مالی و فنی طراحی شده‌اند.
4. **قابل مقیاس:** Design Tokens و ساختار ماژولار به راحتی قابل گسترش برای صفحات جدید هستند.
5. **ریسپانسیو و دسترسپذیر:** Breakpoints، تایپوگرافی Fluid و پشتیبانی از RTL.

### گام بعدی:
- **پروتوتایپ در Figma:** تبدیل این سند به فایل Figma با کامپوننت‌های قابل استفاده مجدد
- **پیاده‌سازی Frontend:** استفاده از React/Vue/Next.js + Tailwind CSS یا CSS-in-JS
- **تست کاربری:** A/B Testing روی Hero Headlines، CTA Buttons و Pricing Cards
- **بهینه‌سازی نهایی:** Lighthouse Score، Core Web Vitals و Accessibility Audit

---

**تاریخ تدوین:** ۱۴۰۳/۰۸/۰۲  
**نسخه:** 1.0.0  
**وضعیت:** آماده برای پیاده‌سازی ✅
