const body = document.body;
const menu = document.querySelector("[data-menu]");
const menuToggle = document.querySelector("[data-menu-toggle]");
const menuBackdrop = document.querySelector("[data-menu-backdrop]");
const navLinks = Array.from(document.querySelectorAll(".site-nav a"));
const mobileQuery = window.matchMedia("(max-width: 1100px)");
const sections = navLinks
  .map((link) => {
    const href = link.getAttribute("href") || "";
    if (!href.startsWith("#")) return null;
    try {
      return document.querySelector(href);
    } catch {
      return null;
    }
  })
  .filter(Boolean);

function setMenu(open) {
  menu.classList.toggle("is-open", open);
  menuToggle.setAttribute("aria-expanded", String(open));
  menuToggle.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
  body.classList.toggle("menu-open", open);
  if (menuBackdrop) {
    menuBackdrop.hidden = !open;
  }
  syncMenuAccessibility(open);
}

function syncMenuAccessibility(open = menu.classList.contains("is-open")) {
  const hidden = mobileQuery.matches && !open;
  menu.setAttribute("aria-hidden", String(hidden));
  navLinks.forEach((link) => {
    if (hidden) {
      link.setAttribute("tabindex", "-1");
    } else {
      link.removeAttribute("tabindex");
    }
  });
}

menuToggle.addEventListener("click", () => {
  setMenu(!menu.classList.contains("is-open"));
});

navLinks.forEach((link) => {
  link.addEventListener("click", () => setMenu(false));
});

if (menuBackdrop) {
  menuBackdrop.addEventListener("click", () => setMenu(false));
}

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 }
);

document.querySelectorAll(".reveal:not(.is-visible)").forEach((element) => {
  revealObserver.observe(element);
});

const navObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const id = `#${entry.target.id}`;
      navLinks.forEach((link) => {
        link.classList.toggle("active", link.getAttribute("href") === id);
      });
    });
  },
  { rootMargin: "-35% 0px -55% 0px", threshold: 0 }
);

sections.forEach((section) => navObserver.observe(section));

const currentPage = body.dataset.page;
if (currentPage) {
  navLinks.forEach((link) => {
    link.classList.toggle("active", link.dataset.nav === currentPage);
  });
}

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    setMenu(false);
  }
});

const committeeFilters = Array.from(document.querySelectorAll("[data-committee-filter]"));
const committeeSections = Array.from(document.querySelectorAll("[data-committee-section]"));

function setCommitteeFilter(filter) {
  committeeFilters.forEach((button) => {
    const active = button.dataset.committeeFilter === filter;
    button.classList.toggle("is-active", active);
    button.setAttribute("aria-pressed", String(active));
  });

  committeeSections.forEach((section) => {
    const visible = filter === "all" || section.dataset.committeeSection === filter;
    section.classList.toggle("is-hidden", !visible);
  });
}

committeeFilters.forEach((button) => {
  button.addEventListener("click", () => setCommitteeFilter(button.dataset.committeeFilter));
});

if (committeeFilters.length) {
  setCommitteeFilter("all");
}

mobileQuery.addEventListener("change", () => {
  if (!mobileQuery.matches) {
    setMenu(false);
  }
  syncMenuAccessibility();
});

syncMenuAccessibility();
