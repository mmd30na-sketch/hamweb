# -*- coding: utf-8 -*-
import html
def L(fa, en, tag='span', cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c} data-lang="fa">{fa}</{tag}><{tag}{c} data-lang="en">{en}</{tag}>'
CHECK = '<svg class="ck" width="22" height="22" viewBox="0 0 22 22" aria-hidden="true"><circle cx="11" cy="11" r="11" fill="currentColor" opacity=".16"/><path d="M6.5 11.5l3 3 6-6.5" stroke="currentColor" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW = '<svg class="arr" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 12H5m0 0l6-6m-6 6l6 6" stroke="currentColor" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SPARK = '<svg class="spark" viewBox="0 0 40 40" aria-hidden="true"><path d="M20 0C21.5 13 27 18.5 40 20 27 21.5 21.5 27 20 40 18.5 27 13 21.5 0 20 13 18.5 18.5 13 20 0Z" fill="currentColor"/></svg>'
MAIL = 'mailto:sina@mmd30na.cloud?subject=Ham%20Pilot%20Access'
def checks(items):
    return '<ul class="checks">' + ''.join(f'<li>{CHECK}<span>{L(fa,en)}</span></li>' for fa, en in items) + '</ul>'

modules = [
 dict(key='taraz', en='Hamtaraz', fa='همتراز', n=('۱','1'),
  tag=('سیستم حسابداری هماهنگ با کسب‌وکار شما','Accounting system in sync with your business'),
  desc=('سیستم حسابداری ابری منطبق با استانداردهای حسابداری بومی خاورمیانه، ساختارهای مالیاتی محلی و رابط کاربری کاملاً راست‌به‌چپ (فارسی و عربی).','Cloud accounting engineered for local Middle-East accounting rules, statutory tax structures, and native Persian/Arabic RTL interfaces.'),
  checks=[('دفتر کل دوطرفه منطبق با سرفصل‌های استاندارد حسابداری منطقه','Double-entry general ledger tailored to regional chart-of-accounts standards'),('صدور فاکتور، تقویم مالی و ثبت اسناد با پشتیبانی بومی راست‌به‌چپ','Native Persian & Arabic RTL invoicing, fiscal calendars, and voucher workflows'),('ثبت خودکار اسناد مالی مستقیماً از تراکنش‌های فروش همدست','Automated journal entries posted directly from Hamdast sales transactions')]),
 dict(key='raz', en='Hamraz', fa='همراز', n=('۲','2'),
  tag=('گزارش محرمانهٔ عملکرد، فقط برای مدیر','Confidential performance report, for the owner only'),
  desc=('گزارش‌های محرمانهٔ مالک و هوش تجاری (BI) برای ارائهٔ تحلیل جریان نقدینگی، حاشیه سود و شاخص‌های کلیدی عملکرد منحصراً برای مدیر کسب‌وکار.','Private owner reports and business intelligence (BI) delivering confidential cash-flow, margin, and operational briefings exclusively to the business owner.'),
  checks=[('خلاصه‌گزارش‌های مدیریتی اختصاصی و مشاهدهٔ سود و زیان درلحظه','Owner-only encrypted executive digests & real-time P&L visibility'),('پرسش‌وپاسخ مالی به زبان طبیعی و هشدار ناهنجاری‌های مالی با هوش مصنوعی','Natural-language financial Q&A and anomaly alerts powered by AI'),('تحلیل ماندگاری مشتریان، سررسید مطالبات و پایش سرمایه در گردش','Cohort retention, receivables aging, and net working capital tracking')]),
 dict(key='dast', en='Hamdast', fa='همدست', n=('۳','3'),
  tag=('منشی هوشمندی که مشتری را تا پرداخت همراهی می‌کند','AI secretary that walks the customer all the way to payment'),
  desc=('عامل فروش هوشمند که مشتری را از اولین پیام و مشاوره تا ثبت سفارش و پرداخت نهایی همراهی کرده و تراکنش تاییدشده را خودکار در همتراز ثبت می‌کند.','AI sales agent that manages the entire customer journey from initial chat inquiry to order confirmation and payment—automatically posting verified entries into Hamtaraz.'),
  checks=[('پاسخ‌گویی ۲۴ ساعته، استعلام قیمت و ثبت سفارش محاوره‌ای','24/7 conversational product discovery, quoting, and order capture'),('هدایت مشتری تا تسویه، تایید پرداخت و صدور خودکار رسید','Guided checkout, payment verification, and automated receipt issuance'),('حذف دوباره‌کاری: ثبت آنی هر فروش موفق در دفتر کل همتراز','Zero manual bookkeeping: every completed sale syncs straight into Hamtaraz')]),
]
def illo(key):
    if key == 'taraz':
        rows = [('فاکتور فروش · همدست','Sales invoice · Hamdast'),('دریافت بانکی','Bank receipt'),('ثبت سند دوطرفه','Double-entry voucher')]
        return '<div class="mini card"><b class="mini-title">'+L('دفتر کل · اسناد امروز','General ledger · today')+'</b>' + ''.join(f'<div class="mini-row"><span>{L(a,b)}</span><em class="badge">{L("ثبت شد","Posted")}</em></div>' for a,b in rows) + '</div>'
    if key == 'raz':
        kp = [('جریان نقدینگی','Cash flow'),('حاشیه سود','Margin'),('سرمایه در گردش','Working capital')]
        return '<div class="mini card dark"><b class="mini-title">'+L('داشبورد محرمانهٔ مدیر','Owner-only dashboard')+'</b><svg class="area" viewBox="0 0 340 110" preserveAspectRatio="none" aria-hidden="true"><path class="area-fill" d="M0 90 C40 80 60 60 100 66 S170 30 210 44 S280 10 340 14 L340 110 L0 110Z"/><path class="area-line" d="M0 90 C40 80 60 60 100 66 S170 30 210 44 S280 10 340 14"/><circle cx="330" cy="15" r="7" fill="#FFD166"/></svg><div class="kpis">' + ''.join(f'<span>{L(a,b)}</span>' for a,b in kp) + '</div></div>'
    st = [('اولین پیام و مشاوره','First message & advice'),('استعلام قیمت','Quote request'),('ثبت سفارش','Order capture'),('پرداخت و صدور رسید','Payment & receipt')]
    nums = ['۱','۲','۳','۴']
    return '<div class="mini card"><b class="mini-title">'+L('مسیر مشتری در همدست','Customer journey in Hamdast')+'</b>' + ''.join(f'<div class="step{" last" if i==3 else ""}"><i>{L(nums[i],str(i+1))}</i><span>{L(a,b)}</span></div>' for i,(a,b) in enumerate(st)) + '</div>'

mod_html = ''
for i, m in enumerate(modules):
    mod_html += f'''
    <article class="module m-{m['key']}{' flip' if i%2 else ''} reveal">
      <div class="illo"><span class="blob a"></span><span class="blob b"></span><span class="spk">{SPARK}</span>{illo(m['key'])}</div>
      <div class="copy">
        <span class="chip">{m['en']} · {L('ماژول '+m['n'][0],'Module '+m['n'][1])}</span>
        <h3 class="mod-name">{L(m['fa'],m['en'])}</h3>
        <p class="mod-tag">{L(*m['tag'])}</p>
        <p class="mod-desc">{L(*m['desc'])}</p>
        {checks(m['checks'])}
      </div>
    </article>'''

ICONS = {
 'chat':'<svg viewBox="0 0 24 24" width="34" height="34"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z" stroke="#081D53" stroke-width="2" fill="none" stroke-linejoin="round"/><circle cx="9" cy="12" r="1.2" fill="#081D53"/><circle cx="13" cy="12" r="1.2" fill="#081D53"/><circle cx="17" cy="12" r="1.2" fill="#081D53"/></svg>',
 'ledger':'<svg viewBox="0 0 24 24" width="34" height="34"><rect x="4" y="3" width="16" height="18" rx="3" stroke="#081D53" stroke-width="2" fill="none"/><path d="M8 8h8M8 12h8M8 16h5" stroke="#081D53" stroke-width="2" stroke-linecap="round"/></svg>',
 'chart':'<svg viewBox="0 0 24 24" width="34" height="34"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2" stroke="#081D53" stroke-width="2.2" stroke-linecap="round"/></svg>'}
steps = [
 ('۱','1','همدست','Hamdast','همدست گفت‌وگو را به پرداخت قطعی تبدیل می‌کند','Hamdast converts chat to verified payment','chat','sun',('خروجی: پرداخت تاییدشده','Output: verified payment')),
 ('۲','2','همتراز','Hamtaraz','همتراز فاکتور و سند حسابداری را ثبت می‌کند','Hamtaraz posts invoice & ledger entry','ledger','mint',('خروجی: فاکتور + سند دفتر کل','Output: invoice + ledger entry')),
 ('۳','3','همراز','Hamraz','همراز داشبورد محرمانهٔ مدیر را به‌روز می‌کند','Hamraz updates private owner BI','chart','lilac',('خروجی: داشبورد درلحظه','Output: real-time dashboard')),
]
pipe = ''
for i, s in enumerate(steps):
    if i:
        pipe += '<div class="conn" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><svg viewBox="0 0 24 24" width="20" height="20"><path d="M15 5l-7 7 7 7" stroke="#FFD166" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
    pipe += f'''<div class="pstep reveal" data-step="{i}"><div class="ptop"><span class="pnum">{L(s[0],s[1])}</span><span class="picon {s[7]}">{ICONS[s[6]]}</span></div><h4>{L(s[2],s[3])}</h4><p>{L(s[4],s[5])}</p><em class="opill">{L(*s[8])}</em></div>'''

tiers = [
 ('۳','3','lilac',('دقت بالا · فقط در نقاط کلیدی','High accuracy · only where it matters'),('لایهٔ سوم — استدلال پیچیده و تحلیل مالی پیشرفته با Google Gemini','Tier 3 — Complex Reasoning & Financial Synthesis with Google Gemini'),('مذاکرات چندمرحله‌ای فروش، تطبیق اسناد پیچیدهٔ مالی و تولید گزارش‌های تحلیلی همراز به مدل‌های Gemini ارجاع می‌شوند تا بالاترین دقت در نقاط کلیدی کسب‌وکار تضمین شود.','Multi-step customer negotiations, ambiguous invoice reconciliation, and Hamraz executive financial narratives are escalated to Gemini—delivering high-accuracy reasoning only where it creates maximum business value.')),
 ('۲','2','sky',('قواعد قطعی · کنترل دسترسی','Deterministic rules · access control'),('لایهٔ دوم — عامل‌های تخصصی دامنه (فروش، حسابداری و گزارش‌دهی)','Tier 2 — Specialized Domain Agents (Sales, Ledger, BI)'),('عامل‌های مجزا برای همدست، همتراز و همراز پیش از ثبت هرگونه داده در پایگاه داده، قواعد قطعی حسابداری و سطوح دسترسی را اعتبارسنجی می‌کنند.','Dedicated agents for Hamdast, Hamtaraz, and Hamraz enforce deterministic accounting rules, RTL formatting, and role-based access boundaries before any database write occurs.')),
 ('۱','1','mint',('پرتکرار · کم‌هزینه','High-frequency · low cost'),('لایهٔ اول — تشخیص نیت مشتری، دسته‌بندی و استخراج ساختاریافته','Tier 1 — Lightweight Intent, Routing & Extraction'),('پردازش‌های پرتکرار و روزمره (تشخیص اولیهٔ درخواست، سوالات متداول و استخراج فیلدها) توسط مدل‌های متن‌باز سبک، آزمایشی و لایهٔ رایگان انجام می‌شود تا هزینهٔ پایه به حداقل برسد.','High-frequency routine tasks (greeting, FAQ matching, entity extraction, and schema validation) are handled by free-tier, trial, and compact open-source models—reducing baseline inference cost near zero.')),
]
tier_html = ''.join(f'<div class="tier {c} reveal" style="--w:{w}%"><span class="tnum">{L(a,b)}</span><div><em class="ttag">{L(*tag)}</em><h4>{L(*t)}</h4><p>{L(*d)}</p></div></div>' for (a,b,c,tag,t,d),w in zip(tiers,[100,92,84]))
road = [('مرحلهٔ فعلی','Current Stage','teal','ترکیب هوشمند مدل‌های متن‌باز، لایهٔ رایگان و آزمایشی در کنار Google Gemini برای استدلال‌های پیچیده.','Dynamic orchestration combining free-tier, trial, and open-source endpoints with Google Gemini for hard reasoning tasks.'),
        ('گام بعدی زیرساخت','Next Milestone','sun','استقرار و میزبانی مستقل مدل‌های متن‌باز بهینه‌شده بر روی زیرساخت ابری کم‌هزینه برای پردازش‌های پرتکرار فارسی و عربی.','Deploying quantized self-hosted open models on low-cost cloud infrastructure for high-volume RTL classification and bookkeeping automation.'),
        ('مقیاس‌پذیری ابری','Cloud Scale','coral','گسترش معماری ترکیبی چندعامله و یکپارچگی با Gemini بر بستر Google Cloud.','Scaling hybrid multi-agent workloads and Gemini API integration on Google Cloud.')]
road_html = ''.join(f'<li><i class="mk {c}"></i><div><b>{L(a,b)}</b><p>{L(d,e)}</p></div></li>' for a,b,c,d,e in road)

plans = [
 ('starter','پایه (Starter)','Starter','mint','مناسب کسب‌وکارهای خرد برای اتوماسیون فروش محاوره‌ای و ثبت اسناد مالی پایه.','For solo operators and micro-businesses automating chat sales and core bookkeeping.',[('عامل فروش هوشمند همدست روی یک کانال ارتباطی','Hamdast AI sales agent for 1 messaging channel'),('هستهٔ حسابداری ابری همتراز و صدور فاکتور راست‌به‌چپ','Hamtaraz core cloud ledger & RTL invoicing'),('گزارش هفتگی عملکرد مدیریت در همراز','Weekly Hamraz owner summary report')],'Ham%20Starter%20Pilot'),
 ('growth','رشد (Growth)','Growth','sun','مناسب کسب‌وکارهای در حال رشد با نیاز به فروش چندکاناله، حسابداری کامل و داشبورد مدیریتی درلحظه.','For active SMBs requiring multi-channel AI sales, full statutory accounting, and real-time BI.',[('همدست چندکاناله با تطبیق خودکار پرداخت‌ها','Hamdast multi-channel sales & payment reconciliation'),('حسابداری کامل همتراز منطبق با قوانین مالی و مالیاتی منطقه','Full Hamtaraz Middle-East accounting & tax rules'),('داشبورد درلحظهٔ همراز و پرسش‌وپاسخ تحلیلی ویژهٔ مدیر','Real-time Hamraz private owner BI & natural-language Q&A')],'Ham%20Growth%20Pilot'),
 ('business','تجاری (Business)','Business','lilac','مناسب مجموعه‌های چندشعبه‌ای با نیاز به گردش‌کار سفارشی، استقرار اختصاصی و اتصال API.','For multi-branch operations needing custom workflows, dedicated onboarding, and API integrations.',[('قواعد اختصاصی CRM و موتور گردش‌کار در همدست','Custom Hamdast CRM & workflow engine rules'),('مدیریت چند مرکز هزینه و سطوح دسترسی پیشرفته در همتراز','Multi-entity Hamtaraz ledgers & role permissions'),('گزارش‌های تلفیقی همراز و پشتیبانی اختصاصی استقرار','Executive multi-branch Hamraz forecasting & priority support')],'Ham%20Business%20Pilot'),
]
plan_html = ''
for k, fa, en, acc, dfa, den, feats, subj in plans:
    hi = ' hi' if k == 'growth' else ''
    btn = 'btn-primary' if hi else 'btn-secondary'
    plan_html += f'''<div class="plan{hi} reveal"><div class="ptop"><h3>{L(fa,en)}</h3><span class="pblob {acc}"></span></div><p class="pnote">{L('پایلوت اختصاصی — تماس بگیرید','Dedicated pilot — contact us')}</p><p class="pdesc">{L(dfa,den)}</p><hr>{checks(feats)}<a class="btn {btn}" href="mailto:sina@mmd30na.cloud?subject={subj}">{ARROW}{L('تماس بگیرید','Contact us')}</a></div>'''

marq_items = [('حسابداری ابری','Cloud accounting'),('گزارش‌های مدیریتی','Owner reporting'),('فروش محاوره‌ای','Conversational sales'),('پشتیبانی بومی راست‌به‌چپ','Native RTL support'),('فارسی و عربی','Persian & Arabic'),('Google Gemini','Google Gemini'),('مسیریابی بهینهٔ هزینه','Cost-aware routing'),('پاسخ‌گویی ۲۴ ساعته','24/7 responses')]
cols = ['sun','coral','lilac','mint','sky']
mq_one = ''.join(f'<span class="mq-item">{L(a,b)}</span><span class="mq-spark {cols[i%5]}">{SPARK}</span>' for i,(a,b) in enumerate(marq_items))

stats = [('۳','3','ماژول یکپارچه','integrated modules'),('۱','1','هستهٔ دادهٔ مشترک','shared data layer'),('۳','3','لایهٔ مسیریابی هوش مصنوعی','AI routing tiers'),('۲۴','24','ساعته پاسخ‌گویی همدست','hour Hamdast responses')]
stat_html = ''.join(f'<div class="stat reveal"><b class="num" data-fa="{a}" data-en="{b}">{L(a,b)}</b><span>{L(c,d)}</span></div>' for a,b,c,d in stats)

tpl = open('/workspace/hamsite/template.html', encoding='utf-8').read()
out = (tpl.replace('{{MODULES}}', mod_html).replace('{{PIPE}}', pipe).replace('{{TIERS}}', tier_html).replace('{{ROAD}}', road_html)
       .replace('{{PLANS}}', plan_html).replace('{{MARQ}}', mq_one + mq_one).replace('{{STATS}}', stat_html)
       .replace('{{ARROW}}', ARROW).replace('{{SPARK}}', SPARK).replace('{{CHECK}}', CHECK).replace('{{MAIL}}', MAIL))
import re
out = re.sub(r'\{\{L:(.*?)\|(.*?)\}\}', lambda m: L(m.group(1), m.group(2)), out, flags=re.S)
assert '{{' not in out, out[out.find('{{')-50:out.find('{{')+80]
open('/workspace/hamsite/dist/index.html', 'w', encoding='utf-8').write(out)
print(len(out))
