from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


ORIGINAL_PAGES = [
    ("About ISH", "https://www.hantavirussociety.org/about-ish"),
    ("ICH2026", "https://www.hantavirussociety.org/ich2026"),
    ("Keynote Speakers", "https://www.hantavirussociety.org/ich2026/keynote-speakers"),
    ("Programme", "https://www.hantavirussociety.org/ich2026/programme"),
    ("Abstracts & Registration", "https://www.hantavirussociety.org/ich2026/abstracts-registration"),
    ("Venue", "https://www.hantavirussociety.org/ich2026/venue"),
    ("Partners & Sponsors", "https://www.hantavirussociety.org/ich2026/partners-sponsors"),
    ("Contact", "https://www.hantavirussociety.org/contact"),
]

NAV = [
    ("about", "About ISH", "about-ish/"),
    ("ich2026", "ICH2026", "ich2026/"),
    ("keynote", "Keynotes", "ich2026/keynote-speakers/"),
    ("programme", "Programme", "ich2026/programme/"),
    ("registration", "Registration", "ich2026/abstracts-registration/"),
    ("venue", "Venue", "ich2026/venue/"),
    ("sponsors", "Sponsors", "ich2026/partners-sponsors/"),
    ("contact", "Contact", "contact/"),
]

MEMBERSHIP_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSc0IHUnT80-qDJn2wU4pLXKQ1F_VEdcziqVL-47iGGAwsLBEA/viewform?pli=1"
CONFERENCE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfMc-cPx3hL8-Q67gN3uFLpQiZlgOD5lr03vvze29w4axGWtQ/viewform"

BOARD = [
    ("Nicole Tischler", "President ISH | Chile", "board/nicole-tischler.jpg", "https://orcid.org/0000-0002-4578-4780"),
    ("Piet Maes", "President Elect | Belgium", "board/piet-maes.jpg", "https://orcid.org/0000-0002-4571-5232"),
    ("Colleen B. Jonsson", "Secretary ISH | USA", "board/colleen-jonsson.jpg", "https://orcid.org/0000-0002-2640-7672"),
    ("Jin Won Song", "Past-President | Korea", "board/jin-won-song.jpg", "https://orcid.org/0000-0003-0796-8332"),
    ("Satoru Arai", "Japan", "board/satoru-arai.jpg", "https://orcid.org/0000-0001-5865-0717"),
    ("Tatjana Avsic-Zupanc", "Slovenia", "board/tatjana-avsic-zupanc.jpg", "https://orcid.org/0000-0001-6243-0688"),
    ("Roger Hewson", "United Kingdom", "board/roger-hewson.jpg", "https://orcid.org/0000-0003-2273-3152"),
    ("Boris Klempa", "Slovakia", "board/boris-klempa.jpg", "https://orcid.org/0000-0002-6931-1224"),
    ("Jonas Klingstrom", "Sweden", "board/jonas-klingstrom.jpg", "https://orcid.org/0000-0001-9076-1441"),
    ("Dexin Li", "China", "board/dexin-li.jpg", ""),
    ("Mifang Liang", "China", "board/mifang-liang.jpg", ""),
    ("Alemka Markotic", "Croatia", "board/almeka-markotic.jpg", "https://orcid.org/0000-0003-4104-7940"),
    ("Valeria Martinez", "Argentina", "board/valeria-martinez.jpg", "https://orcid.org/0000-0002-4356-8136"),
    ("Gustavo Palacios", "USA", "board/gustavo-palacios.jpg", "https://orcid.org/0000-0001-5062-1938"),
    ("Anna Papa", "Greece", "board/anna-papa.jpg", "https://orcid.org/0000-0002-6643-3322"),
    ("Liudmila Yashina", "Russia", "board/liudmila-yashina.jpg", "https://orcid.org/0000-0003-2844-7835"),
    ("Connie Schmaljohn", "Honorary Member | USA", "board/connie-schmaljohn.jpg", "https://orcid.org/0000-0001-8852-5482"),
]

COMMITTEE = [
    ("Nicole Tischler", "Fundacion Ciencia & Vida | Chile", "https://orcid.org/0000-0002-4578-4780"),
    ("Piet Maes", "KU Leuven | Belgium", "https://orcid.org/0000-0002-4571-5232"),
    ("Colleen B. Jonsson", "University of Tennessee | USA", "https://orcid.org/0000-0002-2640-7672"),
    ("Jin Won Song", "Korea University | Korea", "https://orcid.org/0000-0003-0796-8332"),
    ("Satoru Arai", "Japan", "https://orcid.org/0000-0001-5865-0717"),
    ("Steven Bradfute", "University of New Mexico | USA", "https://orcid.org/0000-0002-1985-751X"),
    ("Roger Hewson", "United Kingdom", "https://orcid.org/0000-0003-2273-3152"),
    ("Boris Klempa", "Slovak Academy of Sciences | Slovakia", "https://orcid.org/0000-0002-6931-1224"),
    ("Jonas Klingstrom", "Linkoping University | Sweden", "https://orcid.org/0000-0001-9076-1441"),
    ("Valeria Martinez", "INEI / ANLIS Dr. C. G. Malbran | Argentina", "https://orcid.org/0000-0002-4356-8136"),
    ("Gustavo Palacios", "Icahn School of Medicine at Mount Sinai | USA", "https://orcid.org/0000-0001-5062-1938"),
    ("Jenniffer Angulo", "Chile", "https://orcid.org/0000-0002-0471-4751"),
    ("Maria Ines Barria", "Chile", "https://orcid.org/0000-0001-6225-5971"),
    ("Mario Calvo", "Chile", "https://orcid.org/0000-0002-1796-2236"),
    ("Marcela Ferres", "Pontificia Universidad Catolica de Chile", "https://orcid.org/0000-0001-9415-4657"),
    ("Juan Hormazabal", "Chile", "https://orcid.org/0000-0003-0726-2778"),
    ("Nicole Le Corre", "Chile", "https://orcid.org/0000-0002-9361-4049"),
    ("Constanza Martinez-Valdevenito", "Pontificia Universidad Catolica de Chile", "https://orcid.org/0000-0002-2836-9817"),
    ("Fernando Torres-Perez", "Pontificia Universidad Catolica de Valparaiso", "https://orcid.org/0000-0001-8655-7288"),
    ("Cecilia Vial", "Universidad del Desarrollo", "https://orcid.org/0000-0002-0399-6144"),
    ("Pablo Vial", "Universidad del Desarrollo", "https://orcid.org/0000-0002-4135-0416"),
]

SPONSORS = [
    ("Sociedad Chilena de Microbiologia", "https://somich.cl/", "sponsors/somich.png"),
    ("Centro Basal Ciencia & Vida", "https://www.cienciavida.org/", "sponsors/ciencia-vida.png"),
    ("Universidad San Sebastian", "https://www.uss.cl/", "sponsors/universidad-san-sebastian.jpg"),
    ("Pontificia Universidad Catolica de Chile", "https://www.uc.cl/", "sponsors/universidad-catolica.jpg"),
    ("Universidad del Desarrollo", "https://www.udd.cl/", "sponsors/universidad-del-desarrollo.png"),
    ("ANID", "https://anid.cl/", "sponsors/anid.png"),
]

TRAVEL_LINKS = [
    ("Hotel Bellavista", "https://hotelbellavista.cl/reuniones-y-eventos-corporativos-2/"),
    ("Venue map", "https://goo.gl/maps/dv2jUC4hSGLvr2Ld9"),
    ("Santiago airport", "https://thesantiagoairport.com/"),
    ("Santiago day trips", "https://www.tripadvisor.com/Attractions-g294305-Activities-c42-t205-Santiago_Santiago_Metropolitan_Region.html"),
    ("Santiago tours", "https://www.viator.com/Santiago/d713?pid=P00095352&mcid=42383&medium=link&campaign=scltours"),
    ("Airport transfer", "https://ww2.trasladoaeropuerto.cl/"),
    ("Transfer WhatsApp", "https://api.whatsapp.com/send?phone=56976053701&text=hola,%20lo%20contacto%20desde%20la%20p%C3%A1gina%20web"),
    ("Survip transfer", "https://www.survip.cl/transfer-aeropuerto-puerto-montt-a-puerto-varas.php"),
]


def prefix_for(out_path: str) -> str:
    parent = Path(out_path).parent
    return "" if str(parent) == "." else "../" * len(parent.parts)


def img(prefix: str, asset_path: str) -> str:
    return f"{prefix}assets/images/{asset_path}"


def local(prefix: str, path: str = "") -> str:
    return f"{prefix}{path}"


def attrs(**values: str) -> str:
    return " ".join(f'{key.replace("_", "-")}="{escape(value)}"' for key, value in values.items() if value)


def header(prefix: str, active: str) -> str:
    nav = []
    for key, label, href in NAV:
        current = ' aria-current="page"' if key == active else ""
        nav.append(f'<a href="{local(prefix, href)}" data-nav="{key}"{current}>{escape(label)}</a>')
    return f"""
    <header class="site-header" data-header>
      <a class="brand" href="{local(prefix)}" aria-label="International Society for Hantaviruses">
        <img class="brand-logo" src="{img(prefix, "ui/logo.png")}" alt="International Society for Hantaviruses logo" loading="eager">
        <span class="brand-copy">
          <strong>International Society</strong>
          <span>for Hantaviruses</span>
        </span>
      </a>
      <button class="menu-toggle" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="site-menu" data-menu-toggle>
        <span></span>
        <span></span>
        <span></span>
        <span class="sr-only">Menu</span>
      </button>
      <nav class="site-nav" id="site-menu" aria-label="Primary navigation" data-menu>
        {"".join(nav)}
      </nav>
    </header>"""


def footer(prefix: str) -> str:
    originals = "\n".join(
        f'<a href="{href}" target="_blank" rel="noreferrer">{escape(label)}</a>' for label, href in ORIGINAL_PAGES
    )
    return f"""
    <footer class="site-footer-rich">
      <div>
        <img src="{img(prefix, "ui/logo.png")}" alt="International Society for Hantaviruses logo" loading="lazy">
        <p>Website of the International Society for Hantaviruses.</p>
      </div>
      <nav aria-label="Site pages">
        <strong>Site</strong>
        <a href="{local(prefix, "about-ish/")}">About ISH</a>
        <a href="{local(prefix, "ich2026/")}">ICH2026</a>
        <a href="{local(prefix, "ich2026/abstracts-registration/")}">Registration</a>
        <a href="{local(prefix, "contact/")}">Contact</a>
      </nav>
      <nav aria-label="Original Google Sites pages">
        <strong>Original Google Sites</strong>
        {originals}
      </nav>
      <nav aria-label="Actions">
        <strong>Actions</strong>
        <a href="{MEMBERSHIP_FORM}" target="_blank" rel="noreferrer">Apply for ISH membership</a>
        <a href="{CONFERENCE_FORM}" target="_blank" rel="noreferrer">Conference form</a>
        <a href="mailto:ICH2026@hantavirussociety.org">ICH2026@hantavirussociety.org</a>
      </nav>
    </footer>"""


def doc(out_path: str, active: str, title: str, description: str, body: str) -> str:
    prefix = prefix_for(out_path)
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{escape(description)}">
    <title>{escape(title)}</title>
    <link rel="icon" href="{img(prefix, "ui/logo.png")}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Source+Serif+4:wght@500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{prefix}styles.css">
  </head>
  <body data-page="{active}">
{header(prefix, active)}
    <main id="top">
{body}
    </main>
{footer(prefix)}
    <script src="{prefix}script.js" defer></script>
  </body>
</html>
"""


def home_page(prefix: str) -> str:
    return f"""
      <section class="hero" aria-labelledby="hero-title">
        <picture class="hero-media">
          <img src="{img(prefix, "venue/puerto-varas-hero.jpg")}" alt="Puerto Varas landscape for the International Conference on Hantaviruses" fetchpriority="high">
        </picture>
        <div class="hero-overlay"></div>
        <div class="hero-content reveal is-visible">
          <img class="hero-logo" src="{img(prefix, "ui/logo.png")}" alt="International Society for Hantaviruses logo" loading="eager">
          <p class="eyebrow">Research collaboration since 1989</p>
          <h1 id="hero-title">International Society for Hantaviruses</h1>
          <p class="hero-lede">A global scientific network advancing hantavirus research, clinical knowledge and international collaboration.</p>
          <div class="hero-actions" aria-label="Primary actions">
            <a class="button button-primary" href="{local(prefix, "ich2026/")}">ICH2026 in Chile</a>
            <a class="button button-secondary" href="{MEMBERSHIP_FORM}" target="_blank" rel="noreferrer">Apply for membership</a>
            <a class="button button-ghost" href="{local(prefix, "ich2026/abstracts-registration/")}">Abstracts & registration</a>
          </div>
        </div>
        <aside class="hero-panel" aria-label="Conference date">
          <span>International Conference on Hantaviruses</span>
          <strong>Nov 2-5, 2026</strong>
          <small>Puerto Varas, Chile</small>
          <a href="{local(prefix, "ich2026/programme/")}">Programme</a>
        </aside>
      </section>
      <section class="section intro-band">
        <div class="section-shell two-column">
          <div class="section-heading reveal">
            <p class="eyebrow">About ISH</p>
            <h2>Science-led coordination for a global zoonotic disease community.</h2>
          </div>
          <div class="prose reveal">
            <p>The International Society for Hantaviruses promotes knowledge on hantaviruses and associated diseases through research exchange, training and international scientific cooperation.</p>
            <p>The society connects experts in epidemiology, ecology, viral replication, host-pathogen interaction, pathogenesis, diagnostics, clinical care, vaccines and therapeutics.</p>
          </div>
        </div>
        <div class="section-shell society-gallery" aria-label="ISH visual archive">
          <figure class="reveal">
            <img src="{img(prefix, "ui/society-archive-1.png")}" alt="International hantavirus scientific meeting" loading="lazy" decoding="async">
            <figcaption>International scientific exchange</figcaption>
          </figure>
          <figure class="reveal">
            <img src="{img(prefix, "ui/society-archive-2.png")}" alt="ISH conference participants" loading="lazy" decoding="async">
            <figcaption>Research community and training</figcaption>
          </figure>
        </div>
      </section>
      <section class="section data-section">
        <div class="section-shell">
          <div class="section-heading compact reveal">
            <p class="eyebrow">Research focus</p>
            <h2>A practical agenda for hantavirus science.</h2>
          </div>
          <div class="focus-grid" role="list">
            <article class="focus-item reveal" role="listitem"><span>01</span><h3>Epidemiology & ecology</h3><p>Tracking viral diversity, reservoirs, climate influence and regional transmission dynamics.</p></article>
            <article class="focus-item reveal" role="listitem"><span>02</span><h3>Virus-host biology</h3><p>Understanding replication, immune response, pathogenesis and host-pathogen interaction.</p></article>
            <article class="focus-item reveal" role="listitem"><span>03</span><h3>Diagnostics & care</h3><p>Improving early diagnosis, clinical management and risk assessment after exposure.</p></article>
            <article class="focus-item reveal" role="listitem"><span>04</span><h3>Vaccines & therapeutics</h3><p>Accelerating translational work on prevention, treatment and preparedness.</p></article>
          </div>
        </div>
      </section>
      <section class="section committees">
        <div class="section-shell">
          <div class="section-heading compact reveal">
            <p class="eyebrow">International Advisory Board</p>
            <h2>A global board connecting countries affected by hantavirus disease.</h2>
          </div>
          {advisory_grid(prefix)}
        </div>
      </section>
      <section class="section contact-band">
        <div class="section-shell contact-layout">
          <div class="section-heading reveal">
            <p class="eyebrow">Membership</p>
            <h2>Join the international hantavirus research network.</h2>
          </div>
          <div class="contact-actions reveal">
            <a class="button button-primary" href="{MEMBERSHIP_FORM}" target="_blank" rel="noreferrer">Apply for ISH membership</a>
            <a class="button button-secondary light" href="{local(prefix, "contact/")}">Contact ICH2026</a>
          </div>
        </div>
      </section>"""


def advisory_grid(prefix: str) -> str:
    cards = []
    for name, role, image, href in BOARD:
        heading = f'<a href="{href}" target="_blank" rel="noreferrer">{escape(name)}</a>' if href else escape(name)
        cards.append(
            f'<article class="advisor reveal" role="listitem"><img src="{img(prefix, image)}" alt="{escape(name)}" loading="lazy" decoding="async"><h3>{heading}</h3><p>{escape(role)}</p></article>'
        )
    return f'<div class="advisory-grid" role="list">{"".join(cards)}</div>'


def page_hero(prefix: str, eyebrow: str, title: str, lede: str, image: str, ctas: list[tuple[str, str, str]] | None = None) -> str:
    actions = ""
    if ctas:
        links = "".join(f'<a class="button {klass}" href="{href}">{escape(label)}</a>' for label, href, klass in ctas)
        actions = f'<div class="hero-actions page-actions">{links}</div>'
    return f"""
      <section class="page-hero">
        <img class="page-hero-bg" src="{img(prefix, image)}" alt="" aria-hidden="true">
        <div class="page-hero-overlay"></div>
        <div class="page-hero-copy reveal is-visible">
          <p class="eyebrow">{escape(eyebrow)}</p>
          <h1>{escape(title)}</h1>
          <p class="hero-lede">{escape(lede)}</p>
          {actions}
        </div>
      </section>"""


def ich2026_page(prefix: str) -> str:
    committee_cards = "".join(
        f'<a class="profile-link reveal" href="{href}" target="_blank" rel="noreferrer"><strong>{escape(name)}</strong><span>{escape(role)}</span></a>'
        for name, role, href in COMMITTEE
    )
    return f"""
      {page_hero(prefix, "Puerto Varas | Chile", "International Conference on Hantaviruses 2026", "Four days of scientific exchange in Chile's Lake District, followed by a specialized Andes Virus workshop.", "venue/conference-landscape.png", [( "Programme", local(prefix, "ich2026/programme/"), "button-primary"), ("Registration", local(prefix, "ich2026/abstracts-registration/"), "button-secondary")])}
      <section class="section intro-band">
        <div class="section-shell detail-grid">
          <div class="section-heading reveal"><p class="eyebrow">Conference frame</p><h2>Research, clinical practice and public health in one programme.</h2></div>
          <div class="detail-list reveal">
            <div><span>Dates</span><strong>November 2-5, 2026</strong></div>
            <div><span>Venue</span><strong>Hotel Bellavista, Puerto Varas</strong></div>
            <div><span>Workshop</span><strong>Andes Virus, November 5</strong></div>
          </div>
        </div>
      </section>
      <section class="section data-section">
        <div class="section-shell">
          <div class="section-heading compact reveal"><p class="eyebrow">ICH2026 pages</p><h2>Navigate the conference information by task.</h2></div>
          <div class="resource-grid">
            <a class="resource-item reveal" href="{local(prefix, "ich2026/keynote-speakers/")}"><span>01</span><strong>Keynote speakers</strong><small>Clinical insight and high-consequence virology.</small></a>
            <a class="resource-item reveal" href="{local(prefix, "ich2026/programme/")}"><span>02</span><strong>Programme</strong><small>Sessions and Andes Virus workshop.</small></a>
            <a class="resource-item reveal" href="{local(prefix, "ich2026/abstracts-registration/")}"><span>03</span><strong>Abstracts & registration</strong><small>Submission and registration windows.</small></a>
            <a class="resource-item reveal" href="{local(prefix, "ich2026/venue/")}"><span>04</span><strong>Venue</strong><small>Hotel, map and travel planning.</small></a>
            <a class="resource-item reveal" href="{local(prefix, "ich2026/partners-sponsors/")}"><span>05</span><strong>Partners & sponsors</strong><small>Institutional support.</small></a>
          </div>
        </div>
      </section>
      <section class="section committees">
        <div class="section-shell">
          <div class="section-heading compact reveal"><p class="eyebrow">Scientific and organizing network</p><h2>Committee profiles and ORCID records from the original site.</h2></div>
          <div class="profile-grid">{committee_cards}</div>
        </div>
      </section>"""


def keynote_page(prefix: str) -> str:
    return f"""
      {page_hero(prefix, "Keynote speakers", "Clinical insight and high-consequence virology.", "ICH2026 highlights speakers working across infectious diseases, transmission, diagnostics and medical countermeasures.", "venue/conference-landscape.png")}
      <section class="section speakers">
        <div class="section-shell speaker-grid">
          <article class="speaker reveal">
            <img src="{img(prefix, "speakers/marcela-ferres.png")}" alt="Dr. Marcela Ferres" loading="lazy" decoding="async">
            <div><h2>Dr. Marcela Ferres</h2><p class="speaker-meta">Pontificia Universidad Catolica, Chile</p><p>Pediatric infectious disease specialist studying Andes virus transmission, early diagnosis and viral presence in clinical samples.</p><a class="text-link" href="https://orcid.org/0000-0001-9415-4657" target="_blank" rel="noreferrer">ORCID profile</a></div>
          </article>
          <article class="speaker reveal">
            <img src="{img(prefix, "speakers/jay-hooper.png")}" alt="Dr. Jay Hooper" loading="lazy" decoding="async">
            <div><h2>Dr. Jay Hooper</h2><p class="speaker-meta">USAMRIID, United States</p><p>Chief of the Molecular Virology Branch with long-standing work on high-consequence viruses and medical countermeasures.</p></div>
          </article>
        </div>
      </section>"""


def programme_page(prefix: str) -> str:
    return f"""
      {page_hero(prefix, "Scientific programme", "Focused sessions for the full research-to-care pathway.", "The programme connects viral ecology, evolution, host biology, clinical care, diagnostics, vaccines and therapeutics.", "ui/society-archive-2.png", [("Registration", local(prefix, "ich2026/abstracts-registration/"), "button-primary")])}
      <section class="section program">
        <div class="section-shell">
          <div class="program-grid">
            <article class="program-track reveal"><p class="track-date">November 2-4</p><h3>International Hantavirus Conference</h3><ul><li>Viral epidemiology, evolution and genetics</li><li>Virus ecology and climate change</li><li>Viral replication and host interaction</li><li>Pathogenesis, diagnostics and clinical care</li><li>Vaccines and therapeutics</li></ul></article>
            <article class="program-track highlight reveal"><p class="track-date">November 5</p><h3>Specialized Andes Virus Workshop</h3><ul><li>Translation of vaccine and therapeutic candidates</li><li>Early diagnosis and exposed-person management</li><li>Regional surveillance and response network</li><li>Round table with scientific and health authorities</li></ul><p class="track-note">Simultaneous English-Spanish interpretation planned.</p></article>
          </div>
        </div>
      </section>"""


def registration_page(prefix: str) -> str:
    return f"""
      {page_hero(prefix, "Abstracts & registration", "Registration and abstract submission.", "The original site notes that abstract submission opens in May 2026, with early bird registration planned for May-July.", "venue/puerto-varas-waterfront.jpg", [("Conference form", CONFERENCE_FORM, "button-primary"), ("Contact", local(prefix, "contact/"), "button-secondary")])}
      <section class="section intro-band">
        <div class="section-shell registration-grid">
          <article class="registration-item reveal"><span>Abstract submission</span><strong>Opening May 2026</strong><a class="text-link" href="{CONFERENCE_FORM}" target="_blank" rel="noreferrer">Submission form</a></article>
          <article class="registration-item reveal"><span>Early bird registration</span><strong>May-July</strong><a class="text-link" href="{CONFERENCE_FORM}" target="_blank" rel="noreferrer">Registration link</a></article>
          <article class="registration-item reveal"><span>Standard registration</span><strong>August-October</strong><a class="text-link" href="{CONFERENCE_FORM}" target="_blank" rel="noreferrer">Registration link</a></article>
        </div>
      </section>"""


def venue_page(prefix: str) -> str:
    links = "".join(f'<a href="{href}" target="_blank" rel="noreferrer">{escape(label)}</a>' for label, href in TRAVEL_LINKS)
    return f"""
      {page_hero(prefix, "Venue & travel", "Hotel Bellavista, Puerto Varas.", "The conference venue faces Lake Llanquihue with access through Santiago and Puerto Montt.", "venue/hotel-bellavista.jpg", [("Open map", "https://goo.gl/maps/dv2jUC4hSGLvr2Ld9", "button-primary"), ("Hotel Bellavista", "https://hotelbellavista.cl/reuniones-y-eventos-corporativos-2/", "button-secondary")])}
      <section class="section venue">
        <div class="section-shell venue-layout">
          <div class="venue-copy reveal"><p class="eyebrow">Travel route</p><h2>International arrival, domestic connection, local transfer.</h2><div class="travel-steps"><div><span>01</span>International arrival at Santiago (SCL)</div><div><span>02</span>Domestic flight to Puerto Montt (PMC)</div><div><span>03</span>Transfer to Puerto Varas, 25-30 minutes by road</div></div></div>
          <figure class="venue-image reveal"><img src="{img(prefix, "venue/puerto-varas-waterfront.jpg")}" alt="Puerto Varas waterfront" loading="lazy" decoding="async"><figcaption>Puerto Varas and Lake Llanquihue</figcaption></figure>
        </div>
      </section>
      <section class="section data-section">
        <div class="section-shell"><div class="section-heading compact reveal"><p class="eyebrow">Travel links</p><h2>All travel hyperlinks from the original venue page.</h2></div><div class="link-list reveal">{links}</div></div>
      </section>"""


def sponsors_page(prefix: str) -> str:
    cards = "".join(
        f'<a class="sponsor reveal" href="{href}" target="_blank" rel="noreferrer"><img src="{img(prefix, image)}" alt="{escape(name)}" loading="lazy" decoding="async"><span>{escape(name)}</span></a>'
        for name, href, image in SPONSORS
    )
    return f"""
      {page_hero(prefix, "Partners & sponsors", "Institutional support across Chilean science and public research.", "ICH2026 is supported by Chilean scientific societies, universities and public research agencies.", "ui/society-archive-1.png")}
      <section class="section sponsors"><div class="section-shell"><div class="sponsor-grid" role="list">{cards}</div></div></section>"""


def contact_page(prefix: str) -> str:
    return f"""
      {page_hero(prefix, "Contact", "Reach the ICH2026 organizing team.", "Use the conference email or forms for registration, abstract submission and membership requests.", "venue/conference-landscape.png", [("Email ICH2026", "mailto:ICH2026@hantavirussociety.org", "button-primary"), ("Conference form", CONFERENCE_FORM, "button-secondary")])}
      <section class="section contact">
        <div class="section-shell contact-layout">
          <div class="section-heading reveal"><p class="eyebrow">Organizers</p><h2>ICH2026@hantavirussociety.org</h2></div>
          <div class="contact-actions reveal"><a class="contact-email" href="mailto:ICH2026@hantavirussociety.org">ICH2026@hantavirussociety.org</a><a class="button button-primary" href="{CONFERENCE_FORM}" target="_blank" rel="noreferrer">Conference form</a><a class="button button-secondary" href="{MEMBERSHIP_FORM}" target="_blank" rel="noreferrer">Apply for ISH membership</a></div>
        </div>
      </section>"""


PAGES = [
    ("index.html", "about", "International Society for Hantaviruses", "International Society for Hantaviruses and ICH2026 in Puerto Varas, Chile.", home_page),
    ("about-ish/index.html", "about", "About ISH | International Society for Hantaviruses", "About the International Society for Hantaviruses.", home_page),
    ("ich2026/index.html", "ich2026", "ICH2026 | International Society for Hantaviruses", "International Conference on Hantaviruses 2026 in Puerto Varas, Chile.", ich2026_page),
    ("ich2026/keynote-speakers/index.html", "keynote", "Keynote Speakers | ICH2026", "Keynote speakers for ICH2026.", keynote_page),
    ("ich2026/programme/index.html", "programme", "Programme | ICH2026", "Scientific programme for ICH2026.", programme_page),
    ("ich2026/abstracts-registration/index.html", "registration", "Abstracts & Registration | ICH2026", "Abstract submission and registration for ICH2026.", registration_page),
    ("ich2026/venue/index.html", "venue", "Venue | ICH2026", "Venue and travel information for ICH2026.", venue_page),
    ("ich2026/partners-sponsors/index.html", "sponsors", "Partners & Sponsors | ICH2026", "Partners and sponsors for ICH2026.", sponsors_page),
    ("contact/index.html", "contact", "Contact | ICH2026", "Contact the ICH2026 organizing team.", contact_page),
]


def main() -> None:
    for out_path, active, title, description, builder in PAGES:
        prefix = prefix_for(out_path)
        html = doc(out_path, active, title, description, builder(prefix))
        target = ROOT / out_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print(out_path)


if __name__ == "__main__":
    main()
