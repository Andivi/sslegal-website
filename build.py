#!/usr/bin/env python3
"""Static site generator for the S&S Legal website.

All content lives in this file. Edit it, then run:

    python3 build.py

The pages are written next to this file (index.html, expertise/, lawyers/, ...),
ready to publish on any static host such as GitHub Pages or Netlify.
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = 'https://sslegal.org/'

# --------------------------------------------------------------------------
# Firm details
# --------------------------------------------------------------------------
FIRM = {
    'name': 'S&amp;S Legal',
    'tagline': 'Barristers &amp; Solicitors · Accra',
    'address_lines': ['F233/2 Wentum Street,', 'off Lokko Street, Osu, Accra'],
    'address_one': 'F233/2 Wentum Street, off Lokko Street, Osu, Accra, Ghana',
    'phones': ['+233 24 447 6615', '+233 54 793 1937'],
    'phone_tel': '+233244476615',
    'whatsapp': '233244476615',
    'email': 'info@sslegal.org',
    'hours': 'Monday – Friday, 8:00am – 5:00pm',
    'facebook': 'https://www.facebook.com/sslegal.org',
    'maps': 'https://www.google.com/maps/search/?api=1&amp;query=Wentum+Street+Osu+Accra',
    'year': 2026,
}

# --------------------------------------------------------------------------
# People (from the lawyer profiles on the current website)
# --------------------------------------------------------------------------
PEOPLE = {
    'richmond-numbo-saaka': dict(
        name='Richmond Numbo Saaka', short='Richmond Numbo Saaka, Esq.', first='Richmond', em='Numbo Saaka, Esq.', call='Richmond',
        img='front-richmond-full.jpg', w=491, h=683, studio=True,
        role='Founder · Transactional &amp; Litigation Lawyer', card_role='Founder',
        card_text='Transactional work, litigation and alternative dispute resolution.',
        card_cred='LL.M., Cornell University · QCL, Ghana School of Law',
        lead='Richmond founded S&amp;S Legal in 2017. He brings extensive experience from private practice and academia to the firm’s transactional and dispute resolution work.',
        contact=[('Telephone', '+233 24 447 6615'), ('Email', 'numbo.saaka@sslegal.org')],
        prose=['Richmond Numbo Saaka is a transactional and litigation lawyer with extensive legal experience in both private practice and academia.',
               'He holds a Bachelor of Laws from Kwame Nkrumah University of Science and Technology (KNUST), a Qualifying Certificate in Law from the Ghana School of Law, and a Master of Laws from Cornell University School of Law in Ithaca, New York.',
               'Alongside his practice, he has a passion for legal research, education and scholarship. He has served as a teaching and research assistant at the Faculty of Law, KNUST, and as a lecturer at the Faculty of Law, Mountcrest University College, Accra.',
               'His litigation and alternative dispute resolution skills were developed through practice with George Sarpong Legal Services in Kumasi, and with Dery &amp; Co. and Sory @ Law in Accra.'],
        exp_title='Practice and teaching',
        exp=[('S&amp;S Legal, Accra', 'Founder, 2017'), ('Sory @ Law, Accra', 'Private practice'), ('Dery &amp; Co., Accra', 'Private practice'),
             ('George Sarpong Legal Services, Kumasi', 'Private practice'), ('Faculty of Law, Mountcrest University College', 'Lecturer'),
             ('Faculty of Law, KNUST', 'Teaching and research assistant')],
        areas=['litigation', 'corporate'],
        edu=[('Master of Laws (LL.M.)', 'Cornell University School of Law, New York'), ('Qualifying Certificate in Law', 'Ghana School of Law'),
             ('Bachelor of Laws (LL.B.)', 'Kwame Nkrumah University of Science and Technology')],
        member=[('Ghana Bar Association', 'Member'), ('Cornell Institute for African Development', 'Fellow')]),
    'victor-reginald-johnson': dict(
        name='Victor Reginald Johnson', short='Victor R. Johnson, Esq.', first='Victor R.', em='Johnson, Esq.', call='Victor',
        img='reginald-johnson.jpg', w=500, h=606, studio=False,
        role='Senior Associate · Litigation &amp; Corporate Lawyer', card_role='Senior Associate',
        card_text='Complex litigation, corporate and commercial law, debt recovery, probate and property transactions.',
        card_cred='LL.M. Corporate &amp; Commercial, University of Ghana · Called to the Bar 2020',
        lead='Victor specialises in complex litigation, corporate and commercial law, and debt recovery, with a sharp, practical approach to resolving disputes and completing transactions.',
        contact=[('Called to the Bar', 'December 2020'), ('Email', 'info@sslegal.org')],
        prose=['Victor Reginald Johnson is a Senior Associate at S&amp;S Legal, specialising in complex litigation, corporate and commercial law, and debt recovery.',
               'He also advises on private client matters, including probate and administration, and on immovable property law, including land registration and legal due diligence. He was called to the Bar in December 2020.',
               'Victor holds a B.Sc. in Corporate and Business Development Studies from Pentecost University, an LL.B. from Wisconsin International University, a Qualifying Certificate in Law from the Ghana School of Law, and an LL.M. in Corporate and Commercial Law from the University of Ghana.'],
        exp_title=None, exp=[],
        areas=['litigation', 'debt-recovery', 'corporate', 'due-diligence', 'infrastructure', 'wills'],
        edu=[('LL.M., Corporate and Commercial Law', 'University of Ghana'), ('Qualifying Certificate in Law', 'Ghana School of Law'),
             ('Bachelor of Laws (LL.B.)', 'Wisconsin International University'), ('B.Sc., Corporate and Business Development Studies', 'Pentecost University')],
        member=[('Ghana Bar Association', 'Member')]),
    'nana-akwasi-asafo-adjei': dict(
        name='Nana Akwasi Asafo-Adjei', short='Nana Akwasi Asafo-Adjei, Esq.', first='Nana Akwasi', em='Asafo-Adjei, Esq.', call='Nana Akwasi',
        img='nana-akwasi.jpg', w=500, h=606, studio=False,
        role='Associate', card_role='Associate',
        card_text='Constitutional law, immovable property, commercial and corporate law, and arbitration.',
        card_cred='LL.B., University of Ghana · QCL, Ghana School of Law',
        lead='Nana Akwasi’s practice interests include constitutional law, immovable property, commercial and corporate law, and arbitration.',
        contact=[('Email', 'info@sslegal.org')],
        prose=['Nana Akwasi Asafo-Adjei is a legal practitioner and an Associate at S&amp;S Legal in Osu, Accra.',
               'His interests span constitutional law, immovable property, commercial law, corporate law and arbitration.',
               'He holds a Bachelor of Laws from the University of Ghana School of Law and a Qualifying Certificate in Law from the Ghana School of Law.'],
        exp_title=None, exp=[],
        areas=['litigation', 'corporate', 'infrastructure'],
        extra_chips=['Constitutional law'],
        edu=[('Qualifying Certificate in Law', 'Ghana School of Law'), ('Bachelor of Laws (LL.B.)', 'University of Ghana')],
        member=[('Ghana Bar Association', 'Member')]),
    'abdul-razak-sania': dict(
        name='Dr Abdul Razak Sania', short='Dr Abdul Razak Sania, Esq.', first='Dr Abdul Razak', em='Sania, Esq.', call='Dr Sania',
        img='abdulrazak-sania.jpg', w=500, h=606, studio=False,
        role='Lawyer &amp; Development Practitioner', card_role='Lawyer &amp; Development Practitioner',
        card_text='Law and development, governance reform, enterprise growth and agricultural value chains.',
        card_cred='PhD Development Studies, University of Cape Coast',
        lead='Dr Sania works where law meets governance and socio-economic development, drawing on senior experience in commodities, agribusiness and enterprise.',
        contact=[('Email', 'info@sslegal.org')],
        prose=['Dr Abdul Razak Sania is a multidisciplinary professional whose expertise spans law, project management, commodity value chain development and sustainable livelihoods.',
               'His research explores how legal systems shape socio-economic development, governance and access to justice in emerging economies, with particular attention to informal economic systems, institutional reform and enterprise development.',
               'He has served as Commercial Manager at RMG Commodities/Wienco Ghana and as Managing Director of Agritrade Limited. He is Managing Consultant at San Alliance Limited and a steering committee member of the Ghana Skills Development Fund, and is undertaking professional legal training at S&amp;S Legal.'],
        exp_title='Leadership roles',
        exp=[('San Alliance Limited', 'Managing Consultant'), ('Ghana Skills Development Fund', 'Steering committee member'),
             ('Agritrade Limited', 'Managing Director'), ('RMG Commodities / Wienco Ghana', 'Commercial Manager')],
        areas=[],
        extra_chips=['Law and development', 'Governance and policy', 'Agribusiness and commodities', 'Enterprise development'],
        edu=[('PhD, Development Studies', 'University of Cape Coast'), ('MPhil, Development Studies', 'Kwame Nkrumah University of Science and Technology'),
             ('MBA, Project Management', 'Wisconsin International University College'), ('MA, Ministry (Biblical Studies)', 'Trinity Theological Seminary'),
             ('Bachelor of Laws (LL.B.)', 'Wisconsin International University College'), ('Qualifying Certificate in Law', 'Ghana School of Law'),
             ('Certificate in Energy and Commodity Finance', 'National Banking College'), ('B.Sc., Agriculture', 'Kwame Nkrumah University of Science and Technology')],
        member=[]),
    'bassing-ali-kamaldeen': dict(
        name='Bassing Ali Kamaldeen', short='Bassing Ali Kamaldeen, Esq.', first='Bassing Ali', em='Kamaldeen, Esq.', call='Bassing',
        img='bassing-kamaldeen.jpg', w=500, h=606, studio=False,
        role='Pupil', card_role='Pupil',
        card_text='Litigation, dispute resolution, legal research and public policy, with a focus on energy law.',
        card_cred='LL.M. Energy Law (in progress), University of Ghana',
        lead='Bassing is undertaking his pupillage at S&amp;S Legal while pursuing an LL.M. in Energy Law, with a focus on petroleum, gas and electricity markets.',
        contact=[('Email', 'info@sslegal.org')],
        prose=['Bassing Ali Kamaldeen is undertaking his pupillage at S&amp;S Legal and pursuing a Master of Laws in Energy Law at the University of Ghana, Legon.',
               'His research focuses on the upstream and downstream energy sectors, including petroleum, oil and gas, and electricity markets. He brings an interdisciplinary foundation in law, economic policy management and the social sciences.',
               'Before joining S&amp;S Legal he gained experience with the Legal Aid Commission and the Parliament of Ghana, working on public law, advocacy and legislative processes.'],
        exp_title='Previous experience',
        exp=[('Parliament of Ghana', 'Public law and legislative processes'), ('Legal Aid Commission', 'Advocacy and access to justice')],
        areas=['litigation'],
        extra_chips=['Energy law', 'Public policy'],
        edu=[('LL.M., Energy Law (in progress)', 'University of Ghana'), ('Qualifying Certificate in Law', 'Ghana School of Law, Makola'),
             ('MA, Economic Policy Management', 'University of Ghana'), ('Bachelor of Laws (LL.B.)', 'Wisconsin International University College'),
             ('BA, Sociology', 'Kwame Nkrumah University of Science and Technology'), ('Diploma, Social Work', 'School of Social Work, Osu')],
        member=[]),
}
SUPPORT = ('Rachel Anum', 'Office Manager')

# --------------------------------------------------------------------------
# Practice groups and areas (from the Practice Areas page on the current website)
# --------------------------------------------------------------------------
GROUPS = {
    'business': dict(title='Business', h1='Business law, <em>from formation to growth</em>.',
        intro='We advise domestic and international clients on corporate, investment, finance, technology, property and infrastructure matters.',
        card='Corporate, investment, finance, regulatory, intellectual property and infrastructure work for companies and investors.'),
    'disputes': dict(title='Disputes', h1='Disputes, resolved <em>in court or outside it</em>.',
        intro='Our lawyers have the litigation skills needed to settle disputes in court on our clients’ behalf. Where it is better to resolve a dispute outside the courtroom, we use negotiation, mediation and arbitration.',
        card='Litigation, arbitration and mediation, debt recovery and criminal defence.'),
    'private-clients': dict(title='Private clients', h1='Private clients, <em>handled with care</em>.',
        intro='We help individuals and families plan for the future and resolve personal legal matters, from wills and estates to family and immigration.',
        card='Wills, trusts and estates, and matrimonial, family and immigration matters.'),
}
AREAS = [
    dict(slug='corporate', group='business', title='Corporate, Investment &amp; Securities',
         summary='Commercial and corporate advice for domestic and international clients, and end-to-end investment and securities work.',
         body=['Commercial and corporate advice is at the core of the services we provide to domestic and international clients.',
               'Our end-to-end investment and securities services make it easier for clients to navigate today’s international financial markets.']),
    dict(slug='mergers', group='business', title='Mergers, Acquisitions &amp; Restructuring',
         summary='Advice on expanding or downsizing, from new structures to labour and tax implications.',
         body=['Whether a business is expanding or downsizing, we advise on every stage, from managing the new structure and organogram of the enterprise to the labour and tax implications.',
               'We tailor a solution to each client’s business goals.']),
    dict(slug='due-diligence', group='business', title='Due Diligence, Compliance &amp; Regulatory',
         summary='Legal assessment of business methods and operational risk, with clear advice on closing gaps.',
         body=['We provide a legal assessment of companies’ business methods and operational risks.',
               'We highlight gaps or deficiencies, and advise on the tools and infrastructure needed to meet institutional standards.']),
    dict(slug='banking', group='business', title='Banking, Finance &amp; Capital Markets',
         summary='Buyout and project financing, banking regulation, and Ghanaian and cross-border transactions.',
         body=['We offer complete legal support on buyout financing, project financing and banking regulation.',
               'We also give specialist advice on Ghanaian and cross-border financial and investment transactions.']),
    dict(slug='ip-technology', group='business', title='Intellectual Property, Technology &amp; Telecoms',
         summary='Technology transactions, telecoms infrastructure, and patents, trade marks, copyright and designs.',
         body=['We give strategic advice on technology transactions and on telecommunications infrastructure projects.',
               'We work closely with clients to identify, develop, commercialise and protect intellectual property, and advise on patents, trade marks, copyright, designs and confidential information.']),
    dict(slug='infrastructure', group='business', title='Environmental, Real Estate &amp; Infrastructure',
         summary='Project development, procurement, site acquisition, public land leases and environmental assessment.',
         body=['We advise on all aspects of infrastructure project development, including public bidding and procurement, agreement negotiation, site acquisition and control, and public land leases.',
               'Our work also covers environmental impact assessment, construction and permanent financing, construction contracting, and appeals against project approvals.']),
    dict(slug='litigation', group='disputes', title='Litigation &amp; Alternative Dispute Resolution',
         summary='Representation in court and, where better for the client, negotiation, mediation and arbitration.',
         body=['If so required, we lead a judicial contest to determine and enforce your legal rights, including proceedings in a court of law.',
               'Where it is desirable or necessary to settle a dispute outside the courtroom, we use alternative dispute resolution, including negotiation, mediation and arbitration.']),
    dict(slug='debt-recovery', group='disputes', title='Debt Recovery',
         summary='Commercial, domestic and insolvency recoveries, and enforcement of court orders.',
         body=['When it comes to your money, no amount is too big or too small for us to recover.',
               'We handle commercial recoveries, domestic recoveries and insolvency recoveries, and the enforcement of court orders.']),
    dict(slug='criminal-defence', group='disputes', title='Criminal Defence',
         summary='A considered defence strategy in every case, built to protect clients and their families.',
         body=['We work to reduce, and where possible remove, the penalties our clients face in criminal court, and we build a considered defence strategy in every case.',
               'Our lawyers bring their experience, skill and time to protect you and your family to the very best of their ability.']),
    dict(slug='wills', group='private-clients', title='Wills, Trusts &amp; Estates',
         summary='Wills, trusts, and probate and administration, so your wishes are secure and your family provided for.',
         body=['We help clients write wills that secure their legacy and provide for their loved ones, and we take care of every formality.',
               'We also advise on trusts and the management of assets, and on the probate and administration of estates, anticipating and guarding against problems that may arise later.']),
    dict(slug='family', group='private-clients', title='Matrimonial, Family &amp; Immigration',
         summary='Culturally sensitive representation in family matters, and a clear voice in immigration cases.',
         body=['Our lawyers represent clients in matrimonial and family matters with care and cultural sensitivity, addressing the many connected legal needs these matters involve.',
               'In immigration matters, we give a clear voice to clients facing a complex system that does not guarantee representation.']),
]
AREA = {a['slug']: a for a in AREAS}
for a in AREAS:
    a['lawyers'] = [s for s, p in PEOPLE.items() if a['slug'] in p['areas']]

# --------------------------------------------------------------------------
# Building blocks
# --------------------------------------------------------------------------
ARROW = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4"/></svg>'
FONTS = 'https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&amp;family=Hanken+Grotesk:wght@400;500;600&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap'

def area_url(p, slug):
    return f'{p}expertise/{AREA[slug]["group"]}/index.html#{slug}'

def head(p, path, title, desc, extra=''):
    canonical = SITE_URL + path
    return f'''<!doctype html>
<html lang="en-GH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="S&amp;S Legal">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<link rel="icon" type="image/png" href="{p}assets/img/sslegal-logo.png">
<script>try{{var t=localStorage.getItem("ss-theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{p}assets/css/styles.css">
{extra}</head>
<body>
'''

NAV = [('expertise', 'Expertise', 'expertise/index.html'), ('lawyers', 'Our lawyers', 'lawyers/index.html'),
       ('about', 'About', 'about/index.html'), ('contact', 'Contact', 'contact/index.html')]

def header(p, active):
    cur = ' aria-current="page"'
    links = ''.join(f'<a class="link" href="{p}{u}"{cur if k == active else ""}>{t}</a>' for k, t, u in NAV)
    mlinks = ''.join(f'<a href="{p}{u}">{t}</a>' for k, t, u in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <div class="wrap">
    <a class="brand" href="{p}index.html" aria-label="S&amp;S Legal, home">
      <span class="logo" aria-hidden="true"></span>
      <span><b>S&amp;S Legal</b><small>{FIRM["tagline"]}</small></span>
    </a>
    <nav class="nav" aria-label="Main">
      {links}
      <span class="tools">
        <button class="icon-btn theme-btn" id="theme-btn" type="button" aria-label="Switch between light and dark theme"><svg class="moon" width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M16.5 12.5A7 7 0 0 1 7.5 3.5a7 7 0 1 0 9 9z"/></svg><svg class="sun" width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="10" cy="10" r="3.5"/><path d="M10 1.5v2M10 16.5v2M1.5 10h2M16.5 10h2M4 4l1.4 1.4M14.6 14.6L16 16M4 16l1.4-1.4M14.6 5.4L16 4"/></svg></button>
        <button class="icon-btn menu-btn" id="menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M2 6h16M2 14h16"/></svg></button>
      </span>
      <a class="btn btn-main" href="{p}contact/index.html">Request a consultation</a>
    </nav>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile" hidden>
    <div class="wrap">{mlinks}</div>
  </nav>
</header>
'''

def footer(p):
    groups = ''.join(f'<a href="{p}expertise/{k}/index.html">{g["title"]}</a>' for k, g in GROUPS.items())
    phones = ''.join(f'<span>{x}</span>' for x in FIRM['phones'])
    return f'''<footer>
  <div class="wrap">
    <div class="fgrid">
      <div class="fcol fbrand">
        <a class="brand" href="{p}index.html" aria-label="S&amp;S Legal, home"><span class="logo" aria-hidden="true"></span><span><b>S&amp;S Legal</b><small>{FIRM["tagline"]}</small></span></a>
        <p>{FIRM["address_one"]}</p>
        <p>{FIRM["hours"]}</p>
      </div>
      <nav class="fcol" aria-label="Expertise"><h2>Expertise</h2>{groups}</nav>
      <nav class="fcol" aria-label="The firm"><h2>The firm</h2><a href="{p}lawyers/index.html">Our lawyers</a><a href="{p}about/index.html">About S&amp;S Legal</a><a href="{p}contact/index.html">Contact</a></nav>
      <div class="fcol"><h2>Contact</h2>{phones}<span>{FIRM["email"]}</span><a href="{FIRM["facebook"]}" target="_blank" rel="noopener">Facebook ↗</a></div>
    </div>
    <div class="flegal">
      <p class="disc">The information on this website is general and is not legal advice. Contacting S&amp;S Legal through this website does not create a lawyer–client relationship.</p>
      <div class="frow2"><span>© {FIRM["year"]} S&amp;S Legal</span><a href="{p}privacy/index.html">Privacy notice</a></div>
    </div>
  </div>
</footer>

<div class="mobile-bar" aria-label="Quick contact">
  <a class="btn btn-ghost" href="tel:{FIRM["phone_tel"]}">Call</a>
  <a class="btn btn-wa" href="https://wa.me/{FIRM["whatsapp"]}" target="_blank" rel="noopener">WhatsApp</a>
</div>
<script src="{p}assets/js/site.js"></script>
</body>
</html>
'''

def page(path, depth, active, title, desc, body, extra=''):
    p = '../' * depth
    html = head(p, path, title, desc, extra) + header(p, active) + '<main id="main">\n' + body(p) + '\n</main>\n\n' + footer(p)
    out = os.path.join(ROOT, path or 'index.html')
    if out.endswith('/'):
        out += 'index.html'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    PAGES.append(path)

PAGES = []

def card(p, slug):
    x = PEOPLE[slug]
    return (f'<a class="person" href="{p}lawyers/{slug}/index.html"><div class="photo"><img loading="lazy" width="{x["w"]}" height="{x["h"]}" src="{p}assets/img/{x["img"]}" alt="{x["name"]}"></div>'
            f'<h3>{x["short"]}</h3><span class="role">{x["card_role"]}</span><p>{x["card_text"]}</p><span class="cred">{x["card_cred"]}</span></a>')

def cta(p, title_html):
    return (f'<section class="cta-band"><div class="wrap"><h2>{title_html}</h2><div class="cta-row">'
            f'<a class="btn btn-gold" href="{p}contact/index.html">Request a consultation {ARROW}</a>'
            f'<a class="btn btn-line" href="tel:{FIRM["phone_tel"]}">{FIRM["phones"][0]}</a></div></div></section>')

def consult_form(p, fid):
    groups = ''.join(f'<option>{g["title"]}</option>' for g in GROUPS.values())
    return f'''<form class="form consult" id="{fid}" novalidate aria-labelledby="{fid}-title">
  <h3 id="{fid}-title">Request a consultation</h3>
  <div class="frow">
    <label for="{fid}-name">Full name<input id="{fid}-name" name="name" type="text" autocomplete="name" required></label>
    <label for="{fid}-phone">Phone / WhatsApp<input id="{fid}-phone" name="phone" type="tel" autocomplete="tel" placeholder="+233"></label>
  </div>
  <div class="frow">
    <label for="{fid}-email">Email<input id="{fid}-email" name="email" type="email" autocomplete="email"></label>
    <label for="{fid}-area">Area<select id="{fid}-area" name="area">{groups}<option>Not sure yet</option></select></label>
  </div>
  <label for="{fid}-msg">Briefly, what is happening?<textarea id="{fid}-msg" name="message" rows="3" placeholder="The other party, key dates and any court deadline."></textarea></label>
  <button class="btn btn-gold" type="submit">Send request {ARROW}</button>
  <p class="sent status" role="status" hidden></p>
  <p class="fine">Sending a request does not create a lawyer–client relationship. Please don’t share confidential documents until we confirm there is no conflict of interest. See our <a href="{p}privacy/index.html" style="color:inherit">privacy notice</a>.</p>
</form>'''

def contact_block(p, fid, heading_tag='h2', heading='Let’s talk about <em>your matter.</em>'):
    phones = '<br>'.join(FIRM['phones'])
    return f'''<span class="label">Contact</span>
      <{heading_tag} id="{fid}-heading" class="contact-h" style="margin-top:20px">{heading}</{heading_tag}>
      <div class="close-grid">
        <div class="cinfo">
          <div class="ci"><span class="label">Office</span><span class="v">{"<br>".join(FIRM["address_lines"])}</span><a class="s" href="{FIRM["maps"]}" target="_blank" rel="noopener">Open in Google Maps ↗</a></div>
          <div class="ci"><span class="label">Hours</span><span class="v">Monday – Friday<br>8:00am – 5:00pm</span></div>
          <div class="ci"><span class="label">Telephone</span><span class="v">{phones}</span><button class="copy" type="button" data-copy="{" / ".join(FIRM["phones"])}">Copy numbers</button></div>
          <div class="ci"><span class="label">Email</span><span class="v">{FIRM["email"]}</span><button class="copy" type="button" data-copy="{FIRM["email"]}">Copy email</button></div>
          <div class="ci" style="grid-column:1/-1;flex-direction:row;flex-wrap:wrap;gap:12px"><a class="btn btn-wa" href="https://wa.me/{FIRM["whatsapp"]}" target="_blank" rel="noopener">Message us on WhatsApp</a><a class="btn" style="border-color:var(--band-line);color:var(--on-band)" href="{FIRM["facebook"]}" target="_blank" rel="noopener">Facebook</a></div>
        </div>
        {consult_form(p, fid)}
      </div>'''

def expertise_columns(p):
    def group_col(k):
        g = GROUPS[k]
        areas = [a for a in AREAS if a['group'] == k]
        rows = ''.join(f'<a class="area" href="{p}expertise/{k}/index.html#{a["slug"]}"><h4>{a["title"]}</h4><p>{a["summary"]}</p>{ARROW}</a>' for a in areas)
        return (f'<div class="group"><div class="group-head"><h3><a href="{p}expertise/{k}/index.html">{g["title"]}</a></h3><span>{len(areas):02d} areas</span></div>{rows}'
                f'<a class="group-link" href="{p}expertise/{k}/index.html" style="margin-top:20px">More on {g["title"].lower()} {ARROW}</a></div>')
    return (f'<div class="groups">{group_col("business")}<div class="group-stack">{group_col("disputes")}{group_col("private-clients")}</div></div>')

def founder_band(p):
    r = PEOPLE['richmond-numbo-saaka']
    edu = ''.join(f'<li>{a}<span>{b}</span></li>' for a, b in r['edu'])
    return f'''<section class="founder" aria-labelledby="founder-title">
    <div class="wrap">
      <div class="photo"><img src="{p}assets/img/{r["img"]}" alt="{r["name"]}" width="{r["w"]}" height="{r["h"]}" loading="lazy"></div>
      <div class="founder-copy">
        <span class="label">Founder</span>
        <h2 id="founder-title">Richmond Numbo Saaka, <em>Esq.</em></h2>
        <span class="role">Transactional &amp; Litigation Lawyer</span>
        <p class="bio">Richmond founded S&amp;S Legal in 2017 after building extensive experience in private practice and in academia. He leads the firm’s transactional and dispute resolution work, with particular strength in litigation and alternative dispute resolution.</p>
        <div class="creds">
          <div><h4>Education</h4><ul>{edu}</ul></div>
          <div><h4>Practice before S&amp;S</h4><ul><li>George Sarpong Legal Services<span>Kumasi</span></li><li>Dery &amp; Co.<span>Accra</span></li><li>Sory @ Law<span>Accra</span></li></ul></div>
          <div><h4>Teaching</h4><ul><li>Faculty of Law, KNUST<span>Teaching and research assistant</span></li><li>Faculty of Law, Mountcrest University College<span>Lecturer</span></li></ul></div>
          <div><h4>Memberships</h4><ul><li>Ghana Bar Association<span>Member</span></li><li>Cornell Institute for African Development<span>Fellow</span></li></ul></div>
        </div>
        <div class="cta-row">
          <a class="btn btn-gold" href="{p}lawyers/richmond-numbo-saaka/index.html">Full profile</a>
          <a class="btn btn-line" href="{p}contact/index.html">Contact Richmond</a>
        </div>
      </div>
    </div>
  </section>'''

PILLARS = '''<div class="pillars">
          <div><h3>Experience that counts</h3><p>Legal practice and expertise gained at established firms in Accra and Kumasi, and in university teaching and research.</p></div>
          <div><h3>Faster turnaround</h3><p>No layers of bureaucracy. Work moves quickly from instruction to advice, filing or signature.</p></div>
          <div><h3>Full attention to detail</h3><p>Your matter is handled by lawyers who know it well and are never too busy to answer.</p></div>
        </div>'''

APPROACH = '''<section class="approach" aria-labelledby="approach-title">
    <div class="wrap">
      <div class="sec-head"><div class="t"><span class="label">Working with us</span><h2 id="approach-title">What happens after <em>you get in touch</em>.</h2></div></div>
      <ol class="steps">
        <li><span class="w">First · Day one</span><h3>A conversation</h3><p>Tell us what is happening by phone, WhatsApp, email or at our office in Osu.</p></li>
        <li><span class="w">Then · Within days</span><h3>Clear options</h3><p>We review your documents and set out your options, risks and likely timeline in plain language.</p></li>
        <li><span class="w">Before work begins</span><h3>Agreed terms</h3><p>An engagement letter records exactly what we will do and what it will cost.</p></li>
        <li><span class="w">Throughout</span><h3>Steady updates</h3><p>You hear from us at every stage, from filing and hearings to settlement or signature.</p></li>
      </ol>
    </div>
  </section>'''

def crumbs(p, items):
    out = [f'<a href="{p}index.html">Home</a>']
    for label, url in items:
        out.append('<span aria-hidden="true">/</span>')
        out.append(f'<a href="{p}{url}">{label}</a>' if url else f'<span>{label}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + ''.join(out) + '</nav>'

# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
LD_FIRM = json.dumps({
    '@context': 'https://schema.org', '@type': 'LegalService', 'name': 'S&S Legal', 'url': SITE_URL,
    'logo': SITE_URL + 'assets/img/sslegal-logo.png', 'foundingDate': '2017',
    'founder': {'@type': 'Person', 'name': 'Richmond Numbo Saaka'},
    'telephone': ['+233244476615', '+233547931937'], 'email': 'info@sslegal.org',
    'address': {'@type': 'PostalAddress', 'streetAddress': 'F233/2 Wentum Street, off Lokko Street', 'addressLocality': 'Osu, Accra', 'addressCountry': 'GH'},
    'openingHours': 'Mo-Fr 08:00-17:00', 'sameAs': ['https://www.facebook.com/sslegal.org'], 'areaServed': 'Ghana',
    'employee': [{'@type': 'Person', 'name': x['name'], 'url': SITE_URL + f'lawyers/{s}/'} for s, x in PEOPLE.items()],
}, ensure_ascii=False)

def home(p):
    others = [s for s in PEOPLE if s != 'richmond-numbo-saaka']
    return f'''<div class="top">
  <section class="hero" aria-labelledby="hero-title">
    <div class="wrap">
      <div class="hero-copy">
        <span class="label">Barristers &amp; Solicitors · Osu, Accra · Since 2017</span>
        <h1 id="hero-title">The experience of a leading firm. <em>The attention of a focused one.</em></h1>
        <p class="sub">S&amp;S Legal advises businesses, investors and families across corporate, finance, property and private client matters, and resolves disputes in court and through arbitration.</p>
        <div class="cta-row">
          <a class="btn btn-main" href="{p}contact/index.html">Request a consultation {ARROW}</a>
          <a class="btn btn-ghost" href="{p}expertise/index.html">Explore our expertise</a>
        </div>
      </div>
      <figure class="hero-figure">
        <div class="mosaic">
          <div class="frame tall"><img src="{p}assets/img/nana-akwasi.jpg" alt="Nana Akwasi Asafo-Adjei in wig and gown" width="500" height="606"></div>
          <div class="frame"><img src="{p}assets/img/abdulrazak-sania.jpg" alt="Dr Abdul Razak Sania in court dress" width="500" height="606"></div>
          <div class="frame"><img src="{p}assets/img/bassing-kamaldeen.jpg" alt="Bassing Ali Kamaldeen in court dress" width="500" height="606"></div>
        </div>
        <figcaption><b>Our lawyers</b><span>Litigation, transactions and advisory, from one team in Osu</span><a href="{p}lawyers/index.html">Meet the team →</a></figcaption>
      </figure>
    </div>
  </section>
  <div class="facts">
    <div class="wrap">
      <dl>
        <div><dt>Established</dt><dd>2017, Accra</dd></div>
        <div><dt>Practice areas</dt><dd>Eleven, in three groups</dd></div>
        <div><dt>Disputes</dt><dd>Courts and arbitration</dd></div>
        <div><dt>Membership</dt><dd>Ghana Bar Association</dd></div>
      </dl>
    </div>
  </div>
</div>

  <section class="statement" id="firm" aria-labelledby="firm-label">
    <div class="wrap">
      <span class="label" id="firm-label">The firm</span>
      <div>
        <p class="big">Our lawyers built their practice at some of Ghana’s notable firms. <span>At S&amp;S Legal they bring that expertise to a small, focused team, with faster turnaround and the flexibility to give every client full attention.</span></p>
        {PILLARS}
      </div>
    </div>
  </section>

  <section class="expertise" id="expertise" aria-labelledby="exp-title">
    <div class="wrap">
      <div class="sec-head">
        <div class="t"><span class="label">Expertise</span><h2 id="exp-title">Eleven practice areas, <em>three ways we help</em>.</h2></div>
        <a class="more" href="{p}expertise/index.html">All expertise</a>
      </div>
      {expertise_columns(p)}
    </div>
  </section>

  {founder_band(p)}

  <section class="team" id="lawyers" aria-labelledby="team-title">
    <div class="wrap">
      <div class="sec-head">
        <div class="t"><span class="label">Our lawyers</span><h2 id="team-title">The team behind <em>every matter</em>.</h2></div>
        <a class="more" href="{p}lawyers/index.html">All lawyers</a>
      </div>
      <div class="people">{"".join(card(p, s) for s in others)}</div>
      <p class="support">Supported by <b>{SUPPORT[0]}</b>, {SUPPORT[1]}.</p>
    </div>
  </section>

  {APPROACH}

  <section class="close" id="contact" aria-labelledby="home-form-heading">
    <div class="wrap">
      {contact_block(p, "home-form")}
    </div>
  </section>'''

def expertise_overview(p):
    cards = ''
    for k, g in GROUPS.items():
        lis = ''.join(f'<li>{a["title"]}</li>' for a in AREAS if a['group'] == k)
        cards += f'<a class="gcard" href="{p}expertise/{k}/index.html"><span class="label">Practice group</span><h2>{g["title"]}</h2><p>{g["card"]}</p><ul>{lis}</ul><span class="go">View {g["title"].lower()} {ARROW}</span></a>'
    return f'''<section class="page-hero" aria-labelledby="ptitle"><div class="wrap">
  {crumbs(p, [("Expertise", None)])}
  <span class="label">Expertise</span>
  <h1 id="ptitle">Eleven practice areas, <em>three ways we help</em>.</h1>
  <p class="sub">From company formation and finance to disputes in court and the wishes of a family, our work is organised in three practice groups.</p>
</div></section>
<section class="areas-detail" aria-label="Practice groups"><div class="wrap"><div class="overview-groups">{cards}</div></div></section>
<section class="expertise" aria-labelledby="all-title"><div class="wrap">
  <div class="sec-head"><div class="t"><span class="label">All practice areas</span><h2 id="all-title">Find your <em>area</em>.</h2></div></div>
  {expertise_columns(p)}
</div></section>
''' + cta(p, 'Not sure which area? <em>Ask us.</em>')

ROUTES = '''<section class="routes" aria-labelledby="routes-title"><div class="wrap">
  <div class="sec-head"><div class="t"><span class="label">Your options</span><h2 id="routes-title">Two routes to <em>a resolution</em>.</h2><p>We advise on the route that best protects your position, and we can change course if a dispute develops.</p></div></div>
  <div class="route-grid">
    <div class="route"><span class="label">In court</span><h3>When rights must be decided and enforced</h3><p>We prepare, file and argue your case, and see it through to judgment and enforcement.</p><ul><li>Bringing and defending claims</li><li>Hearings and trial</li><li>Enforcing judgments and court orders</li></ul></div>
    <div class="route"><span class="label">Outside court</span><h3>When a faster, private outcome is better</h3><p>We negotiate, mediate or arbitrate to reach a resolution without a trial where that serves you.</p><ul><li>Negotiation</li><li>Mediation</li><li>Arbitration</li></ul></div>
  </div>
</div></section>'''

def group_page(k):
    g = GROUPS[k]
    areas = [a for a in AREAS if a['group'] == k]
    people = [s for s in PEOPLE if any(s in a['lawyers'] for a in areas)]
    def body(p):
        rows = ''
        for i, a in enumerate(areas, 1):
            who = ''
            if a['lawyers']:
                who = '<span class="who">Lawyers</span><div class="chips">' + ''.join(f'<a href="{p}lawyers/{s}/index.html">{PEOPLE[s]["name"]}</a>' for s in a['lawyers']) + '</div>'
            paras = ''.join(f'<p>{x}</p>' for x in a['body'])
            rows += f'<article class="adetail" id="{a["slug"]}"><span class="n">{i:02d}</span><h2>{a["title"]}</h2><div class="body">{paras}{who}</div></article>'
        team = ''
        if people:
            team = f'''<section class="colleagues" id="lawyers" aria-labelledby="gl-title"><div class="wrap">
  <div class="sec-head"><div class="t"><span class="label">Lawyers in this group</span><h2 id="gl-title">Who will <em>handle your matter</em>.</h2></div><a class="more" href="{p}lawyers/index.html">All lawyers</a></div>
  <div class="people three">{"".join(card(p, s) for s in people)}</div>
</div></section>'''
        others = ''.join(f'<a href="{p}expertise/{o}/index.html">{GROUPS[o]["title"]}</a>' for o in GROUPS if o != k)
        return f'''<section class="page-hero" aria-labelledby="ptitle"><div class="wrap">
  {crumbs(p, [("Expertise", "expertise/index.html"), (g["title"], None)])}
  <span class="label">Practice group · {g["title"]}</span>
  <h1 id="ptitle">{g["h1"]}</h1>
  <p class="sub">{g["intro"]}</p>
  <div class="cta-row"><a class="btn btn-main" href="{p}contact/index.html">Discuss your matter {ARROW}</a>{'<a class="btn btn-ghost" href="#lawyers">Lawyers in this group</a>' if people else ''}</div>
</div></section>
<section class="areas-detail" aria-label="Areas in this group"><div class="wrap">{rows}
  <div class="chips" style="margin-top:40px"><span style="border:0;padding-left:0">Other practice groups:</span>{others}</div>
</div></section>
{ROUTES if k == "disputes" else ""}
{team}
''' + cta(p, 'Facing a dispute? <em>Talk to us early.</em>' if k == 'disputes' else 'Speak with <em>our team</em>.')
    page(f'expertise/{k}/', 2, 'expertise', f'{g["title"]} · S&amp;S Legal', g['intro'], body)

def lawyers_index(p):
    return f'''<section class="page-hero" aria-labelledby="ptitle"><div class="wrap">
  {crumbs(p, [("Our lawyers", None)])}
  <span class="label">Our lawyers</span>
  <h1 id="ptitle">The team behind <em>every matter</em>.</h1>
  <p class="sub">A small, focused team of lawyers whose experience spans leading Ghanaian firms, universities, business and public service.</p>
</div></section>
<section class="team" aria-label="Lawyers"><div class="wrap">
  <div class="people five">{"".join(card(p, s) for s in PEOPLE)}</div>
  <p class="support">Supported by <b>{SUPPORT[0]}</b>, {SUPPORT[1]}.</p>
</div></section>
''' + cta(p, 'Speak with <em>our team</em>.')

def profile(slug):
    x = PEOPLE[slug]
    def body(p):
        chips = ''.join(f'<a href="{area_url(p, a)}">{AREA[a]["title"]}</a>' for a in x['areas'])
        chips += ''.join(f'<span>{c}</span>' for c in x.get('extra_chips', []))
        li = lambda items: ''.join(f'<li>{a}<span>{b}</span></li>' for a, b in items)
        side = f'<div><h2>Areas of practice</h2><div class="chips">{chips}</div></div><div><h2>Education</h2><ul>{li(x["edu"])}</ul></div>'
        if x['member']:
            side += f'<div><h2>Memberships</h2><ul>{li(x["member"])}</ul></div>'
        main = '<div><h2>Profile</h2><div class="prose">' + ''.join(f'<p>{t}</p>' for t in x['prose']) + '</div></div>'
        if x['exp']:
            main += f'<div><h2>{x["exp_title"]}</h2><ul class="timeline">' + ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in x['exp']) + '</ul></div>'
        pc = ''.join(f'<span>{k}: <b>{v}</b></span>' for k, v in x['contact'])
        studio = ' studio' if x['studio'] else ''
        others = [s for s in PEOPLE if s != slug]
        return f'''<section class="page-hero profile-hero" aria-labelledby="ptitle">
  <div class="wrap">
    <div class="pcopy">
      {crumbs(p, [("Our lawyers", "lawyers/index.html"), (x["name"], None)])}
      <span class="role">{x["role"]}</span>
      <h1 id="ptitle">{x["first"]} <em>{x["em"]}</em></h1>
      <p class="lead">{x["lead"]}</p>
      <div class="cta-row"><a class="btn btn-main" href="{p}contact/index.html">Request a consultation {ARROW}</a><a class="btn btn-ghost" href="{p}lawyers/index.html">All lawyers</a></div>
      <div class="pc">{pc}</div>
    </div>
    <div class="portrait-lg{studio}"><img src="{p}assets/img/{x["img"]}" alt="{x["name"]}" width="{x["w"]}" height="{x["h"]}"></div>
  </div>
</section>
<section class="profile-body"><div class="wrap"><aside class="side">{side}</aside><div class="main-col">{main}</div></div></section>
<section class="colleagues" aria-labelledby="col-title"><div class="wrap">
  <div class="sec-head"><div class="t"><span class="label">Colleagues</span><h2 id="col-title">Working <em>alongside</em> {x["call"]}.</h2></div><a class="more" href="{p}lawyers/index.html">All lawyers</a></div>
  <div class="people three">{"".join(card(p, s) for s in others)}</div>
</div></section>
''' + cta(p, 'Speak with <em>our team</em>.')
    ld = json.dumps({'@context': 'https://schema.org', '@type': 'Person', 'name': x['name'].replace('&amp;', '&'),
                     'jobTitle': x['card_role'].replace('&amp;', '&'), 'worksFor': {'@type': 'LegalService', 'name': 'S&S Legal', 'url': SITE_URL},
                     'image': SITE_URL + 'assets/img/' + x['img'], 'url': SITE_URL + f'lawyers/{slug}/'}, ensure_ascii=False)
    page(f'lawyers/{slug}/', 2, 'lawyers', f'{x["name"]} · S&amp;S Legal', f'{x["name"]}, {x["card_role"]} at S&amp;S Legal, Osu, Accra.', body,
         f'<script type="application/ld+json">{ld}</script>\n')

def about(p):
    return f'''<section class="page-hero" aria-labelledby="ptitle"><div class="wrap">
  {crumbs(p, [("About", None)])}
  <span class="label">About S&amp;S Legal</span>
  <h1 id="ptitle">A focused firm, <em>founded in 2017</em>.</h1>
  <p class="sub">Established in 2017 by Richmond Numbo Saaka, S&amp;S Legal provides a range of corporate services, and resolves disputes through litigation in court and alternative dispute resolution such as arbitration.</p>
</div></section>
<section class="statement" aria-labelledby="why-label"><div class="wrap">
  <span class="label" id="why-label">Why clients choose us</span>
  <div>
    <p class="big">Our lawyers built their practice at some of Ghana’s notable firms. <span>Work is done by a small, focused team that concentrates on delivering excellent legal service to each client, without bureaucracy or layers of redundancy.</span></p>
    {PILLARS}
  </div>
</div></section>
{founder_band(p)}
{APPROACH}
<section class="team" aria-labelledby="team-title"><div class="wrap">
  <div class="sec-head"><div class="t"><span class="label">Our people</span><h2 id="team-title">Meet <em>the team</em>.</h2></div><a class="more" href="{p}lawyers/index.html">All lawyers</a></div>
  <div class="people">{"".join(card(p, s) for s in PEOPLE if s != "richmond-numbo-saaka")}</div>
  <p class="support">Supported by <b>{SUPPORT[0]}</b>, {SUPPORT[1]}.</p>
</div></section>
''' + cta(p, 'Speak with <em>our team</em>.')

def contact(p):
    return f'''<section class="contact-page" aria-labelledby="contact-form-heading"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb" style="margin-bottom:28px"><a href="{p}index.html" style="color:var(--on-band-2)">Home</a><span aria-hidden="true">/</span><span style="color:var(--on-band-2)">Contact</span></nav>
  {contact_block(p, "contact-form", "h1")}
</div></section>
<section class="routes" aria-labelledby="visit-title"><div class="wrap">
  <div class="sec-head"><div class="t"><span class="label">Visiting the office</span><h2 id="visit-title">Find us <em>in Osu</em>.</h2><p>Our office is on Wentum Street, off Lokko Street in Osu, Accra. Please call ahead so a lawyer is free to meet you.</p></div></div>
  <div class="route-grid">
    <div class="route"><span class="label">Address</span><h3>F233/2 Wentum Street</h3><p>Off Lokko Street, Osu, Accra, Ghana</p><ul><li><a href="{FIRM["maps"]}" target="_blank" rel="noopener">Open in Google Maps</a></li></ul></div>
    <div class="route"><span class="label">Before you come</span><h3>What to bring</h3><p>Bring any contracts, letters, court papers and a list of key dates. If you have been served, tell us the date of service straight away.</p><ul><li>{FIRM["hours"]}</li></ul></div>
  </div>
</div></section>'''

def privacy(p):
    return f'''<section class="page-hero" aria-labelledby="ptitle"><div class="wrap">
  {crumbs(p, [("Privacy notice", None)])}
  <h1 id="ptitle">Privacy <em>notice</em>.</h1>
  <p class="sub">How S&amp;S Legal handles the information you share with us through this website.</p>
</div></section>
<section class="prose-page"><div class="wrap">
  <h2>Who we are</h2>
  <p>S&amp;S Legal is a law firm at {FIRM["address_one"]}. You can contact us at {FIRM["email"]} or on {FIRM["phones"][0]}.</p>
  <h2>What we collect</h2>
  <p>When you request a consultation, email or call us, we receive the details you choose to share: your name, phone number, email address and a description of your matter.</p>
  <h2>How we use it</h2>
  <ul><li>To reply to your request and arrange a consultation.</li><li>To check for conflicts of interest before we discuss your matter.</li><li>To provide legal services, if you instruct us.</li></ul>
  <h2>This website</h2>
  <p>This website does not use advertising or tracking cookies. If you choose a light or dark theme, that choice is stored only in your own browser.</p>
  <h2>Sharing</h2>
  <p>We do not sell your information. We share it only where needed to provide legal services to you, or where the law requires it.</p>
  <h2>Your rights</h2>
  <p>Under the Data Protection Act, 2012 (Act 843), you may ask to see the personal information we hold about you, and ask us to correct it. Write to {FIRM["email"]}.</p>
  <p style="margin-top:32px;font-size:14px;color:var(--muted)">Last updated November 2026.</p>
</div></section>'''

def not_found():
    # Served for any missing path, so links are root-relative.
    def body(p):
        return f'''<section class="page-hero" aria-labelledby="ptitle"><div class="wrap">
  <span class="label">Page not found</span>
  <h1 id="ptitle">We couldn’t find <em>that page</em>.</h1>
  <p class="sub">It may have moved when our website was updated. Try one of these instead.</p>
  <div class="cta-row"><a class="btn btn-main" href="/index.html">Home</a><a class="btn btn-ghost" href="/expertise/index.html">Expertise</a><a class="btn btn-ghost" href="/lawyers/index.html">Our lawyers</a><a class="btn btn-ghost" href="/contact/index.html">Contact</a></div>
</div></section>'''
    html = head('/', '404.html', 'Page not found · S&amp;S Legal', 'This page could not be found.') + header('/', None) + '<main id="main">\n' + body('/') + '\n</main>\n\n' + footer('/')
    with open(os.path.join(ROOT, '404.html'), 'w', encoding='utf-8') as f:
        f.write(html)

# --------------------------------------------------------------------------
def main():
    page('', 0, None, 'S&amp;S Legal · Barristers &amp; Solicitors, Accra',
         'S&amp;S Legal is a law firm in Osu, Accra, advising businesses, investors and families on corporate, finance, property and private client matters, and resolving disputes in court and through arbitration.',
         home, f'<script type="application/ld+json">{LD_FIRM}</script>\n')
    page('expertise/', 1, 'expertise', 'Expertise · S&amp;S Legal', 'Eleven practice areas in three groups: Business, Disputes and Private clients.', expertise_overview)
    for k in GROUPS:
        group_page(k)
    page('lawyers/', 1, 'lawyers', 'Our lawyers · S&amp;S Legal', 'Meet the lawyers of S&amp;S Legal in Osu, Accra.', lawyers_index)
    for s in PEOPLE:
        profile(s)
    page('about/', 1, 'about', 'About · S&amp;S Legal', 'S&amp;S Legal was founded in 2017 by Richmond Numbo Saaka. A focused team for corporate work and dispute resolution.', about)
    page('contact/', 1, 'contact', 'Contact · S&amp;S Legal', 'Contact S&amp;S Legal in Osu, Accra: +233 24 447 6615, info@sslegal.org.', contact)
    page('privacy/', 1, None, 'Privacy notice · S&amp;S Legal', 'How S&amp;S Legal handles information shared through this website.', privacy)
    not_found()
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for path in PAGES:
            f.write(f'  <url><loc>{SITE_URL}{path}</loc></url>\n')
        f.write('</urlset>\n')
    with open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n')
    print(f'Built {len(PAGES) + 1} pages.')

if __name__ == '__main__':
    main()
