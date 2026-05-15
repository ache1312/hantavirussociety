from __future__ import annotations

import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SITE_URL = "https://www.hantavirussociety.org"

OG_IMAGES: dict[str, str] = {
    "home": "ui/home-science-hero.webp",
    "about": "ui/home-science-hero.webp",
    "ich2026": "ich2026/conference-volcano.jpg",
    "keynote": "venue/conference-landscape.png",
    "programme": "ui/society-archive-2.png",
    "registration": "venue/puerto-varas-waterfront.jpg",
    "venue": "venue/hotel-bellavista.jpg",
    "sponsors": "ui/society-archive-1.png",
    "contact": "venue/conference-landscape.png",
}

CONFERENCE_JSON_LD = """{
    "@context": "https://schema.org",
    "@type": "Event",
    "name": "International Conference on Hantaviruses 2026",
    "alternateName": "ICH2026",
    "startDate": "2026-11-02",
    "endDate": "2026-11-05",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "location": {
      "@type": "Place",
      "name": "Hotel Bellavista",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Puerto Varas",
        "addressRegion": "Los Lagos",
        "addressCountry": "CL"
      }
    },
    "organizer": {
      "@type": "Organization",
      "name": "International Society for Hantaviruses",
      "url": "https://www.hantavirussociety.org"
    },
    "url": "https://www.hantavirussociety.org/ich2026",
    "image": "https://www.hantavirussociety.org/assets/images/ich2026/conference-volcano.jpg",
    "description": "International Conference on Hantaviruses 2026 in Puerto Varas, Chile. Covering viral epidemiology, ecology, virus-host interactions, pathogenesis, vaccines and therapeutics."
  }"""


THEME_BOOTSTRAP = """    <script>
      (() => {
        const root = document.documentElement;
        let storedTheme = null;
        try {
          storedTheme = localStorage.getItem("ish-theme");
        } catch {}
        const theme = storedTheme === "dark" || storedTheme === "light" ? storedTheme : "light";
        root.dataset.theme = theme;
        root.style.colorScheme = theme;
      })();
    </script>"""


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
]

NAV_GROUPS = [
    ("Society", [("about", "About ISH", "about-ish/")]),
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
    ("hotel", "Hotel Bellavista", "Conference venue and event facilities.", "https://hotelbellavista.cl/reuniones-y-eventos-corporativos-2/"),
    ("map-pin", "Venue map", "Av. Vicente Perez Rosales #060, Puerto Varas.", "https://goo.gl/maps/dv2jUC4hSGLvr2Ld9"),
    ("plane", "Santiago airport", "International arrival at Arturo Merino Benítez Airport.", "https://thesantiagoairport.com/"),
    ("route", "Santiago day trips", "Optional stop-over ideas near Santiago.", "https://www.tripadvisor.com/Attractions-g294305-Activities-c42-t205-Santiago_Santiago_Metropolitan_Region.html"),
    ("route", "Santiago tours", "Additional tours and day activities in Santiago.", "https://www.viator.com/Santiago/d713?pid=P00095352&mcid=42383&medium=link&campaign=scltours"),
    ("car", "Airport transfer", "Shared or private transfer from Puerto Montt airport.", "https://ww2.trasladoaeropuerto.cl/"),
    ("message", "Transfer WhatsApp", "Direct WhatsApp contact for airport transfer reservations.", "https://api.whatsapp.com/send?phone=56976053701&text=hola,%20lo%20contacto%20desde%20la%20p%C3%A1gina%20web"),
    ("mail", "Transfer email", "reservas@trasladoaeropuerto.cl", "mailto:reservas@trasladoaeropuerto.cl"),
    ("car", "Survip transfer", "Transfer service from Puerto Montt airport to Puerto Varas.", "https://www.survip.cl/transfer-aeropuerto-puerto-montt-a-puerto-varas.php"),
]

TRAVEL_ICONS = {
    "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 17h14l-1.6-5.2A3 3 0 0 0 14.5 10h-5a3 3 0 0 0-2.9 1.8L5 17Z"/><path d="M7 17v2"/><path d="M17 17v2"/><path d="M6.5 14h11"/><circle cx="8" cy="17" r="1"/><circle cx="16" cy="17" r="1"/></svg>',
    "hotel": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v15"/><path d="M16 10h2a2 2 0 0 1 2 2v9"/><path d="M8 8h.01"/><path d="M12 8h.01"/><path d="M8 12h.01"/><path d="M12 12h.01"/><path d="M9 21v-4h3v4"/><path d="M3 21h18"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="16" height="12" rx="2"/><path d="m4 8 8 6 8-6"/></svg>',
    "map-pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-5.2 7-11a7 7 0 1 0-14 0c0 5.8 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    "message": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 18.5 6.2 15A7 7 0 1 1 9 17.4L5 18.5Z"/><path d="M9 10h6"/><path d="M9 13h4"/></svg>',
    "plane": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10.5 20 13 13l7-2.5a1.3 1.3 0 0 0 0-2.5L4 3l3.8 7L4 17l6.5-2.4V20Z"/></svg>',
    "route": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.5 6H14a3 3 0 0 1 0 6h-4a3 3 0 0 0 0 6h5.5"/></svg>',
}


def prefix_for(out_path: str) -> str:
    parent = Path(out_path).parent
    return "" if str(parent) == "." else "../" * len(parent.parts)


def img(prefix: str, asset_path: str) -> str:
    return f"{prefix}assets/images/{asset_path}"


def load_image_manifest() -> dict[str, dict[str, object]]:
    manifest_path = ROOT / "assets" / "images" / "optimized" / "manifest.json"
    if not manifest_path.exists():
        return {}
    return json.loads(manifest_path.read_text(encoding="utf-8"))


IMAGE_MANIFEST = load_image_manifest()


def asset_key(asset_path: str) -> str:
    return asset_path.split("?", 1)[0]


def format_attrs(values: dict[str, object]) -> str:
    parts = []
    for key, value in values.items():
        if value is None or (value == "" and key != "alt"):
            continue
        name = key[:-1] if key.endswith("_") else key
        parts.append(f'{name.replace("_", "-")}="{escape(str(value), quote=True)}"')
    return " ".join(parts)


def optimized_source(prefix: str, asset_path: str, sizes: str) -> str:
    manifest = IMAGE_MANIFEST.get(asset_key(asset_path))
    if not manifest:
        return ""
    variants = sorted(manifest["variants"], key=lambda item: item["width"])  # type: ignore[index]
    srcset = ", ".join(
        f'{prefix}assets/images/{variant["path"]} {variant["width"]}w' for variant in variants
    )
    return f'<source {format_attrs({"type": "image/webp", "srcset": srcset, "sizes": sizes})}>'


def responsive_image(
    prefix: str,
    asset_path: str,
    alt: str,
    *,
    class_name: str = "",
    picture_class: str = "responsive-image",
    loading: str = "",
    decoding: str = "",
    fetchpriority: str = "",
    sizes: str = "100vw",
    aria_hidden: str = "",
) -> str:
    manifest = IMAGE_MANIFEST.get(asset_key(asset_path))
    image_attrs: dict[str, object] = {
        "class": class_name,
        "src": img(prefix, asset_path),
        "alt": alt,
        "loading": loading,
        "decoding": decoding,
        "fetchpriority": fetchpriority,
        "aria_hidden": aria_hidden,
    }
    if manifest:
        image_attrs["width"] = manifest["width"]
        image_attrs["height"] = manifest["height"]
    picture_attrs = format_attrs({"class": picture_class})
    picture_attrs = f" {picture_attrs}" if picture_attrs else ""
    return f'<picture{picture_attrs}>{optimized_source(prefix, asset_path, sizes)}<img {format_attrs(image_attrs)}></picture>'


def local(prefix: str, path: str = "") -> str:
    return f"{prefix}{path}"


def contact_href(prefix: str) -> str:
    return local(prefix, "about-ish/#contact")


def attrs(**values: str) -> str:
    return format_attrs(values)


def travel_icon(name: str) -> str:
    return f'<span class="travel-link-icon" aria-hidden="true">{TRAVEL_ICONS[name]}</span>'


def travel_link_card(icon: str, label: str, description: str, href: str) -> str:
    target = "" if href.startswith("mailto:") else ' target="_blank" rel="noreferrer"'
    return (
        f'<a class="travel-link" href="{escape(href, quote=True)}"{target}>'
        f'{travel_icon(icon)}'
        f'<span class="travel-link-copy"><strong>{escape(label)}</strong><small>{escape(description)}</small></span>'
        "</a>"
    )


def clean_output(content: str) -> str:
    return "\n".join(line.rstrip() for line in content.splitlines()) + "\n"


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
        {responsive_image(prefix, "ui/logo.png", "International Society for Hantaviruses logo", class_name="brand-logo", loading="eager", decoding="async", sizes="65px")}
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
      <button class="theme-toggle" type="button" aria-label="Light mode active. Switch to dark mode." aria-pressed="false" title="Light mode active. Switch to dark mode." data-theme-tooltip="Light mode active. Switch to dark mode." data-theme-toggle>
        <span class="theme-icon theme-icon-sun" aria-hidden="true"></span>
        <span class="theme-icon theme-icon-moon" aria-hidden="true"></span>
        <span class="sr-only" data-theme-label>Light mode active. Switch to dark mode.</span>
      </button>
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
        {responsive_image(prefix, "ui/logo.png", "International Society for Hantaviruses logo", loading="lazy", decoding="async", sizes="120px")}
        <p>Website of the International Society for Hantaviruses.</p>
      </div>
      <nav aria-label="Site pages">
        <strong>Site</strong>
        <a href="{local(prefix, "about-ish/")}">About ISH</a>
        <a href="{local(prefix, "ich2026/")}">ICH2026</a>
        <a href="{local(prefix, "ich2026/abstracts-registration/")}">Registration</a>
        <a href="{contact_href(prefix)}">Contact</a>
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

    page_dir = str(Path(out_path).parent)
    canonical = SITE_URL + "/" if page_dir == "." else f"{SITE_URL}/{page_dir}/"
    og_image = SITE_URL + "/assets/images/" + OG_IMAGES.get(active, "ui/home-science-hero.webp")

    json_ld = ""
    if active in ICH_NAV_KEYS:
        json_ld = f'\n    <script type="application/ld+json">\n    {CONFERENCE_JSON_LD}\n    </script>'

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{escape(description)}">
    <title>{escape(title)}</title>
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{escape(title)}">
    <meta property="og:description" content="{escape(description)}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:site_name" content="International Society for Hantaviruses">
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{escape(title)}">
    <meta name="twitter:description" content="{escape(description)}">
    <meta name="twitter:image" content="{og_image}">
    <!-- Canonical -->
    <link rel="canonical" href="{canonical}">
    <link rel="icon" href="{img(prefix, "ui/logo.png")}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Source+Serif+4:wght@500;600&display=swap" rel="stylesheet">
{THEME_BOOTSTRAP}
    <link rel="stylesheet" href="{prefix}styles.css">{json_ld}
  </head>
  <body data-page="{active}">
    <div class="scroll-progress" aria-hidden="true"></div>
    <a class="skip-link" href="#main-content">Skip to main content</a>
{header(prefix, active)}
    <div class="menu-backdrop" data-menu-backdrop hidden></div>
{subnav}
    <main id="main-content" tabindex="-1">
{body}
    </main>
{footer(prefix)}
    <button class="back-to-top" aria-label="Back to top" title="Back to top">↑</button>
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
        {responsive_image(prefix, hero_image, hero_alt, picture_class="hero-media", fetchpriority="high", sizes="100vw")}
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
        <aside class="hero-panel" aria-label="ICH2026 conference brief">
          <div class="hero-panel-kicker">ICH2026</div>
          <span class="hero-panel-title">International Conference on Hantaviruses</span>
          <strong class="hero-panel-date">Nov 2-5, 2026</strong>
          <div class="hero-panel-meta" aria-label="Conference location and venue">
            <span>Puerto Varas, Chile</span>
            <span>Hotel Bellavista</span>
          </div>
          <div class="countdown" data-countdown="2026-11-02" aria-label="Time until ICH2026">
            <div class="countdown-unit"><span class="countdown-val" data-unit="days">--</span><span class="countdown-label">Days</span></div>
            <div class="countdown-unit"><span class="countdown-val" data-unit="hours">--</span><span class="countdown-label">Hours</span></div>
            <div class="countdown-unit"><span class="countdown-val" data-unit="minutes">--</span><span class="countdown-label">Minutes</span></div>
          </div>
          <a class="hero-panel-link" href="{local(prefix, "ich2026/programme/")}">Programme</a>
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
            {responsive_image(prefix, "ui/society-archive-2.png", "ICH2023 Seoul meeting participants", loading="lazy", decoding="async", sizes="(max-width: 780px) 100vw, 1180px")}
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
            <a class="button button-secondary light" href="{contact_href(prefix)}">Contact ICH2026</a>
          </div>
        </div>
      </section>"""


def advisory_grid(prefix: str) -> str:
    cards = []
    for index, (name, role, image, href) in enumerate(BOARD):
        if "|" in role:
            title, country = [part.strip() for part in role.split("|", 1)]
        else:
            title, country = "International Advisory Board", role
        heading = f'<a href="{href}" target="_blank" rel="noreferrer">{escape(name)}</a>' if href else escape(name)
        officer_class = " advisor-officer" if index < 4 else ""
        cards.append(
            f"""
            <article class="advisor{officer_class} reveal" role="listitem">
              <div class="advisor-photo">{responsive_image(prefix, image, name, loading="lazy", decoding="async", sizes="(max-width: 780px) 104px, 184px")}</div>
              <div class="advisor-copy">
                <span class="advisor-location">{escape(country)}</span>
                <h3>{heading}</h3>
                <p>{escape(title)}</p>
              </div>
            </article>"""
        )
    return f'<div class="advisory-grid" role="list">{"".join(cards)}</div>'


def page_hero(prefix: str, eyebrow: str, title: str, lede: str, image: str, ctas: list[tuple[str, str, str]] | None = None, breadcrumbs: list[tuple[str, str | None]] | None = None) -> str:
    actions = ""
    if ctas:
        links = "".join(f'<a class="button {klass}" href="{href}">{escape(label)}</a>' for label, href, klass in ctas)
        actions = f'<div class="hero-actions page-actions">{links}</div>'
    breadcrumb_html = ""
    if breadcrumbs:
        items = []
        for label, href in breadcrumbs:
            if href:
                items.append(f'<li><a href="{href}">{escape(label)}</a></li>')
            else:
                items.append(f'<li aria-current="page">{escape(label)}</li>')
        breadcrumb_html = f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'
    return f"""
      <section class="page-hero">
        {responsive_image(prefix, image, "", class_name="page-hero-bg", loading="eager", decoding="async", sizes="100vw", aria_hidden="true")}
        <div class="page-hero-overlay"></div>
        <div class="page-hero-copy reveal is-visible">
          {breadcrumb_html}
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
              {responsive_image(prefix, image, name, loading="lazy", decoding="async", sizes="96px")}
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
        {responsive_image(prefix, "ich2026/conference-volcano.jpg", "Osorno Volcano and Petrohue waterfalls near Puerto Varas", class_name="ich-hero-bg", fetchpriority="high", sizes="100vw")}
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
            {responsive_image(prefix, "venue/puerto-varas-waterfront.jpg", "Puerto Varas waterfront and Lake Llanquihue", loading="lazy", decoding="async", sizes="(max-width: 1060px) 100vw, 420px")}
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
              {responsive_image(prefix, "ich2026/generated/scientific-program.jpg", "Researchers reviewing hantavirus program topics in a scientific session", loading="lazy", decoding="async", sizes="(max-width: 1060px) 100vw, 560px")}
              <div>
                <span>01</span>
                <h3>Scientific Program</h3>
                <p>Sessions span viral epidemiology, ecology, virus-host interaction, pathogenesis, clinical aspects, vaccines and therapeutics.</p>
                <a class="text-link" href="{local(prefix, "ich2026/programme/")}">View programme</a>
              </div>
            </article>
            <article class="ich-feature reveal">
              {responsive_image(prefix, "ich2026/generated/keynote-speakers.jpg", "Keynote speaker presenting hantavirus microscopy to a scientific audience", loading="lazy", decoding="async", sizes="(max-width: 1060px) 100vw, 560px")}
              <div>
                <span>02</span>
                <h3>Keynote Speakers</h3>
                <p>Invited experts highlight current developments across hantavirus research, clinical science and medical countermeasures.</p>
                <a class="text-link" href="{local(prefix, "ich2026/keynote-speakers/")}">See speakers</a>
              </div>
            </article>
            <article class="ich-feature reveal">
              {responsive_image(prefix, "ich2026/generated/abstract-registration.jpg", "Scientist preparing abstract submission and conference registration materials", loading="lazy", decoding="async", sizes="(max-width: 1060px) 100vw, 560px")}
              <div>
                <span>03</span>
                <h3>Abstract Submission & Registration</h3>
                <p>Submission and registration are handled through the conference form, with early registration timing listed on the registration page.</p>
                <a class="text-link" href="{local(prefix, "ich2026/abstracts-registration/")}">Registration details</a>
              </div>
            </article>
            <article class="ich-feature reveal">
              {responsive_image(prefix, "ich2026/generated/andes-virus-workshop.jpg", "Clinical and public health team working on Andes virus workshop materials in Southern Chile", loading="lazy", decoding="async", sizes="(max-width: 1060px) 100vw, 560px")}
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
            <h2>Scientific and local teams coordinating ICH2026 in Puerto Varas.</h2>
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
    crumbs = [("Home", local(prefix)), ("ICH2026", local(prefix, "ich2026/")), ("Keynote Speakers", None)]
    return f"""
      {page_hero(prefix, "Keynote speakers", "ICH2026 Keynote Speakers", "Invited speakers for the International Conference on Hantaviruses.", "venue/conference-landscape.png", breadcrumbs=crumbs)}
      <section class="section speakers">
        <div class="section-shell speaker-grid">
          <article class="speaker reveal">
            {responsive_image(prefix, "speakers/marcela-ferres.png", "Dr. Marcela Ferres", loading="lazy", decoding="async", sizes="196px")}
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
            {responsive_image(prefix, "speakers/jay-hooper.png", "Dr. Jay Hooper", loading="lazy", decoding="async", sizes="196px")}
            <div>
              <h2>Dr. Jay Hooper</h2>
              <p class="speaker-meta">United States Army Medical Research Institute of Infectious Diseases (USAMRIID), USA</p>
              <p>Dr. Jay Hooper is the Chief of the Molecular Virology Branch at USAMRIID. He has more than 30 years of research experience working with lethal viruses, mostly in Biosafety Level 3 and BSL-4 high-containment. His research is aimed at the discovery and development of medical countermeasures targeting high consequence viral diseases of military importance, including hemorrhagic fever and diseases caused by poxviruses.</p>
              <p>Dr. Hooper received a B.A. in Biology from Colby College in 1986 and a Ph.D. in Virology from Harvard University in 1995. His research has resulted in more than 100 peer-reviewed publications and 15 patents.</p>
              <a class="text-link" href="https://orcid.org/0000-0002-4475-0415" target="_blank" rel="noreferrer">ORCID profile</a>
            </div>
          </article>
        </div>
      </section>"""


def programme_page(prefix: str) -> str:
    crumbs = [("Home", local(prefix)), ("ICH2026", local(prefix, "ich2026/")), ("Programme", None)]
    return f"""
      {page_hero(prefix, "ICH2026 Program", "International Hantavirus Conference", "November 2-4, followed by the Andes Virus Workshop on November 5.", "ui/society-archive-2.png", [("Registration", local(prefix, "ich2026/abstracts-registration/"), "button-primary")], breadcrumbs=crumbs)}
      <section class="section program">
        <div class="section-shell">
          <div class="program-grid program-support">
            <article class="program-track reveal"><p class="track-date">November 2-4</p><h3>International Hantavirus Conference</h3><p>The meeting will cover the following topics:</p><ul><li>Viral epidemiology, evolution &amp; genetics</li><li>Virus ecology and climate change</li><li>Viral replication</li><li>Virus-host interactions</li><li>Pathogenesis</li><li>Vaccines &amp; therapeutics</li><li>Clinical aspects &amp; diagnostics</li></ul></article>
            <article class="program-track highlight reveal"><p class="track-date">November 5</p><h3>Andes Virus Workshop</h3><p>Topics will cover the following aspects:</p><ul><li>Translation of vaccine &amp; therapeutics candidates</li><li>Early diagnosis</li><li>Management of Andes virus-exposed persons</li><li>Surveillance of Andes virus</li><li>Regional Network</li><li>Other topics</li><li>Round Table discussion</li></ul><p class="track-note">This workshop will count with simultaneous translation (English-Spanish; Spanish-English).</p></article>
          </div>
        </div>
      </section>"""


def registration_page(prefix: str) -> str:
    crumbs = [("Home", local(prefix)), ("ICH2026", local(prefix, "ich2026/")), ("Abstracts & Registration", None)]
    return f"""
      {page_hero(prefix, "ICH2026 Registration & Abstract Submission", "Registration and abstract submission.", "Abstract submission opens in May 2026, with early bird registration planned for May-July.", "venue/puerto-varas-waterfront.jpg", [("Conference form", CONFERENCE_FORM, "button-primary"), ("Contact", contact_href(prefix), "button-secondary")], breadcrumbs=crumbs)}
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
    links = "".join(travel_link_card(icon, label, description, href) for icon, label, description, href in TRAVEL_LINKS)
    crumbs = [("Home", local(prefix)), ("ICH2026", local(prefix, "ich2026/")), ("Venue & Travel", None)]
    return f"""
      {page_hero(prefix, "ICH2026 Venue & Travel", "Hotel Bellavista, Puerto Varas.", "The 2026 meeting will take place in the Hotel Bellavista, Puerto Varas.", "venue/hotel-bellavista.jpg", [("Open map", "https://goo.gl/maps/dv2jUC4hSGLvr2Ld9", "button-primary"), ("Hotel Bellavista", "https://hotelbellavista.cl/reuniones-y-eventos-corporativos-2/", "button-secondary")], breadcrumbs=crumbs)}
      <section class="section venue">
        <div class="section-shell venue-layout">
          <div class="venue-copy reveal">
            <p class="eyebrow">How to get to Puerto Varas</p>
            <h2>A practical route into the Chilean Lake District.</h2>
            <div class="venue-address">
              <span>Venue address</span>
              <a href="https://goo.gl/maps/dv2jUC4hSGLvr2Ld9" target="_blank" rel="noreferrer">Av. Vicente Perez Rosales #060, Puerto Varas</a>
            </div>
            <div class="travel-steps">
              <div><span>Arrival</span><strong>Santiago (SCL)</strong><small>Immigration, luggage and domestic connection.</small></div>
              <div><span>Connection</span><strong>Puerto Montt (PMC)</strong><small>Domestic flight to El Tepual Airport.</small></div>
              <div><span>Transfer</span><strong>Puerto Varas</strong><small>Private transfer, taxi, bus or shuttle to the venue.</small></div>
            </div>
          </div>
          <figure class="venue-image reveal">{responsive_image(prefix, "venue/puerto-varas-waterfront.jpg", "Hotel Bellavista conference room", loading="lazy", decoding="async", sizes="(max-width: 1060px) 100vw, 520px")}<figcaption>Hotel Bellavista conference facilities</figcaption></figure>
        </div>
      </section>
      <section class="section intro-band">
        <div class="section-shell travel-detail-list">
          <article class="reveal">
            <p class="eyebrow">International arrival</p>
            <h2>Arrive through Santiago (SCL)</h2>
            <p>Most international travelers will arrive at Arturo Merino Benítez International Airport (SCL) in Santiago, Chile.</p>
            <h3>After landing</h3>
            <ul><li>Proceed through immigration and customs</li><li>Collect your luggage</li><li>Follow signs for domestic connections</li></ul>
            <p><strong>Tip:</strong> Allow at least 2-3 hours for connection time, especially if arriving from long-haul international flights.</p>
            <p>Alternatively, you may prefer to make a stop-over in Santiago. There are several hotels near the airport. It is also possible to book <a class="text-link" href="https://www.tripadvisor.com/Attractions-g294305-Activities-c42-t205-Santiago_Santiago_Metropolitan_Region.html" target="_blank" rel="noreferrer">day trips</a> to diverse destinations, close to, or in <a class="text-link" href="https://www.viator.com/Santiago/d713?pid=P00095352&mcid=42383&medium=link&campaign=scltours" target="_blank" rel="noreferrer">Santiago</a>.</p>
          </article>
          <article class="reveal">
            <p class="eyebrow">Domestic connection</p>
            <h2>Fly from Santiago to Puerto Montt (PMC)</h2>
            <p>From Santiago, take a domestic flight to El Tepual Airport (PMC) in Puerto Montt.</p>
            <ul><li>Flight duration: approximately 1 hour 40 minutes</li><li>Airlines operate multiple daily flights</li></ul>
            <p><strong>Tip:</strong> Puerto Montt is the main gateway to the Los Lagos region and Puerto Varas.</p>
          </article>
          <article class="reveal">
            <p class="eyebrow">Airport transfer</p>
            <h2>Connect from Puerto Montt Airport to Puerto Varas</h2>
            <p>Puerto Varas is located approximately 20-30 km from the airport, with a travel time of about 25-30 minutes depending on traffic.</p>
            <p>Upon arrival at the airport, you will find several transportation options.</p>
            <h3>Private or Shared Transfer</h3>
            <ul><li>Pre-booked or available at the airport</li><li>Drop-off directly at your hotel</li><li>Travel time: ~30 minutes</li><li>Approximate amount: 15-25 USD</li></ul>
            <p>You can find more information through <a class="text-link" href="https://ww2.trasladoaeropuerto.cl/" target="_blank" rel="noreferrer">Airport Transfer</a>, <a class="text-link" href="https://api.whatsapp.com/send?phone=56976053701&text=hola,%20lo%20contacto%20desde%20la%20p%C3%A1gina%20web" target="_blank" rel="noreferrer">WhatsApp +56976053701</a>, <a class="text-link" href="mailto:reservas@trasladoaeropuerto.cl">reservas@trasladoaeropuerto.cl</a>, or <a class="text-link" href="https://www.survip.cl/transfer-aeropuerto-puerto-montt-a-puerto-varas.php" target="_blank" rel="noreferrer">Survip transfer</a>.</p>
            <h3>Taxi</h3>
            <ul><li>Available directly outside the terminal</li><li>Travel time: ~25-30 minutes</li><li>Safe and widely used</li><li>Estimated cost: 20-30 USD</li></ul>
            <h3>Bus / Shuttle</h3>
            <ul><li>Budget-friendly option</li><li>Travel time: ~30-40 minutes depending on route</li><li>Estimated cost: 2 USD</li><li>Departures from Puerto Montt bus terminal</li></ul>
            <p>Taxis and transfers are the most convenient options for international travelers.</p>
          </article>
          <article class="reveal">
            <p class="eyebrow">Final destination</p>
            <h2>Puerto Varas</h2>
            <p>Puerto Varas is a scenic lakeside city located in southern Chile, known for:</p>
            <ul><li>Lake Llanquihue</li><li>Osorno Volcano</li><li>Easy access to national parks and research sites</li></ul>
            <h3>Travel Tips</h3>
            <ul><li>Currency: Chilean Peso (CLP)</li><li>Most taxis and services accept cards, but carrying some cash is recommended</li><li>Weather can change quickly - bring appropriate clothing</li><li>Spanish is the local language, but basic English is commonly understood in tourism services</li></ul>
          </article>
        </div>
      </section>
      <section class="section data-section">
        <div class="section-shell"><div class="section-heading compact reveal"><p class="eyebrow">Travel resources</p><h2>Venue, airport and transfer contacts for ICH2026 participants.</h2></div><div class="travel-link-list reveal">{links}</div></div>
      </section>"""


def sponsors_page(prefix: str) -> str:
    cards = "".join(
        f'<a class="sponsor reveal" href="{href}" target="_blank" rel="noreferrer">{responsive_image(prefix, image, name, loading="lazy", decoding="async", sizes="220px")}<span>{escape(name)}</span></a>'
        for name, href, image in SPONSORS
    )
    crumbs = [("Home", local(prefix)), ("ICH2026", local(prefix, "ich2026/")), ("Partners & Sponsors", None)]
    return f"""
      {page_hero(prefix, "Partners & sponsors", "Institutional support across Chilean science and public research.", "ICH2026 is supported by Chilean scientific societies, universities and public research agencies.", "ui/society-archive-1.png", breadcrumbs=crumbs)}
      <section class="section sponsors"><div class="section-shell"><div class="sponsor-grid" role="list">{cards}</div></div></section>"""


def contact_section() -> str:
    return f"""
      <section class="section contact" id="contact">
        <div class="section-shell contact-layout">
          <div class="section-heading reveal"><p class="eyebrow">Contact</p><h2>CONTACT ICH2026 Organizers</h2></div>
          <div class="contact-actions reveal"><a class="contact-email" href="mailto:ICH2026@hantavirussociety.org">ICH2026@hantavirussociety.org</a></div>
        </div>
      </section>"""


def contact_page(prefix: str) -> str:
    return contact_section()


def about_page(prefix: str) -> str:
    return f"""
      {page_hero(prefix, "About ISH", "About the International Society for Hantaviruses", "Founded in 1989 with its first Meeting in Seoul (Korea).", "about-hantavirus-microscopy-pixnio.jpg", [("Apply for ISH Membership", MEMBERSHIP_FORM, "button-primary")])}
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
            {responsive_image(prefix, "ui/society-archive-2.png", "ICH2023 Seoul meeting participants", loading="lazy", decoding="async", sizes="(max-width: 780px) 100vw, 1180px")}
            <figcaption>ICH2023 Seoul | Republic of Korea</figcaption>
          </figure>
        </div>
      </section>
      <section class="section committees">
        <div class="section-shell">
          <div class="section-heading compact reveal">
            <p class="eyebrow">International Advisory Board</p>
            <h2>Global advisory leadership across hantavirus-affected regions.</h2>
          </div>
          {advisory_grid(prefix)}
        </div>
      </section>
      {contact_section()}"""


PAGES = [
    ("index.html", "home", "International Society for Hantaviruses", "International Society for Hantaviruses and ICH2026 in Puerto Varas, Chile.", home_page),
    ("about-ish/index.html", "about", "About ISH | International Society for Hantaviruses", "About the International Society for Hantaviruses.", about_page),
    ("ich2026/index.html", "ich2026", "ICH2026 | International Society for Hantaviruses", "International Conference on Hantaviruses 2026 in Puerto Varas, Chile.", ich2026_page),
    ("ich2026/keynote-speakers/index.html", "keynote", "Keynote Speakers | ICH2026", "Keynote speakers for ICH2026.", keynote_page),
    ("ich2026/programme/index.html", "programme", "Programme | ICH2026", "Scientific programme for ICH2026.", programme_page),
    ("ich2026/abstracts-registration/index.html", "registration", "Abstracts & Registration | ICH2026", "Abstract submission and registration for ICH2026.", registration_page),
    ("ich2026/venue/index.html", "venue", "Venue | ICH2026", "Venue and travel information for ICH2026.", venue_page),
    ("ich2026/partners-sponsors/index.html", "sponsors", "Partners & Sponsors | ICH2026", "Partners and sponsors for ICH2026.", sponsors_page),
    ("contact/index.html", "contact", "Contact | ICH2026", "Contact the ICH2026 organizing team.", contact_page),
]


def generate_sitemap() -> None:
    urls = []
    priorities = {"home": "1.0", "about": "0.9", "ich2026": "0.9"}
    for out_path, active, *_ in PAGES:
        page_dir = str(Path(out_path).parent)
        loc = SITE_URL + "/" if page_dir == "." else f"{SITE_URL}/{page_dir}/"
        priority = priorities.get(active, "0.8")
        changefreq = "weekly" if active in ("home", "about", "ich2026") else "monthly"
        urls.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>{changefreq}</changefreq>\n    <priority>{priority}</priority>\n  </url>"
        )
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "\n".join(urls)
    sitemap += "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print("sitemap.xml")


def main() -> None:
    for out_path, active, title, description, builder in PAGES:
        prefix = prefix_for(out_path)
        html = clean_output(doc(out_path, active, title, description, builder(prefix)))
        target = ROOT / out_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        print(out_path)
    generate_sitemap()


if __name__ == "__main__":
    main()
