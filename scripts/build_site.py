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

NAV_GROUPS = [
    ("Society", [("about", "About ISH", "about-ish/"), ("contact", "Contact", "contact/")]),
    (
        "Conference",
        [
            ("ich2026", "ICH2026", "ich2026/"),
            ("keynote", "Keynotes", "ich2026/keynote-speakers/"),
            ("programme", "Programme", "ich2026/programme/"),
            ("registration", "Registration", "ich2026/abstracts-registration/"),
            ("venue", "Venue", "ich2026/venue/"),
            ("sponsors", "Sponsors", "ich2026/partners-sponsors/"),
        ],
    ),
]

ICH_NAV_KEYS = {"ich2026", "keynote", "programme", "registration", "venue", "sponsors"}

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

SCIENTIFIC_COMMITTEE = [
    ("Nicole Tischler", "President ISH", "Fundacion Ciencia & Vida / Universidad San Sebastian", "Chile", "ich2026/scientific-nicole-tischler.jpg", "https://orcid.org/0000-0002-4578-4780"),
    ("Piet Maes", "President Elect ISH", "Universite libre de Bruxelles", "Belgium", "ich2026/scientific-piet-maes.jpg", "https://orcid.org/0000-0002-4571-5232"),
    ("Colleen B. Jonsson", "Secretary ISH", "University of Tennessee Health Science Center", "USA", "ich2026/scientific-colleen-jonsson.jpg", "https://orcid.org/0000-0002-2640-7672"),
    ("Jin Won Song", "Past-President ISH", "Korea University College of Medicine", "Korea", "ich2026/scientific-jin-won-song.jpg", "https://orcid.org/0000-0003-0796-8332"),
    ("Satoru Arai", "Scientific Committee", "National Institute of Infectious Diseases / Japan Institute for Health Security", "Japan", "ich2026/scientific-satoru-arai.jpg", "https://orcid.org/0000-0001-5865-0717"),
    ("Steven Bradfute", "Scientific Committee", "Center for Global Health, University of New Mexico", "USA", "ich2026/scientific-steven-bradfute.jpg", "https://orcid.org/0000-0002-1985-751X"),
    ("Roger Hewson", "Scientific Committee", "UK Health Security Agency / London School of Hygiene & Tropical Medicine", "UK", "ich2026/scientific-roger-hewson.jpg", "https://orcid.org/0000-0003-2273-3152"),
    ("Boris Klempa", "Scientific Committee", "Biomedical Research Center, Slovak Academy of Sciences", "Slovakia", "ich2026/scientific-boris-klempa.jpg", "https://orcid.org/0000-0002-6931-1224"),
    ("Jonas Klingstrom", "Scientific Committee", "Linkoping University", "Sweden", "ich2026/scientific-jonas-klingstrom.jpg", "https://orcid.org/0000-0001-9076-1441"),
    ("Valeria Martinez", "Scientific Committee", "INEI / ANLIS Dr. C. G. Malbran", "Argentina", "ich2026/scientific-valeria-martinez.jpg", "https://orcid.org/0000-0002-4356-8136"),
    ("Gustavo Palacios", "Scientific Committee", "Icahn School of Medicine at Mount Sinai", "USA", "ich2026/scientific-gustavo-palacios.jpg", "https://orcid.org/0000-0001-5062-1938"),
]

LOCAL_COMMITTEE = [
    ("Jenniffer Angulo", "Local Organizing Committee", "Pontificia Universidad Catolica de Chile", "", "ich2026/local-jenniffer-angulo.jpg", "https://orcid.org/0000-0002-0471-4751"),
    ("Maria Ines Barria", "Local Organizing Committee", "Universidad San Sebastian", "Puerto Montt", "ich2026/local-maria-ines-barria.jpg", "https://orcid.org/0000-0001-6225-5971"),
    ("Mario Calvo", "Local Organizing Committee", "Universidad Austral de Chile", "Valdivia", "ich2026/local-mario-calvo.jpg", "https://orcid.org/0000-0002-1796-2236"),
    ("Marcela Ferres", "Local Organizing Committee", "Pontificia Universidad Catolica de Chile", "", "ich2026/local-marcela-ferres.jpg", "https://orcid.org/0000-0001-9415-4657"),
    ("Juan Hormazabal", "Local Organizing Committee", "Universidad del Desarrollo", "", "ich2026/local-juan-hormazabal.jpg", "https://orcid.org/0000-0003-0726-2778"),
    ("Nicole Le Corre", "Local Organizing Committee", "Pontificia Universidad Catolica de Chile", "", "ich2026/local-nicole-le-corre.jpg", "https://orcid.org/0000-0002-9361-4049"),
    ("Constanza Martinez-Valdevenito", "Local Organizing Committee", "Pontificia Universidad Catolica de Chile", "", "ich2026/local-constanza-martinez-valdevenito.jpg", "https://orcid.org/0000-0002-2836-9817"),
    ("Nicole Tischler", "Local Organizing Committee", "Fundacion Ciencia & Vida / Universidad San Sebastian", "", "ich2026/scientific-nicole-tischler.jpg", "https://orcid.org/0000-0002-4578-4780"),
    ("Fernando Torres-Perez", "Local Organizing Committee", "Pontificia Universidad Catolica de Valparaiso", "", "ich2026/local-fernando-torres-perez.jpg", "https://orcid.org/0000-0001-8655-7288"),
    ("Cecilia Vial", "Local Organizing Committee", "Universidad del Desarrollo", "", "ich2026/local-cecilia-vial.jpg", "https://orcid.org/0000-0002-0399-6144"),
    ("Pablo Vial", "Local Organizing Committee", "Universidad del Desarrollo", "", "ich2026/local-pablo-vial.jpg", "https://orcid.org/0000-0002-4135-0416"),
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
    nav_groups = []
    for group_label, links in NAV_GROUPS:
        items = []
        for key, label, href in links:
            current = ' aria-current="page"' if key == active else ""
            items.append(f'<a href="{local(prefix, href)}" data-nav="{key}"{current}>{escape(label)}</a>')
        nav_groups.append(
            f'<div class="nav-group" data-nav-group="{escape(group_label.lower())}"><span>{escape(group_label)}</span><div>{"".join(items)}</div></div>'
        )
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
        {"".join(nav_groups)}
      </nav>
    </header>"""


def ich_subnav(prefix: str, active: str) -> str:
    links = []
    for key, label, href in NAV:
        if key not in ICH_NAV_KEYS:
            continue
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{local(prefix, href)}" data-nav="{key}"{current}>{escape(label)}</a>')
    return f"""
      <nav class="subnav-strip" aria-label="ICH2026 section navigation">
        <span>ICH2026</span>
        <div>{"".join(links)}</div>
      </nav>"""


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
        <a href="mailto:ICH2026@hantavirussociety.org">Contact ICH2026</a>
      </nav>
    </footer>"""


def doc(out_path: str, active: str, title: str, description: str, body: str) -> str:
    prefix = prefix_for(out_path)
    subnav = ich_subnav(prefix, active) if active in ICH_NAV_KEYS else ""
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
    <div class="menu-backdrop" data-menu-backdrop hidden></div>
{subnav}
    <main id="top">
{body}
    </main>
{footer(prefix)}
    <script src="{prefix}script.js" defer></script>
  </body>
</html>
"""


def home_page(
    prefix: str,
    hero_image: str = "ui/home-science-hero.webp?v=sober-20260515",
    hero_alt: str = "Scientist examining microscopy data in a virology laboratory",
) -> str:
    return f"""
      <section class="hero" aria-labelledby="hero-title">
        <picture class="hero-media">
          <img src="{img(prefix, hero_image)}" alt="{escape(hero_alt)}" fetchpriority="high">
        </picture>
        <div class="hero-overlay"></div>
        <div class="hero-content reveal is-visible">
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
        <div class="section-shell society-gallery single-image" aria-label="ISH visual archive">
          <figure class="reveal">
            <img src="{img(prefix, "ui/society-archive-2.png")}" alt="ICH2023 Seoul meeting participants" loading="lazy" decoding="async">
            <figcaption>ICH2023 Seoul | Republic of Korea</figcaption>
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
      <section class="section research-domains">
        <div class="section-shell research-domain-layout">
          <div class="section-heading reveal">
            <p class="eyebrow">Scientific domains</p>
            <h2>From field ecology to clinical preparedness.</h2>
          </div>
          <div class="domain-list reveal" aria-label="Hantavirus research domains">
            <span>Reservoir ecology</span>
            <span>Viral evolution</span>
            <span>Host response</span>
            <span>Diagnostics</span>
            <span>Clinical care</span>
            <span>Vaccines</span>
            <span>Therapeutics</span>
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


def committee_grid(prefix: str, people: list[tuple[str, str, str, str, str, str]]) -> str:
    cards = []
    for name, role, affiliation, location, image, href in people:
        location_html = f"<span>{escape(location)}</span>" if location else ""
        cards.append(
            f"""
            <article class="committee-person reveal" role="listitem">
              <img src="{img(prefix, image)}" alt="{escape(name)}" loading="lazy" decoding="async">
              <div>
                <h3><a href="{href}" target="_blank" rel="noreferrer">{escape(name)}</a></h3>
                <p>{escape(role)}</p>
                <span>{escape(affiliation)}</span>
                {location_html}
              </div>
            </article>"""
        )
    return f'<div class="committee-people-grid" role="list">{"".join(cards)}</div>'


def ich2026_page(prefix: str) -> str:
    scientific_people = committee_grid(prefix, SCIENTIFIC_COMMITTEE)
    local_people = committee_grid(prefix, LOCAL_COMMITTEE)
    return f"""
      <section class="ich-hero" aria-labelledby="ich-title">
        <img class="ich-hero-bg" src="{img(prefix, "ich2026/conference-volcano.jpg")}" alt="Osorno Volcano and Petrohue waterfalls near Puerto Varas" fetchpriority="high">
        <div class="ich-hero-overlay"></div>
        <div class="ich-hero-copy reveal is-visible">
          <p class="eyebrow">International Conference on Hantaviruses</p>
          <h1 id="ich-title">Puerto Varas | Chile</h1>
          <p class="hero-lede">November 2-5 2026</p>
          <div class="ich-hero-meta" aria-label="Conference details">
            <span>Venue & Location</span>
            <strong>Hotel Bellavista, Lake District</strong>
            <span>Specialized workshop</span>
            <strong>Andes Virus, November 5</strong>
          </div>
          <div class="hero-actions page-actions">
            <a class="button button-primary" href="{local(prefix, "ich2026/abstracts-registration/")}">Abstracts & registration</a>
            <a class="button button-secondary" href="{local(prefix, "ich2026/programme/")}">Scientific programme</a>
            <a class="button button-secondary" href="{local(prefix, "ich2026/venue/")}">Venue</a>
          </div>
        </div>
      </section>
      <section class="conference-summary" aria-label="ICH2026 quick facts">
        <div class="summary-item"><span>Dates</span><strong>November 2-5, 2026</strong></div>
        <div class="summary-item"><span>City</span><strong>Puerto Varas, Chile</strong></div>
        <div class="summary-item"><span>Venue</span><strong>Hotel Bellavista</strong></div>
        <div class="summary-item"><span>Focus</span><strong>Hantavirus science and Andes Virus workshop</strong></div>
      </section>
      <section class="section intro-band">
        <div class="section-shell ich-story">
          <div class="section-heading reveal">
            <p class="eyebrow">Venue & Location</p>
            <h2>Puerto Varas, located in the scenic Lake District in Southern Chile.</h2>
          </div>
          <div class="prose reveal">
            <p>The 2026 meeting of the International Society for Hantaviruses will take place in Puerto Varas, located in the scenic Lake District in Southern Chile widely regarded as a gateway to Patagonia. The city sits at the foot of the iconic Osorno Volcano in southern Chile, providing a spectacular natural setting for scientific exchange and collaboration.</p>
            <p>The conference will bring together scientists and health professionals from around the world to share and discuss the latest advances across a broad range of topics, including viral epidemiology, ecology, virus-host interactions, pathogenesis, clinical aspects of disease, and the development of vaccines and therapeutics.</p>
          </div>
          <figure class="ich-story-figure reveal">
            <img src="{img(prefix, "venue/puerto-varas-waterfront.jpg")}" alt="Puerto Varas waterfront and Lake Llanquihue" loading="lazy" decoding="async">
            <figcaption>Puerto Varas, Lake Llanquihue and the Chilean Lake District.</figcaption>
          </figure>
        </div>
      </section>
      <section class="section conference-path-section">
        <div class="section-shell">
          <div class="section-heading compact reveal">
            <p class="eyebrow">Conference path</p>
            <h2>Move through ICH2026 by decision point.</h2>
          </div>
          <div class="conference-path" role="list">
            <a class="path-step reveal" role="listitem" href="{local(prefix, "ich2026/venue/")}"><span>01</span><strong>Plan travel</strong><small>Venue, airports, local transfers and Puerto Varas context.</small></a>
            <a class="path-step reveal" role="listitem" href="{local(prefix, "ich2026/programme/")}"><span>02</span><strong>Choose sessions</strong><small>Scientific themes, main meeting and Andes Virus workshop.</small></a>
            <a class="path-step reveal" role="listitem" href="{local(prefix, "ich2026/abstracts-registration/")}"><span>03</span><strong>Submit and register</strong><small>Abstract submission, early bird timing and conference form.</small></a>
            <a class="path-step reveal" role="listitem" href="{local(prefix, "ich2026/partners-sponsors/")}"><span>04</span><strong>Review partners</strong><small>Institutional support and scientific host network.</small></a>
          </div>
        </div>
      </section>
      <section class="section data-section">
        <div class="section-shell">
          <div class="section-heading compact reveal">
            <p class="eyebrow">Scientific Program & Keynote Speakers</p>
            <h2>An excellent platform for students, postdoctoral researchers, and established scientists.</h2>
            <p>The International Conference on Hantaviruses will provide an excellent platform for students, postdoctoral researchers, and established scientists to present their latest findings and engage with the international hantavirus research community. In addition, the organizing committee has invited leading experts in the field to deliver keynote lectures highlighting cutting-edge developments in hantavirus research.</p>
          </div>
          <div class="ich-feature-grid">
            <article class="ich-feature reveal">
              <img src="{img(prefix, "ich2026/hantavirus-em.jpg")}" alt="Hantavirus particles under electron microscopy" loading="lazy" decoding="async">
              <div>
                <span>01</span>
                <h3>Scientific Program</h3>
                <p>Sessions span viral epidemiology, ecology, virus-host interaction, pathogenesis, clinical aspects, vaccines and therapeutics.</p>
                <a class="text-link" href="{local(prefix, "ich2026/programme/")}">View programme</a>
              </div>
            </article>
            <article class="ich-feature reveal">
              <img src="{img(prefix, "ich2026/rodent-reservoir.jpg")}" alt="Rodent reservoir associated with hantavirus ecology" loading="lazy" decoding="async">
              <div>
                <span>02</span>
                <h3>Keynote Speakers</h3>
                <p>Invited experts highlight current developments across hantavirus research, clinical science and medical countermeasures.</p>
                <a class="text-link" href="{local(prefix, "ich2026/keynote-speakers/")}">See speakers</a>
              </div>
            </article>
            <article class="ich-feature reveal">
              <img src="{img(prefix, "venue/conference-landscape.png")}" alt="Conference landscape in Southern Chile" loading="lazy" decoding="async">
              <div>
                <span>03</span>
                <h3>Abstract Submission & Registration</h3>
                <p>Submission and registration are handled through the conference form, with early registration timing listed on the registration page.</p>
                <a class="text-link" href="{local(prefix, "ich2026/abstracts-registration/")}">Registration details</a>
              </div>
            </article>
            <article class="ich-feature reveal">
              <img src="{img(prefix, "ich2026/conference-volcano.jpg")}" alt="Osorno Volcano and Petrohue waterfalls" loading="lazy" decoding="async">
              <div>
                <span>04</span>
                <h3>Andes Virus Workshop</h3>
                <p>A focused day on regional evidence, clinical care, early diagnosis and public health response.</p>
                <a class="text-link" href="{local(prefix, "ich2026/programme/")}">Workshop details</a>
              </div>
            </article>
          </div>
        </div>
      </section>
      <section class="section ich-workshop">
        <div class="section-shell ich-workshop-layout">
          <div class="section-heading reveal">
            <p class="eyebrow">Specialized Workshop: Andes Virus</p>
            <h2>A one-day workshop dedicated to Andes virus.</h2>
          </div>
          <div class="prose reveal">
            <p>In addition to the traditional ICH scientific program, the conference will feature on November 5 a one-day workshop dedicated to Andes virus, a pathogen of particular regional importance. This workshop will provide an opportunity for researchers, clinicians, and public health professionals to discuss the local epidemiology, clinical management, and public health response to hantavirus cardiopulmonary syndrome.</p>
            <p>Local authorities and decision-makers will also be invited to participate, fostering dialogue between the scientific community and public health stakeholders.</p>
            <a class="button button-primary" href="{local(prefix, "ich2026/programme/")}">Workshop programme</a>
          </div>
        </div>
      </section>
      <section class="section committees">
        <div class="section-shell">
          <div class="section-heading compact reveal">
            <p class="eyebrow">Organizing Committees</p>
            <h2>Scientific and local teams from the original ICH2026 page.</h2>
          </div>
          <div class="committee-tabs reveal" role="group" aria-label="Filter committees">
            <button type="button" class="is-active" data-committee-filter="all">All</button>
            <button type="button" data-committee-filter="scientific">Scientific</button>
            <button type="button" data-committee-filter="local">Local</button>
          </div>
          <div class="committee-section" data-committee-section="scientific">
            <div class="committee-label reveal">
              <span>Scientific Committee</span>
              <p>International scientific direction for the conference programme.</p>
            </div>
            {scientific_people}
          </div>
          <div class="committee-section" data-committee-section="local">
            <div class="committee-label reveal">
              <span>Local Organizing Committee</span>
              <p>Chilean host institutions coordinating the Puerto Varas meeting.</p>
            </div>
            {local_people}
          </div>
          <div class="partners-link reveal">
            <a class="button button-primary" href="{local(prefix, "ich2026/partners-sponsors/")}">ICH2026 Partners & Sponsors</a>
          </div>
        </div>
      </section>"""


def keynote_page(prefix: str) -> str:
    return f"""
      {page_hero(prefix, "Keynote speakers", "ICH2026 Keynote Speakers", "Invited speakers for the International Conference on Hantaviruses.", "venue/conference-landscape.png")}
      <section class="section speakers">
        <div class="section-shell speaker-grid">
          <article class="speaker reveal">
            <img src="{img(prefix, "speakers/marcela-ferres.png")}" alt="Dr. Marcela Ferres" loading="lazy" decoding="async">
            <div>
              <h2>Dr. Marcela Ferres</h2>
              <p class="speaker-meta">Pontificia Universidad Catolica, Chile</p>
              <p>Dr. Marcela Ferres is a professor, pediatric infectious diseases specialist, and director of the Infectious Diseases and Molecular Virology Laboratory at the Faculty of Medicine, Universidad Catolica de Chile, and Red de Salud UC CHRISTUS, Santiago, Chile. She has more than 29 years of experience in clinical hantavirus research, working closely with Dr. Pablo Vial's group at Universidad del Desarrollo.</p>
              <p>Her research focuses on the epidemiological, cellular, and molecular factors involved in person-to-person transmission of Andes virus. She has contributed to landmark studies identifying key transmission risks and advancing early diagnostic methods, including RT-PCR. Her work has also explored viral presence in different body fluids, highlighting potential transmission routes such as saliva and maternal milk.</p>
              <p>More recently, her team successfully isolated a new Andes virus strain from a household contact during the incubation period. Dr. Ferres has authored more than 30 peer-reviewed publications in hantavirus, SARS-CoV-2, and diagnostic virology, and is the author of a Clinical Virology book, currently preparing its third edition.</p>
              <a class="text-link" href="https://orcid.org/0000-0001-9415-4657" target="_blank" rel="noreferrer">ORCID profile</a>
            </div>
          </article>
          <article class="speaker reveal">
            <img src="{img(prefix, "speakers/jay-hooper.png")}" alt="Dr. Jay Hooper" loading="lazy" decoding="async">
            <div>
              <h2>Dr. Jay Hooper</h2>
              <p class="speaker-meta">United States Army Medical Research Institute of Infectious Diseases (USAMRIID), USA</p>
              <p>Dr. Jay Hooper is the Chief of the Molecular Virology Branch at USAMRIID. He has more than 30 years of research experience working with lethal viruses, mostly in Biosafety Level 3 and BSL-4 high-containment. His research is aimed at the discovery and development of medical countermeasures targeting high consequence viral diseases of military importance, including hemorrhagic fever and diseases caused by poxviruses.</p>
              <p>Dr. Hooper received a B.A. in Biology from Colby College in 1986 and a Ph.D. in Virology from Harvard University in 1995. His research has resulted in more than 100 peer-reviewed publications and 15 patents.</p>
            </div>
          </article>
        </div>
      </section>"""


def programme_page(prefix: str) -> str:
    return f"""
      {page_hero(prefix, "ICH2026 Program", "International Hantavirus Conference", "November 2-4, followed by the Andes Virus Workshop on November 5.", "ui/society-archive-2.png", [("Registration", local(prefix, "ich2026/abstracts-registration/"), "button-primary")])}
      <section class="section program">
        <div class="section-shell">
          <div class="program-grid program-support">
            <article class="program-track reveal"><p class="track-date">November 2-4</p><h3>International Hantavirus Conference</h3><p>The meeting will cover the following topics:</p><ul><li>Viral epidemiology, evolution &amp; genetics</li><li>Virus ecology and climate change</li><li>Viral replication</li><li>Virus-host interactions</li><li>Pathogenesis</li><li>Vaccines &amp; therapeutics</li><li>Clinical aspects &amp; diagnostics</li></ul></article>
            <article class="program-track highlight reveal"><p class="track-date">November 5</p><h3>Andes Virus Workshop</h3><p>Topics will cover the following aspects:</p><ul><li>Translation of vaccine &amp; therapeutics candidates</li><li>Early diagnosis</li><li>Management of Andes virus-exposed persons</li><li>Surveillance of Andes virus</li><li>Regional Network</li><li>Other topics</li><li>Round Table discussion</li></ul><p class="track-note">This workshop will count with simultaneous translation (English-Spanish; Spanish-English).</p></article>
          </div>
        </div>
      </section>"""


def registration_page(prefix: str) -> str:
    return f"""
      {page_hero(prefix, "ICH2026 Registration & Abstract Submission", "Registration and abstract submission.", "Abstract submission opens in May 2026, with early bird registration planned for May-July.", "venue/puerto-varas-waterfront.jpg", [("Conference form", CONFERENCE_FORM, "button-primary"), ("Contact", local(prefix, "contact/"), "button-secondary")])}
      <section class="section intro-band">
        <div class="section-shell registration-flow-layout">
          <div class="section-heading reveal"><p class="eyebrow">Registration flow</p><h2>ICH2026 Registration & Abstract Submission</h2><p>Comming soon ...</p><p>We apologize for the delay. Our team is currently supporting the cruise ship emergency.</p></div>
          <div class="registration-flow">
            <article class="registration-item reveal"><span>Abstract Submission</span><strong>Opening May 2026</strong><a class="text-link" href="{CONFERENCE_FORM}" target="_blank" rel="noreferrer">Link</a></article>
            <article class="registration-item reveal"><span>Early Bird Registration</span><strong>May - July</strong><a class="text-link" href="{CONFERENCE_FORM}" target="_blank" rel="noreferrer">Link</a></article>
            <article class="registration-item reveal"><span>Standar Registration</span><strong>August - October</strong><a class="text-link" href="{CONFERENCE_FORM}" target="_blank" rel="noreferrer">Link</a></article>
          </div>
        </div>
      </section>"""


def venue_page(prefix: str) -> str:
    links = "".join(f'<a href="{href}" target="_blank" rel="noreferrer">{escape(label)}</a>' for label, href in TRAVEL_LINKS)
    return f"""
      {page_hero(prefix, "ICH2026 Venue & Travel", "Hotel Bellavista, Puerto Varas.", "The 2026 meeting will take place in Hotel Bellavista, Puerto Varas.", "venue/hotel-bellavista.jpg", [("Open map", "https://goo.gl/maps/dv2jUC4hSGLvr2Ld9", "button-primary"), ("Hotel Bellavista", "https://hotelbellavista.cl/reuniones-y-eventos-corporativos-2/", "button-secondary")])}
      <section class="section venue">
        <div class="section-shell venue-layout">
          <div class="venue-copy reveal">
            <p class="eyebrow">How to get to Puerto Varas</p>
            <h2>International arrival, domestic flight and local transfer.</h2>
            <div class="travel-steps">
              <div><span>01</span>International arrival - Santiago (SCL)</div>
              <div><span>02</span>Domestic flight - Santiago to Puerto Montt (PMC)</div>
              <div><span>03</span>Transfer - Puerto Montt Airport to Puerto Varas</div>
            </div>
          </div>
          <figure class="venue-image reveal"><img src="{img(prefix, "venue/puerto-varas-waterfront.jpg")}" alt="Puerto Varas waterfront" loading="lazy" decoding="async"><figcaption>Puerto Varas and Lake Llanquihue</figcaption></figure>
        </div>
      </section>
      <section class="section intro-band">
        <div class="section-shell travel-detail-list">
          <article class="reveal">
            <p class="eyebrow">Step 1</p>
            <h2>International Arrival - Santiago (SCL)</h2>
            <p>Most international travelers will arrive at Arturo Merino Benitez International Airport (SCL) in Santiago, Chile.</p>
            <ul><li>Proceed through immigration and customs</li><li>Collect your luggage</li><li>Follow signs for domestic connections</li></ul>
            <p><strong>Tip:</strong> Allow at least 2-3 hours for connection time, especially if arriving from long-haul international flights.</p>
            <p>Alternatively, you may prefer to make a stop-over in Santiago. There are several hotels near the airport. Also, it is possible to book day trips to diverse destinations, close to, or in Santiago.</p>
          </article>
          <article class="reveal">
            <p class="eyebrow">Step 2</p>
            <h2>Domestic Flight - Santiago to Puerto Montt (PMC)</h2>
            <p>From Santiago, take a domestic flight to El Tepual Airport (PMC) in Puerto Montt.</p>
            <ul><li>Flight duration: approximately 1 hour 40 minutes</li><li>Airlines operate multiple daily flights</li></ul>
            <p><strong>Tip:</strong> Puerto Montt is the main gateway to the Los Lagos region and Puerto Varas.</p>
          </article>
          <article class="reveal">
            <p class="eyebrow">Step 3</p>
            <h2>Transfer - Puerto Montt Airport to Puerto Varas</h2>
            <p>Puerto Varas is located approximately 20-30 km from the airport, with a travel time of about 25-30 minutes depending on traffic.</p>
            <h3>Private or Shared Transfer</h3>
            <ul><li>Pre-booked or available at the airport</li><li>Drop-off directly at your hotel</li><li>Travel time: ~30 minutes</li><li>Approximate amount: 15-25 USD</li></ul>
            <h3>Taxi</h3>
            <ul><li>Available directly outside the terminal</li><li>Travel time: ~25-30 minutes</li><li>Safe and widely used</li><li>Estimated cost: 20-30 USD</li></ul>
            <h3>Bus / Shuttle</h3>
            <ul><li>Budget-friendly option</li><li>Travel time: ~30-40 minutes depending on route</li><li>Estimated cost: 2 USD</li><li>Departures from Puerto Montt bus terminal</li></ul>
            <p>Taxis and transfers are the most convenient options for international travelers.</p>
          </article>
          <article class="reveal">
            <p class="eyebrow">Final destination</p>
            <h2>Puerto Varas</h2>
            <p>Puerto Varas is a scenic lakeside city located in southern Chile, known for Lake Llanquihue, Osorno Volcano, and easy access to national parks and research sites.</p>
            <h3>Travel Tips</h3>
            <ul><li>Currency: Chilean Peso (CLP)</li><li>Most taxis and services accept cards, but carrying some cash is recommended</li><li>Weather can change quickly - bring appropriate clothing</li><li>Spanish is the local language, but basic English is commonly understood in tourism services</li></ul>
          </article>
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
      {page_hero(prefix, "Contact", "CONTACT ICH2026 Organizers", "ICH2026@hantavirussociety.org", "venue/conference-landscape.png", [("Email ICH2026", "mailto:ICH2026@hantavirussociety.org", "button-primary")])}
      <section class="section contact">
        <div class="section-shell contact-layout">
          <div class="section-heading reveal"><p class="eyebrow">Contact</p><h2>CONTACT ICH2026 Organizers</h2></div>
          <div class="contact-actions reveal"><a class="contact-email" href="mailto:ICH2026@hantavirussociety.org">ICH2026@hantavirussociety.org</a></div>
        </div>
      </section>"""


def about_page(prefix: str) -> str:
    return f"""
      {page_hero(prefix, "About ISH", "About the International Society for Hantaviruses", "Founded in 1989 with its first Meeting in Seoul (Korea).", "venue/puerto-varas-hero.jpg", [("Apply for ISH Membership", MEMBERSHIP_FORM, "button-primary")])}
      <section class="section intro-band">
        <div class="section-shell two-column">
          <div class="section-heading reveal">
            <p class="eyebrow">About ISH</p>
            <h2>About the International Society for Hantaviruses</h2>
          </div>
          <div class="prose reveal">
            <p>This society was founded in 1989 with its first Meeting in Seoul (Korea), to promote the advancement and promulgation of knowledge on hantaviruses and the diseases they cause. It also fosters collaboration and the exchange of expertise in all areas of knowledge, including viral epidemiology and ecology, viral replication, host interactions, pathogenesis, advances in vaccine and therapeutics, diagnostics and clinical management.</p>
            <p>The society is led by an International Advisory Board composed of members from countries most affected by hantaviruses, reflecting its global scope and commitment to addressing regional challenges. Since its establishment, the society has convened a triennial meeting that brings together researchers, clinicians, and public health professionals. The next International Hantavirus Conference (ICH) will be held in November 2026 in Puerto Varas, Chile.</p>
            <a class="button button-primary" href="{MEMBERSHIP_FORM}" target="_blank" rel="noreferrer">Apply for ISH Membership</a>
          </div>
        </div>
        <div class="section-shell society-gallery single-image" aria-label="ICH2023 Seoul">
          <figure class="reveal">
            <img src="{img(prefix, "ui/society-archive-2.png")}" alt="ICH2023 Seoul meeting participants" loading="lazy" decoding="async">
            <figcaption>ICH2023 Seoul | Republic of Korea</figcaption>
          </figure>
        </div>
      </section>
      <section class="section committees">
        <div class="section-shell">
          <div class="section-heading compact reveal">
            <p class="eyebrow">International Advisory Board</p>
            <h2>International Advisory Board</h2>
          </div>
          {advisory_grid(prefix)}
        </div>
      </section>"""


PAGES = [
    ("index.html", "about", "International Society for Hantaviruses", "International Society for Hantaviruses and ICH2026 in Puerto Varas, Chile.", home_page),
    ("about-ish/index.html", "about", "About ISH | International Society for Hantaviruses", "About the International Society for Hantaviruses.", about_page),
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
